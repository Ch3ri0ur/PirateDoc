# Implementation

The [BerryMSE project](https://github.com/Ch3ri0ur/berrymse) is so designed that it produces an one file executable, which runs on the RaspberryPi and streams the [RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md) via Websocket. A demo website is contained in the executable and is reachable on the given address, but its also possible to integrate the video in other websites via a small JavaScript script. The integration and playback in the website happens via [MSE](Theory/Video/mse.md), which almost every browser supports.

The implementation is focused on using as little components as possible and be very lightweight in performance and network traffic. This is achieved by avoiding unnecessary re-encoding and using hardware accelerated encoding and decoding on the server and the client.

The [H.264](Theory/Video/h264.md) compression of the [RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md) stack helps limit the network traffic. For compatibility with browsers the frames (the [H.264 NAL Units](Theory/Video/h264.md)) are wrapped according the [ISOBMFF](Theory/Video/mpeg4.md) specification. These packages can be fed into the video player in the browser and are decoded by the [MSE](Theory/Video/mse.md) in real-time. The transport is performed via Websocket, because it doesn't need extra fallback server infrastructure, like a STUN/TURN server for [WebRTC](Research/webRTC.md).

The server is written in the programming language Golang. The Website is written with HTML, CSS and vanilla JavaScript.

Only the [RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md) is currently fully supported. The width, height, bandwidth ,rotation and source device can be configured. For more information see [H.264 Parameter](Theory/Video/h264.md). Rudimentary webcam support has been implemented. These webcams need to support [H.264](Theory/Video/h264.md) streaming, see [H264 Cameras](Theory/Camera%20and%20Driver/h264camera.md). The problem is that compared to the [RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md) these webcams can not be configured as well and generate very high bandwidth.

## Brief Process Overview

1. Camera ([RPiCam](Theory/Camera%20and%20Driver/rpicamera.md), [H264 Camera](Theory/Camera%20and%20Driver/h264camera.md))
    - Produces raw image data ([H264 Camera](Theory/Camera%20and%20Driver/h264camera.md) has an integrated [H.264](Theory/Video/h264.md) encoder and uses its own driver. It skips step 2 and interacts with the [V4L2 Driver](Theory/Camera%20and%20Driver/v4l2.md) directly).
2. Camera driver ([libcamera](Theory/Camera%20and%20Driver/libcamera.md), [raspicam](Theory/Camera%20and%20Driver/legacycameraStack.md))
    - Converts image data from camera to selected data format, here [H.264 NAL Units](Theory/Video/h264.md).
3. [V4L2 Driver](Theory/Camera%20and%20Driver/v4l2.md)
    - Stores image data in buffer and provides device interface on the device node, ``/dev/video0``.
4. BerryMSE
    1. Source [goV4l2](Theory/Camera%20and%20Driver/goV4l2.md)
            - Retrieves [NAL Units](Theory/Video/h264.md) from device node and adds them to the hub buffer.
    2. Hub
            - Creates [AVCFF MPEG-4 Part 15](Theory/Video/mpeg4.md) conform packages by storing [NAL Units](Theory/Video/h264.md) into [ISOBMFF](Theory/Video/mpeg4.md) Structure.
    3. Websocket
            - Created [AVCFF](Theory/Video/avcff.md) conform packages (frames) get send to registered websocket clients.
5. JavaScript client
    1. Websocket
        - Received [AVCFF](Theory/Video/avcff.md) packages get appended to the [MSE SourceBuffer](Theory/Video/mse.md).
    2. MSE
        - Creates video by decoding the [H.264](Theory/Video/h264.md) packages and feeding the the resulting frames to the video element.
6. HTML Video Element
    - Displays video on website.

## Camera to H.264 NAL Unit Stream

[RaspberryPi Camera](Theory/Camera%20and%20Driver/rpicamera.md) or other [H264 Camera](Theory/Camera%20and%20Driver/h264camera.md) capture the image with a image sensor. This captured image gets converted into a [H.264 Stream](Theory/Video/h264.md) by the [raspicam Driver](Theory/Camera%20and%20Driver/legacycameraStack.md) or the integrated encoder by [H264 Camera](Theory/Camera%20and%20Driver/h264camera.md). The camera driver than gets accessed by the [V4L2 Driver](Theory/Camera%20and%20Driver/v4l2.md) that handles the user space buffer side and provides the device nodes ``e.g. /dev/video0`` to access the camera stream and provides a unicam config interface.

This all happens outside the BerryMSE application on the RaspberryPi. BerryMSE starts with the usage of [go-v4l2 lib](Theory/Camera%20and%20Driver/goV4l2.md) that provides a data channel (Golang channel) and a configuration interface for the camera in Golang. The [go-v4l2 lib](Theory/Camera%20and%20Driver/goV4l2.md) opens the stream of the camera (as a [H.264 Stream](Theory/Video/h264.md)) and configures the [V4L2](Theory/Camera%20and%20Driver/v4l2.md) user space buffer.
It reads the buffer and puts the data in the channel. The data in this case are NAL Units from the [H.264 Stream](Theory/Video/h264.md) of the camera. During testing we found that occasionally the library would crash, presumably because the source was not yet ready. In order to prevent these crashes, fault tolerance has been implemented to ensure reliable start on boot.

## H.264 NAL Unit Stream to WS Stream

The NAL Units of [H.264](Theory/Video/h264.md) get inspected in BerryMSE for the type of NAL Units.

- If it is a [SPS or PPS](Theory/Video/h264.md) NAL Unit than the [SPS or PPS](Theory/Video/h264.md) will get stored. It is needed as a Parameter for the [AVC File Format](Theory/Video/avcff.md).
- If it is frame data then it gets packed in [MPEG-4 Part 15](Theory/Video/mpeg4.md) [AVC File Format](Theory/Video/avcff.md) and prepared for the transport via Websocket to the clients. Important is that a client will only recieve
- Every other NAL Unit gets ignored.

When a Client gets connected it will Receive

## WS Stream to Video

[MPEG-4](Theory/Video/mpeg4.md)
[MSE](Theory/Video/mse.md)


## Website
    Gets Http Served Website
    Client side the MSE is used to enable playback in a \<video\> tag.


