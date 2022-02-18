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
More Infos to NAL Units can be found here [H.264](Theory/Video/h264.md).

## H.264 NAL Unit Stream to WS Stream

The NAL Units of [H.264](Theory/Video/h264.md) get inspected in BerryMSE for their type.

- If it is [P-Frame or I-Frame Data](Theory/Video/h264.md) than it will gets packed in a [MPEG-4 Part 15](Theory/Video/mpeg4.md) [AVC File Format](Theory/Video/avcff.md) and prepared for the transport via Websocket to the clients. Important is that a client will only start receiving Data when SPS, PPS are known to extract the Codec infos. Also the first frame needs to be an I-Frame that initializes the sequence.
- If it is a [SPS or PPS](Theory/Video/h264.md) NAL Unit than the [SPS or PPS](Theory/Video/h264.md) will get stored. It is needed as a Parameter for the [AVC File Format](Theory/Video/avcff.md).
- Every other NAL Unit type gets ignored.

When a Client gets connected it will receive a [Initial Fragment package](Theory/Video/avcff.md) of "FTYP" and "MOOV" that contain the Information about the stream. Frames will get send [Movie Fragments](Theory/Video/avcff.md) that are a combination of a "MOOF" and "MDAT" package. The frame index gets count up for each client independently.
Mor Infos to the Packages can be found here [AVC File Format](Theory/Video/avcff.md) and here [MPEG-4 Part 15](Theory/Video/mpeg4.md)

The Packages get send over Websocket.

## WS Stream to Video

On the Clients Side the video will be displayed on a Webpage in a video tag. To do this the packages of the websocket need to be passed to the [Media Source Extention](Theory/Video/mse.md) that can read and decode [H.264 Videos](Theory/Video/h264.md) that are send as [MPEG-4 Part 15](Theory/Video/mpeg4.md) [AVC File Format](Theory/Video/avcff.md). This all happens in a separate JavaScript.

The JavaScript not only creates and supplies the [MSE](Theory/Video/mse.md) with the packages from the websocket, it also extracts the codec information from the stream first to create the [MSE Object and SourceBuffer](Theory/Video/mse.md). The Script also controls the video element so that it jumps to the newest decoded segment and don't spend time to prebuffering the data first.

The Website (.html) and Javascript are served by a HTTP Fileserver under der selected URL address.


## Configuration

The currently implemented configurations are:

-  H264 bitrate:
    Changes the bitrate of the video and the encoder will now try to only produce a [H264 Stream](Theory/Video/h264.md).
- Video height resolution:
    Changes the video height resolution.
- Video width resolution:
    Changes the video width resolution.
- Video rotation:
    Changes the video rotation resolution. It can only be changed in 90 degree steps and rotates the picture clockwise.
- Video source:
    Changes the source Device Node of the video.
- Server URL address:
    Changes the URL address were the video and website gets published to.
- Server websocket name:
    Changes the websocket name were the video packages can get received. This will break the demo page!

!!! Warning

    Only the [RPi Camera](Theory/Camera%20and%20Driver/rpicamera.md) currently supports the Settings

    - Rotation
    - Bitrate

    [H264 USB Cameras](Theory/Camera%20and%20Driver/h264camera.md) need to use ``-1`` to skip them.


### Flags

Flags have the highest Priority and will overwrite any default Value and also Overwrite the Config loaded from the Config File.

The Flags are fisted below:

    Usage of ./berrymse:
        -c, -- string                   Use config Path/Name.yml
                                        Default Path is current directory! (default "config.yml")
        -b, --Camera.Bitrate int        Bitrate in bit/s!
                                        Only supported for RPI Camera
                                        Other Cameras need to use -1 (default 1500000)
        -h, --Camera.Height int         Height Resolution (default 720)
        -r, --Camera.Rotation int       Rotation in 90degree Step
                                        Only supported for RPI Camera
                                        Other Cameras need to use -1
        -d, --Camera.SourceFD string    Use camera /dev/videoX (default "/dev/video0")
        -w, --Camera.Width int          Width Resolution (default 1280)
        -l, --Server.URL string         listen on host:port (default "localhost:2020")
        -s, --Server.WebSocket string   Name of Websocket for Video Stream (default "video_websocket")

### Config File

    The Config File, if available, gets loaded in the beginning. Default Name is "config.yml" and it is structured as seen below.

    ``` yaml title="config.yml"
    camera:
    sourceFD: "/dev/video0"
    width: 1280
    height: 720
    bitrate: 1500000
    rotation: 0

    server:
    url: "0.0.0.0:80"
    ```