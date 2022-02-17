# Implementation

The BerryMSE project is so designed that it produces an one file executable, which runs on the RaspberryPi and streams the [RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md) via Websocket. A Demo Website is contained in the executable and is reachable on the given address, but its also possible to integrate the video in other websites via a small JavaScript. The Integration and Display in the Website happens via [MSE](Theory/Video/mse.md) Extension, which almost every Browser has already implemented.

The Implementation is focused on using as less components as possible and be very lightweight in performance and Network traffic. This is achieved by not doing any Decoding and Encoding on the RaspberryPi and using the [H.264](Theory/Video/h264.md) Compression of the [RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md). By using the very optimized [MSE](Theory/Video/mse.md) of the Browser to decode the Video only a Transport of the [H.264 NAL Units](Theory/Video/h264.md) is needed. This is performed via Websocket, which is also very easy to setup and doesn't needs extra server infrastructure, like a STUN/TURN Server for [WebRTC](Research/webRTC.md).

Almost the complete Project is written in the Programming Language Golang. Only for the Website is HTML and JavaScript code necessary.

Only the [RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md) is currently supported and also only works with the default settings for Width, Height and Bitrate. The Reason for this is, that the [H.264 Parameter](Theory/Video/h264.md) are currently Hardcoded. Further Goal is to support this Settings and also make it possible to use other [Cameras](Theory/Camera%20and%20Driver/h264camera.md) that support [H.264](Theory/Video/h264.md).

## Brief Process Overview

1. Camera ([RPiCam](Theory/Camera%20and%20Driver/rpicamera.md), [H264 Camera](Theory/Camera%20and%20Driver/h264camera.md))
    - Produces RawImage Data.
2. Camera Driver ([libcamera](Theory/Camera%20and%20Driver/libcamera.md), [raspicam](Theory/Camera%20and%20Driver/legacycameraStack.md))
    - Converts Imagedata from Camera to selected data format, [H.264 NAL Units](Theory/Video/h264.md).
3. V4L2 Driver
    - Stores Image Data in Buffer and provides Device Interface on the Device Node, ``/dev/video0``.
4. BerryMSE
    1. Source [goV4l2](Theory/Camera%20and%20Driver/goV4l2.md)
            - Retrieves single [NAL Unit](Theory/Video/h264.md) from Device Node and adds it to the Hubs Buffer.
    2. Hub
            - [AVCFF MPEG-4 Part 15](Theory/Video/mpeg4.md) conform packages by storing [NAL Units](Theory/Video/h264.md) into [ISOBMFF](Theory/Video/mpeg4.md) Structure. 
    3. Websocket
            - Created [AVCFF](Theory/Video/avcff.md) conform packages (Frames) get send to register WebSocket Clients. 
5. JavaScript
    1. Websocket
        - Append [AVCFF](Theory/Video/avcff.md) packages in [MSE SourceBuffer](Theory/Video/mse.md).
    2. MSE
        - Creates Video by Decode [H.264](Theory/Video/h264.md) out the received NAL Units.
6. HTML Video Element
    - Displays Video on Website.

TODO


## Camera to H.264 NAL Unit Stream

[RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md)
[raspicam Driver](Theory/Camera%20and%20Driver/legacycameraStack.md)
[V4L2](Theory/Camera%20and%20Driver/v4l2.md)
[H.264](Theory/Video/h264.md)

## H.264 NAL Unit Stream to WS Stream

[H.264](Theory/Video/h264.md)
[MPEG-4](Theory/Video/mpeg4.md)

## WS Stream to Video

[MPEG-4](Theory/Video/mpeg4.md)
[MSE](Theory/Video/mse.md)


## Website
    Gets Http Served Website
    Client side the MSE is used to enable playback in a \<video\> tag.


