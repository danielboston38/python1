import threading
import unittest
import urllib.error
import urllib.request
from datetime import datetime
from http.server import ThreadingHTTPServer
from unittest import mock

import app
from app import BOSTON, BusHandler, bus_message, format_message, upcoming_departures

NOW = datetime(2026, 10, 10, 7, 36, tzinfo=BOSTON)


def prediction(departure=None, arrival=None):
    return {"attributes": {"departure_time": departure, "arrival_time": arrival}}


def at(hour, minute, second=0):
    return datetime(2026, 10, 10, hour, minute, second, tzinfo=BOSTON)


class UpcomingDeparturesTest(unittest.TestCase):
    def test_returns_future_departures_sorted(self):
        payload = {"data": [
            prediction("2026-10-10T07:57:30-04:00"),
            prediction("2026-10-10T07:42:00-04:00"),
        ]}
        self.assertEqual(upcoming_departures(payload, NOW), [at(7, 42), at(7, 57, 30)])

    def test_drops_departures_in_the_past(self):
        payload = {"data": [
            prediction("2026-10-10T07:30:00-04:00"),
            prediction("2026-10-10T07:42:00-04:00"),
        ]}
        self.assertEqual(upcoming_departures(payload, NOW), [at(7, 42)])

    def test_uses_arrival_time_when_departure_is_missing(self):
        payload = {"data": [prediction(None, "2026-10-10T07:50:00-04:00")]}
        self.assertEqual(upcoming_departures(payload, NOW), [at(7, 50)])

    def test_skips_predictions_without_times(self):
        payload = {"data": [prediction(None, None), prediction("2026-10-10T07:42:00-04:00")]}
        self.assertEqual(upcoming_departures(payload, NOW), [at(7, 42)])

    def test_empty_data(self):
        self.assertEqual(upcoming_departures({"data": []}, NOW), [])


class FormatMessageTest(unittest.TestCase):
    def test_two_buses(self):
        self.assertEqual(
            format_message([at(7, 42), at(7, 57, 30)], NOW, "220", "Quincy Center"),
            "The next 220 to Quincy Center is in 6 minutes, at 7:42. "
            "The one after is in 21 minutes.",
        )

    def test_one_bus(self):
        self.assertEqual(
            format_message([at(7, 42)], NOW, "220", "Quincy Center"),
            "The next 220 to Quincy Center is in 6 minutes, at 7:42. "
            "No other buses are predicted yet.",
        )

    def test_no_buses(self):
        self.assertEqual(
            format_message([], NOW, "220", "Quincy Center"),
            "No 220 buses are predicted right now.",
        )

    def test_under_a_minute_is_arriving_now(self):
        self.assertEqual(
            format_message([at(7, 36, 40)], NOW, "220", "Quincy Center"),
            "The next 220 to Quincy Center is arriving now, at 7:36. "
            "No other buses are predicted yet.",
        )

    def test_one_minute_is_singular(self):
        self.assertEqual(
            format_message([at(7, 37, 30)], NOW, "220", "Quincy Center"),
            "The next 220 to Quincy Center is in 1 minute, at 7:37. "
            "No other buses are predicted yet.",
        )

    def test_clock_time_is_12_hour(self):
        now = at(13, 0)
        self.assertEqual(
            format_message([at(13, 5)], now, "220", "Quincy Center"),
            "The next 220 to Quincy Center is in 5 minutes, at 1:05. "
            "No other buses are predicted yet.",
        )

    def test_clock_time_is_converted_to_boston(self):
        payload = {"data": [prediction("2026-10-10T11:42:00Z")]}
        departures = upcoming_departures(payload, NOW)
        self.assertEqual(
            format_message(departures, NOW, "220", "Quincy Center"),
            "The next 220 to Quincy Center is in 6 minutes, at 7:42. "
            "No other buses are predicted yet.",
        )


class BusMessageTest(unittest.TestCase):
    def test_mbta_failure_gives_spoken_error(self):
        failure = urllib.error.HTTPError(app.MBTA_URL, 429, "Too Many Requests", {}, None)
        with mock.patch("app.fetch_predictions", side_effect=failure), \
                mock.patch("sys.stderr"):
            self.assertEqual(bus_message(), "I couldn't reach the MBTA right now.")

    def test_success_uses_predictions(self):
        with mock.patch("app.fetch_predictions", return_value={"data": []}):
            self.assertEqual(bus_message(), "No 220 buses are predicted right now.")


class ServerTest(unittest.TestCase):
    def setUp(self):
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), BusHandler)
        self.base = f"http://127.0.0.1:{self.server.server_port}"
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        patcher = mock.patch("app.bus_message", return_value="Test sentence.")
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)

    def get(self, path):
        with mock.patch.object(BusHandler, "log_message"):
            return urllib.request.urlopen(self.base + path, timeout=5)

    def test_bus_returns_plain_text_sentence(self):
        with self.get("/bus") as response:
            self.assertEqual(response.status, 200)
            self.assertEqual(response.headers["Content-Type"], "text/plain; charset=utf-8")
            self.assertEqual(response.read().decode("utf-8"), "Test sentence.")

    def test_bus_path_with_query_string(self):
        with self.get("/bus?x=1") as response:
            self.assertEqual(response.read().decode("utf-8"), "Test sentence.")

    def test_other_paths_are_404(self):
        for path in ("/", "/busy", "/favicon.ico"):
            with self.subTest(path=path), self.assertRaises(urllib.error.HTTPError) as caught:
                self.get(path)
            self.assertEqual(caught.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
