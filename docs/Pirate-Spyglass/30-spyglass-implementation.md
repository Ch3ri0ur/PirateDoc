# Implementation

BerryMSE is a project produces a one file executable which runs on the RaspberryPi and streams the Camera to the Website via Websocket.
Almost everything in this Project written in the Programming Language Golang and only the Website needs to contain HTML and JavaScript code.

## Short Summary

Camera - RawImage - Camera Driver - V4L2 - H.264 NAL Units - BerryMSE MPEG-4 Part15 - BerryMSE WebSocket - JavaScript Websocket - JavaScript MSE - HTML Video Element


## Camera to H.264 NAL Unit Stream

[V4L2](Theory/Camera and Driver/v4l2.md)
[H.264](Theory/Video/h264.md)

## H.264 NAL Unit Stream to WS Stream

[H.264](Theory/Video/h264.md)
[MPEG-4](Theory/Video/mpeg4.md)

## WS Stream to Video

[MPEG-4](Theory/Video/mpeg4.md)
[MSE](Theory/Video/mse.md)

### Hardware

Matching the used Raspberry Pi, a Raspberry Pi camera module is used to capture image data. This data is provided in a [v4l2] format 
- A Raspberry Pi camera module provides the driver with raw image data.
- The v4l2 video driver (Legacy Raspberry Pi Buster Stack)
  - hardware accelerated encoding
  - generates mp4 part 10 NAL units

### Server
- A server to
  -  wrap the encoded h264 fragments into 
  - Provide websocket endpoints to send the fragments

### Client
- Client side the MSE is used to enable playback in a \<video\> tag.




H.264 Network Abstraction Layer (NAL) units are read from `/dev/video0`, a
Video4Linux2 compatible camera interface. Each unit corresponds to one frame.
Frames are packaged into MPEG-4 ISO BMFF (ISO/IEC 14496-12) compliant
fragments and sent via a websocket to the browser client. The client appends
each received buffer to the media source for playback.
