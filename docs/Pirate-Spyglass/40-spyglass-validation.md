# Validation

## Tests

Visual tests by recursively filming a stopwatch showed a latency below 300ms.

Stress tests with up to 5 Streams showed only minor CPU utilization on the Raspberry Pi.

Long term tests only stopped when the websocket connection was closed by the browser (during standby for instance) after multiple hours. The reset Button works 

The server never generated any problems or crashes.

## Future steps and Improvements

- Replace Websocket connection with Webtransport
- Replace MSE with Webcodecs
- Add fallback for iOS
- Add configuration for resolution and bandwith
- Add USB Webcam support
- Add Server reboot on crash (even though it was rock solid during testing)