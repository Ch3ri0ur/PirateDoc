# Implementation

The BerryMSE project is so designed that it produces an one file executable, which runs on the RaspberryPi and streams the [RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md) via Websocket. A Demo Website is contained in the executable and is reachable on the given address, but its also possible to integrate the video in other websites via a small JavaScript. The Integration and Display in the Website happens via [MSE](Theory/Video/mse.md) Extension, which almost every Browser has already implemented.

The Implementation is focused on using as less components as possible and be very lightweight in performance and Network traffic. This is achieved by not doing any Decoding and Encoding on the RaspberryPi and using the [H.264](Theory/Video/h264.md) Compression of the [RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md). By using the very optimized [MSE](Theory/Video/mse.md) of the Browser to decode the Video only a Transport of the [H.264 NAL Units](Theory/Video/h264.md) is needed. This is performed via Websocket, which is also very easy to setup and doesn't needs extra server infrastructure, like a STUN/TURN Server for [WebRTC](Theory/webRTC.md).

Almost the complete Project is written in the Programming Language Golang. Only for the Website is HTML and JavaScript code necessary.

Only the [RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md) is currently supported and also only works with the default settings for Width, Height and Bitrate. The Reason for this is, that the [H.264 Parameter](Theory/Video/h264.md) are currently Hardcoded. Further Goal is to support this Settings and also make it possible to use other [Cameras](Theory/Camera%20and%20Driver/h264camera.md) that support [H.264](Theory/Video/h264.md).

## Short Summary

Camera - RawImage - Camera Driver - V4L2 - H.264 NAL Units - BerryMSE - NAL Unit ISOBMFF MPEG-4 Part15 - BerryMSE WebSocket - JavaScript Websocket - JavaScript MSE - HTML Video Element



H.264 Network Abstraction Layer (NAL) units are read from `/dev/video0`, a
Video4Linux2 compatible camera interface. Each unit corresponds to one frame.
Frames are packaged into MPEG-4 ISO BMFF (ISO/IEC 14496-12) compliant
fragments and sent via a websocket to the browser client. The client appends
each received buffer to the media source for playback.


## Camera to H.264 NAL Unit Stream

[V4L2](Theory/Camera%20and%20Driver/v4l2.md)
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



