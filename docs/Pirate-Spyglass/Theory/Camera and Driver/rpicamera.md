# Raspberry Pi Camera Module

There are two Version of the Module V1 and V2.

The Camera gets connected by a ribbon cable and the driver on the Raspberry Pi is for

- RPi Buster or Older (RPI OS <=10) is it [rapivid](legacycameraStack.md) which is integrated in the GPU.
- RPi Bullseye (RPI OS 11) is it [libcamera](libcamera.md) an Opensource Linux oriented camera Stack that run on the CPU. It is only a few months old and in this Project not supported.

https://www.raspberrypi.com/documentation/accessories/camera.html#installing-a-raspberry-pi-camera
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2

The Camera on RPi-OS Buster (10) or earlier needs to activate the Camera in the config Menu ``sudo raspi-config``. It can be found under ``Interfacing Options`` or by changing a parameter directly in ``boot.config``. See in [rapivid](legacycameraStack.md) for more info.

The Camera Driver [libcamera](libcamera.md) on Bullseye can be deactivated and the old [rapivid](legacycameraStack.md) can be reactivated by using the config Menu ``sudo raspi-config``. It can be found under ``Interfacing Options`` or by changing some parameter directly in ``boot.config``. See in [libcamera](libcamera.md) for more info.

https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/3

## V4L2 adapter Driver bmc2835-v4l2

This Driver Implementation provides some extra API for the [v4l2](v4l2.md) to Control the RPI Camera.

Sometimes the special Driver for [v4l2](v4l2.md) Interface needs to be Installed and activated with:

    sudo modprobe bcm2835-v4l2

``v4l2-ctl --list-formats -d /dev/video0``

    ioctl: VIDIOC_ENUM_FMT
            Type: Video Capture

            [0]: 'YU12' (Planar YUV 4:2:0)
            [1]: 'YUYV' (YUYV 4:2:2)
            [2]: 'RGB3' (24-bit RGB 8-8-8)
            [3]: 'JPEG' (JFIF JPEG, compressed)
            [4]: 'H264' (H.264, compressed)
            [5]: 'MJPG' (Motion-JPEG, compressed)
            [6]: 'YVYU' (YVYU 4:2:2)
            [7]: 'VYUY' (VYUY 4:2:2)
            [8]: 'UYVY' (UYVY 4:2:2)
            [9]: 'NV12' (Y/CbCr 4:2:0)
            [10]: 'BGR3' (24-bit BGR 8-8-8)
            [11]: 'YV12' (Planar YVU 4:2:0)
            [12]: 'NV21' (Y/CrCb 4:2:0)
            [13]: 'RX24' (32-bit XBGR 8-8-8-8)

``v4l2-ctl --all -d /dev/video0``

    Driver Info:
            Driver name      : bm2835 mmal
            Card type        : mmal service 16.1
            Bus info         : platform:bcm2835-v4l2-0
            Driver version   : 5.10.63
            Capabilities     : 0x85200005
                    Video Capture
                    Video Overlay
                    Read/Write
                    Streaming
                    Extended Pix Format
                    Device Capabilities
            Device Caps      : 0x05200005
                    Video Capture
                    Video Overlay
                    Read/Write
                    Streaming
                    Extended Pix Format
    Priority: 2
    Video input : 0 (Camera 0: ok)
    Format Video Capture:
            Width/Height      : 1280/720
            Pixel Format      : 'H264' (H.264)
            Field             : None
            Bytes per Line    : 0
            Size Image        : 921600
            Colorspace        : SMPTE 170M
            Transfer Function : Default (maps to Rec. 709)
            YCbCr/HSV Encoding: Default (maps to ITU-R 601)
            Quantization      : Default (maps to Full Range)
            Flags             :
    Format Video Overlay:
            Left/Top    : 150/50
            Width/Height: 1024/768
            Field       : None
            Chroma Key  : 0x00000000
            Global Alpha: 0xff
            Clip Count  : 0
            Clip Bitmap : No
    Framebuffer Format:
            Capability    : Extern Overlay
                            Global Alpha
            Flags         : Overlay Matches Capture/Output Size
            Width         : 1280
            Height        : 720
            Pixel Format  : 'YU12'
    Streaming Parameters Video Capture:
            Capabilities     : timeperframe
            Frames per second: 30.000 (30000/1000)
            Read buffers     : 1

    User Controls

                        brightness 0x00980900 (int)    : min=0 max=100 step=1 default=50 value=50 flags=slider
                        contrast 0x00980901 (int)    : min=-100 max=100 step=1 default=0 value=0 flags=slider
                        saturation 0x00980902 (int)    : min=-100 max=100 step=1 default=0 value=0 flags=slider
                        red_balance 0x0098090e (int)    : min=1 max=7999 step=1 default=1000 value=1000 flags=slider
                    blue_balance 0x0098090f (int)    : min=1 max=7999 step=1 default=1000 value=1000 flags=slider
                    horizontal_flip 0x00980914 (bool)   : default=0 value=0
                    vertical_flip 0x00980915 (bool)   : default=0 value=0
            power_line_frequency 0x00980918 (menu)   : min=0 max=3 default=1 value=1
                                    0: Disabled
                                    1: 50 Hz
                                    2: 60 Hz
                                    3: Auto
                        sharpness 0x0098091b (int)    : min=-100 max=100 step=1 default=0 value=0 flags=slider
                    color_effects 0x0098091f (menu)   : min=0 max=15 default=0 value=0
                                    0: None
                                    1: Black & White
                                    2: Sepia
                                    3: Negative
                                    4: Emboss
                                    5: Sketch
                                    6: Sky Blue
                                    7: Grass Green
                                    8: Skin Whiten
                                    9: Vivid
                                    10: Aqua
                                    11: Art Freeze
                                    12: Silhouette
                                    13: Solarization
                                    14: Antique
                                    15: Set Cb/Cr
                            rotate 0x00980922 (int)    : min=0 max=360 step=90 default=0 value=0 flags=modify-layout
                color_effects_cbcr 0x0098092a (int)    : min=0 max=65535 step=1 default=32896 value=32896

    Codec Controls

                video_bitrate_mode 0x009909ce (menu)   : min=0 max=1 default=0 value=0 flags=update
                                    0: Variable Bitrate
                                    1: Constant Bitrate
                    video_bitrate 0x009909cf (int)    : min=25000 max=25000000 step=25000 default=10000000 value=1500000
            repeat_sequence_header 0x009909e2 (bool)   : default=0 value=0
                h264_i_frame_period 0x00990a66 (int)    : min=0 max=2147483647 step=1 default=60 value=60
                        h264_level 0x00990a67 (menu)   : min=0 max=13 default=11 value=11
                                    0: 1
                                    1: 1b
                                    2: 1.1
                                    3: 1.2
                                    4: 1.3
                                    5: 2
                                    6: 2.1
                                    7: 2.2
                                    8: 3
                                    9: 3.1
                                    10: 3.2
                                    11: 4
                                    12: 4.1
                                    13: 4.2
                    h264_profile 0x00990a6b (menu)   : min=0 max=4 default=4 value=4
                                    0: Baseline
                                    1: Constrained Baseline
                                    2: Main
                                    4: High

    Camera Controls

                    auto_exposure 0x009a0901 (menu)   : min=0 max=3 default=0 value=0
                                    0: Auto Mode
                                    1: Manual Mode
            exposure_time_absolute 0x009a0902 (int)    : min=1 max=10000 step=1 default=1000 value=1000
        exposure_dynamic_framerate 0x009a0903 (bool)   : default=0 value=0
                auto_exposure_bias 0x009a0913 (intmenu): min=0 max=24 default=12 value=12
                                    0: -4000 (0xfffffffffffff060)
                                    1: -3667 (0xfffffffffffff1ad)
                                    2: -3333 (0xfffffffffffff2fb)
                                    3: -3000 (0xfffffffffffff448)
                                    4: -2667 (0xfffffffffffff595)
                                    5: -2333 (0xfffffffffffff6e3)
                                    6: -2000 (0xfffffffffffff830)
                                    7: -1667 (0xfffffffffffff97d)
                                    8: -1333 (0xfffffffffffffacb)
                                    9: -1000 (0xfffffffffffffc18)
                                    10: -667 (0xfffffffffffffd65)
                                    11: -333 (0xfffffffffffffeb3)
                                    12: 0 (0x0)
                                    13: 333 (0x14d)
                                    14: 667 (0x29b)
                                    15: 1000 (0x3e8)
                                    16: 1333 (0x535)
                                    17: 1667 (0x683)
                                    18: 2000 (0x7d0)
                                    19: 2333 (0x91d)
                                    20: 2667 (0xa6b)
                                    21: 3000 (0xbb8)
                                    22: 3333 (0xd05)
                                    23: 3667 (0xe53)
                                    24: 4000 (0xfa0)
        white_balance_auto_preset 0x009a0914 (menu)   : min=0 max=10 default=1 value=1
                                    0: Manual
                                    1: Auto
                                    2: Incandescent
                                    3: Fluorescent
                                    4: Fluorescent H
                                    5: Horizon
                                    6: Daylight
                                    7: Flash
                                    8: Cloudy
                                    9: Shade
                                    10: Greyworld
                image_stabilization 0x009a0916 (bool)   : default=0 value=0
                    iso_sensitivity 0x009a0917 (intmenu): min=0 max=4 default=0 value=0
                                    0: 0 (0x0)
                                    1: 100000 (0x186a0)
                                    2: 200000 (0x30d40)
                                    3: 400000 (0x61a80)
                                    4: 800000 (0xc3500)
            iso_sensitivity_auto 0x009a0918 (menu)   : min=0 max=1 default=1 value=1
                                    0: Manual
                                    1: Auto
            exposure_metering_mode 0x009a0919 (menu)   : min=0 max=3 default=0 value=0
                                    0: Average
                                    1: Center Weighted
                                    2: Spot
                                    3: Matrix
                        scene_mode 0x009a091a (menu)   : min=0 max=13 default=0 value=0
                                    0: None
                                    8: Night
                                    11: Sports

    JPEG Compression Controls

                compression_quality 0x009d0903 (int)    : min=1 max=100 step=1 default=30 value=30
