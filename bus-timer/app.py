"""Say when the next MBTA bus leaves my stop, as one sentence for Siri."""

import json
import os
import traceback
import urllib.parse
import urllib.request
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from zoneinfo import ZoneInfo

BOSTON = ZoneInfo("America/New_York")
MBTA_URL = "https://api-v3.mbta.com/predictions"

STOP_ID = os.environ.get("STOP_ID", "3614")
ROUTE_ID = os.environ.get("ROUTE_ID", "220")
DIRECTION_ID = os.environ.get("DIRECTION_ID", "1")
DESTINATION = os.environ.get("DESTINATION", "Quincy Center")
PORT = int(os.environ.get("PORT", "8220"))
API_KEY = os.environ.get("MBTA_API_KEY", "")


def upcoming_departures(payload, now):
    """Return the predicted departure times that are not in the past, sorted."""
    departures = []
    for item in payload.get("data", []):
        attributes = item.get("attributes", {})
        stamp = attributes.get("departure_time") or attributes.get("arrival_time")
        if stamp is None:
            continue
        when = datetime.fromisoformat(stamp)
        if when >= now:
            departures.append(when)
    return sorted(departures)


def describe_wait(when, now):
    minutes = int((when - now).total_seconds() // 60)
    if minutes < 1:
        return "arriving now"
    if minutes == 1:
        return "in 1 minute"
    return f"in {minutes} minutes"


def clock_time(when):
    local = when.astimezone(BOSTON)
    return f"{local.hour % 12 or 12}:{local.minute:02d}"


def format_message(departures, now, route, destination):
    """Make the sentence Siri speaks from the first two departures."""
    if not departures:
        return f"No {route} buses are predicted right now."
    first = departures[0]
    message = (
        f"The next {route} to {destination} is "
        f"{describe_wait(first, now)}, at {clock_time(first)}."
    )
    if len(departures) == 1:
        return message + " No other buses are predicted yet."
    return message + f" The one after is {describe_wait(departures[1], now)}."


def fetch_predictions():
    """Get the live predictions for our stop, route and direction from the MBTA."""
    query = urllib.parse.urlencode({
        "filter[stop]": STOP_ID,
        "filter[route]": ROUTE_ID,
        "filter[direction_id]": DIRECTION_ID,
        "sort": "departure_time",
    })
    request = urllib.request.Request(f"{MBTA_URL}?{query}")
    if API_KEY:
        request.add_header("x-api-key", API_KEY)
    with urllib.request.urlopen(request, timeout=10) as response:
        return json.load(response)


def bus_message():
    """Return the sentence for Siri. A failed MBTA call is logged, not raised."""
    try:
        payload = fetch_predictions()
    except Exception:
        traceback.print_exc()
        return "I couldn't reach the MBTA right now."
    now = datetime.now(BOSTON)
    return format_message(upcoming_departures(payload, now), now, ROUTE_ID, DESTINATION)


class BusHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if urllib.parse.urlsplit(self.path).path != "/bus":
            self.send_error(404)
            return
        body = bus_message().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    server = ThreadingHTTPServer(("", PORT), BusHandler)
    print(f"Listening on port {PORT}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
