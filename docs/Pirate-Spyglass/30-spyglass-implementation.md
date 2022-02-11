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