# Bus Timer — Design

## Goal

Say "Hey Siri, when is my bus" on an iPhone at home and hear when the next
MBTA Route 220 bus arrives at my stop, heading to Quincy Center.

The answer must come from the Synology NAS, because the Mac is not always on.

## Fixed facts

| Item | Value |
|------|-------|
| Route | `220` |
| Stop | `3614` — Bridge St @ Blackstone Rd |
| Direction | `1` — Inbound, to Quincy Center Station |
| NAS | Synology DS218+, DSM 7.2.2, x86_64, IP `192.168.50.251` |
| Docker | Container Manager 24.0.2 (installed 2026-10-10) |
| Network reach | Home Wi-Fi only. The service is not exposed to the internet. |

## Architecture

```
iPhone Shortcut ──HTTP GET──▶ NAS :8220 /bus ──HTTPS──▶ api-v3.mbta.com/predictions
      ▲                                │
      └──────── plain-text sentence ◀──┘
```

1. A Siri Shortcut named **"When is my bus"** runs two actions:
   *Get Contents of URL* `http://192.168.50.251:8220/bus`, then *Speak Text*.
2. A small Python service on the NAS gets the predictions from the MBTA
   and returns one plain-text sentence.

## Components

### `app.py`

- Uses the Python standard library only (`http.server`, `urllib`, `json`,
  `datetime`). No third-party packages.
- Has one endpoint: `GET /bus`. It returns `text/plain; charset=utf-8`.
  All other paths return 404.
- Reads its settings from environment variables:
  - `MBTA_API_KEY` (optional). Without a key the MBTA allows 20 requests
    per minute, which is enough, but a key is recommended.
  - `STOP_ID` (default `3614`)
  - `ROUTE_ID` (default `220`)
  - `DIRECTION_ID` (default `1`)
  - `DESTINATION` (default `Quincy Center`). This is used in the spoken
    sentence.
  - `PORT` (default `8220`)
- Calls the MBTA with this request:
  `GET https://api-v3.mbta.com/predictions?filter[stop]=…&filter[route]=…&filter[direction_id]=…&sort=departure_time`
  with the header `x-api-key` when a key is set, and a timeout of 10 seconds.
- The code has two pure functions, so they can be tested without a network:
  - `upcoming_departures(payload, now) -> list[datetime]`. It takes each
    prediction's `departure_time`, or `arrival_time` when there is no
    departure time, and drops missing times and times before `now`. It
    returns the times sorted.
  - `format_message(departures, now, route, destination) -> str`. It makes
    the spoken sentence from the first two departures.

### Messages

| Case | Message |
|------|---------|
| 2 or more buses | "The next 220 to Quincy Center is in 6 minutes, at 7:42. The one after is in 21 minutes." |
| 1 bus | "The next 220 to Quincy Center is in 6 minutes, at 7:42. No other buses are predicted yet." |
| Less than 1 minute away | "…is arriving now…" |
| No buses | "No 220 buses are predicted right now." |
| MBTA error or timeout | "I couldn't reach the MBTA right now." The full exception is written to stderr, so it shows in the container log. |

- Clock times use 12-hour format with no AM/PM, in `America/New_York`. MBTA
  times already include a timezone offset, so we convert them to that zone.
- Minutes are rounded down.

### Deployment files

- `Dockerfile`: `python:3.12-slim`. It copies `app.py` and runs it.
- `docker-compose.yml`: one service, `bus-timer`. It maps port `8220:8220`,
  uses `restart: unless-stopped`, and reads `env_file: .env`.
- `.env.example`: lists the variables. The real `.env` is ignored by git.
- On the NAS, the files go in `/volume1/docker/bus-timer`. The user
  creates a **Project** in the Container Manager web UI and points it at
  that folder. Docker needs root, so the user does this step, not Claude.

## Testing

- `test_app.py` uses `unittest` and fixed MBTA JSON samples. It tests these
  cases: two or more buses, one bus, no buses, predictions in the past,
  predictions with no `departure_time` (we use `arrival_time` instead),
  and the "arriving now" case.
- Live check: run `curl http://192.168.50.251:8220/bus` from the Mac after
  the deploy.
- Final check: say "Hey Siri, when is my bus" on the iPhone.

## Out of scope

- Access from outside the home network (for example, Tailscale).
- More than one stop or route, and different stops by time of day.
- Service alerts or detours.
