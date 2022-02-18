# Implementation

The [BerryMSE project](https://github.com/Ch3ri0ur/berrymse) is so designed that it produces an one file executable, which runs on the RaspberryPi and streams the [RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md) via Websocket. A Demo Website is contained in the executable and is reachable on the given address, but its also possible to integrate the video in other websites via a small JavaScript. The Integration and Display in the Website happens via [MSE](Theory/Video/mse.md) Extension, which almost every Browser has already implemented.

The Implementation is focused on using as less components as possible and be very lightweight in performance and Network traffic. This is achieved by not doing any Decoding and Encoding on the RaspberryPi and using the [H.264](Theory/Video/h264.md) Compression of the [RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md). By using the very optimized [MSE](Theory/Video/mse.md) of the Browser to decode the Video only a Transport of the [H.264 NAL Units](Theory/Video/h264.md) is needed. This is performed via Websocket, which is also very easy to setup and doesn't needs extra server infrastructure, like a STUN/TURN Server for [WebRTC](Research/webRTC.md).

Almost the complete Project is written in the Programming Language Golang. Only for the Website is HTML and JavaScript code necessary.

Only the [RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md) is currently supported and also only works with the default settings for Width, Height and Bitrate. The Reason for this is, that the [H.264 Parameter](Theory/Video/h264.md) are currently Hardcoded. Further Goal is to support this Settings and also make it possible to use other [H264 Cameras](Theory/Camera%20and%20Driver/h264camera.md) that support [H.264](Theory/Video/h264.md).

## Brief Process Overview

1. Camera ([RPiCam](Theory/Camera%20and%20Driver/rpicamera.md), [H264 Camera](Theory/Camera%20and%20Driver/h264camera.md))
    - Produces RawImage Data ([H264 Camera](Theory/Camera%20and%20Driver/h264camera.md) has an Integrated [H.264](Theory/Video/h264.md) Encoder and uses its own driver. It skips Step 2 and interacts with the [V4L2 Driver](Theory/Camera%20and%20Driver/v4l2.md) directly).
2. Camera Driver ([libcamera](Theory/Camera%20and%20Driver/libcamera.md), [raspicam](Theory/Camera%20and%20Driver/legacycameraStack.md))
    - Converts Imagedata from Camera to selected data format, [H.264 NAL Units](Theory/Video/h264.md).
3. [V4L2 Driver](Theory/Camera%20and%20Driver/v4l2.md)
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

## Camera to H.264 NAL Unit Stream

[RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md) or other [H264 Camera](Theory/Camera%20and%20Driver/h264camera.md) capture the Image with a Image Sensor. This captured Image gets converted into a [H.264 Stream](Theory/Video/h264.md) by the [raspicam Driver](Theory/Camera%20and%20Driver/legacycameraStack.md) or the integrated Encoder by [H264 Camera](Theory/Camera%20and%20Driver/h264camera.md). The Camera Driver than gets accessed by the [V4L2 Driver](Theory/Camera%20and%20Driver/v4l2.md) that handles the User Space Buffer side and provides the Device Nodes ``e.g. /dev/video0`` to access the Camera Stream and give a Unicam config interface.

This all happened outside the BerryMSE on the RaspberryPi. BerryMSE starts with the usage of [go-v4l2 lib](Theory/Camera%20and%20Driver/goV4l2.md) that provides an data channel (Golang Channel) and a configuration Interface for the camera in Golang. The [go-v4l2 lib](Theory/Camera%20and%20Driver/goV4l2.md) opens the stream of the camera (as [H.264 Stream](Theory/Video/h264.md)) and configures the [V4L2](Theory/Camera%20and%20Driver/v4l2.md) User Space Buffer.
It reads the Buffer and puts the data in the channel. The data in this case are NAL Units from the [H.264 Stream](Theory/Video/h264.md) of the camera. A little improvement has been implemented by us to prevent the crashes of the Source when starting up (Source wasn't ready, only happened rarely).

## H.264 NAL Unit Stream to WS Stream

The NAL Units of [H.264](Theory/Video/h264.md) get inspected in BerryMSE for the type of NAL Units.

- If it is Frame Data than it will gets packed in a [MPEG-4 Part 15](Theory/Video/mpeg4.md) [AVC File Format](Theory/Video/avcff.md) and prepared for the transport via Websocket to the clients. Important is that a client will only recieve
- If it is a [SPS or PPS](Theory/Video/h264.md) NAL Unit than the [SPS or PPS](Theory/Video/h264.md) will get stored. It is needed as a Parameter for the [AVC File Format](Theory/Video/avcff.md).
- Every other NAL Unit gets ignored.

When a Client gets connected it will Receive

## WS Stream to Video

[MPEG-4](Theory/Video/mpeg4.md)
[MSE](Theory/Video/mse.md)


## Website
    Gets Http Served Website
    Client side the MSE is used to enable playback in a \<video\> tag.


