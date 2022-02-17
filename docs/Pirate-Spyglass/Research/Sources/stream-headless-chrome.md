# Self implemented WebRTC

In the research for WebRTC Streamer solutions, a often found result have been tutorials for a webbrowser implemented video call room. This used the Webbrowser to perform a WebRTC Stream to all other member of the room. A simple Server did just the signaling of the SDP.

- Quelle: https://www.youtube.com/watch?v=h2WkZ0h0-Rc&list=PL_YW-znSZ_dK365WaVuiBUN6FYc9_1hni&index=1

Based on these Solution an Special Implementation was made that streamed the Usermedia of the Host to many.

- Private Repository: https://github.com/KingMaxi95/BroadcastLocalUserMediaWebRTC

This Implementation had one website for the Host and a Website for the Users to connected to the stream. The Host page just had to be opened on the raspberry Pi to Start Streaming and the Server would transmit the SDP's from and to the Users.

To Automate the Host side the server just starts a Headless Chromium Webbrowser that opens the Hostpage.

This concept worked very well and didn't used many extra components, just:

- node to serve and coordinate everything
- puppeteer extension for node to manage a webbrowser ([puppeteer](https://github.com/puppeteer/puppeteer) is from a Google developer)
- chromium as web browser (automatically installed with puppeteer and is a Open source Webbrowser)

But the chromium Webbrowser didn't allowed to do custom settings to the Raspberry Pi Camera, when the usermedia was called. It used the v4l2 driver and changed settings of it back to the only supported formats:

- MJPEG 1280x780 30fps
- YUV 480x320 30fps

Both needed Resources for conversion, because WebRTC uses only V8 or H264 for transmission. Also the H264 from the Raspi Cam needed to be converted from h264 to the named Formats before, what already used about 30% of one Processor with the webbrowser environment.

This double conversion used a lot of resources and each new user that needed a stream caused a significant rise in processor usage, so that only 3 fully occupied the 4 processors of the Raspberry Pi.

The Solution could be Promising if the multi compression that happens for each user could be reduced and the original H264 Format of the Camera could be used.

Further Investigations should be made on:

- Re-Re-Stream: Send the Stream to yourself so that it is compressed and than to the users (only one compression and not for each new user)
- GStreamer WebRTC Implementation. https://gstreamer.freedesktop.org/documentation/webrtc/index.html?gi-language=c
- ALternative video driver or webbrowser