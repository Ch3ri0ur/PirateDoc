# H264 USB Camera

USB Cameras can have a [H264](Theory/Video/h264.md) Encoder integrated and provide a [H264](Theory/Video/h264.md).

Some Cameras will provide multiple Device Nodes, you can check what Formats they provide by using:

    v4l2-ctl --list-formats -d /dev/video0

## Victure Webcam SC30

In the Project we used the Victure Webcam SC30.

The Camera Provides 4 Device Nodes ``/dev/videoX`` but only 2 Provide Video.

 - /dev/video0: MPEG and YUYV
 - /dev/video2: H264


v4l2-ctl --list-formats -d /dev/video2

    ioctl: VIDIOC_ENUM_FMT
        Type: Video Capture

        [0]: 'H264' (H.264, compressed)

v4l2-ctl --all -d /dev/video2

    Driver Info:
            Driver name      : uvcvideo
            Card type        : USB  Camera: USB  Camera
            Bus info         : usb-0000:01:00.0-1.1
            Driver version   : 5.10.63
            Capabilities     : 0x84a00001
                    Video Capture
                    Metadata Capture
                    Streaming
                    Extended Pix Format
                    Device Capabilities
            Device Caps      : 0x04200001
                    Video Capture
                    Streaming
                    Extended Pix Format
    Media Driver Info:
            Driver name      : uvcvideo
            Model            : USB  Camera: USB  Camera
            Serial           : USB  Camera
            Bus info         : usb-0000:01:00.0-1.1
            Media version    : 5.10.63
            Hardware revision: 0x00000100 (256)
            Driver version   : 5.10.63
    Interface Info:
            ID               : 0x03000008
            Type             : V4L Video
    Entity Info:
            ID               : 0x00000007 (7)
            Name             : USB  Camera: USB  Camera
            Function         : V4L2 I/O
            Pad 0x01000011   : 0: Sink
            Link 0x0200001e: from remote pad 0x1000010 of entity 'Extension 4': Data, Enabled, Immutable
    Priority: 2
    Video input : 0 (Camera 1: ok)
    Format Video Capture:
            Width/Height      : 1920/1080
            Pixel Format      : 'H264' (H.264)
            Field             : None
            Bytes per Line    : 3840
            Size Image        : 0
            Colorspace        : sRGB
            Transfer Function : Rec. 709
            YCbCr/HSV Encoding: ITU-R 601
            Quantization      : Default (maps to Full Range)
            Flags             :
    Crop Capability Video Capture:
            Bounds      : Left 0, Top 0, Width 1920, Height 1080
            Default     : Left 0, Top 0, Width 1920, Height 1080
            Pixel Aspect: 1/1
    Selection Video Capture: crop_default, Left 0, Top 0, Width 1920, Height 1080, Flags:
    Selection Video Capture: crop_bounds, Left 0, Top 0, Width 1920, Height 1080, Flags:
    Streaming Parameters Video Capture:
            Capabilities     : timeperframe
            Frames per second: invalid (1/0)
            Read buffers     : 0
                        brightness 0x00980900 (int)    : min=-64 max=64 step=1 default=0 value=0
                        contrast 0x00980901 (int)    : min=0 max=64 step=1 default=32 value=32
                        saturation 0x00980902 (int)    : min=0 max=128 step=1 default=56 value=56
                                hue 0x00980903 (int)    : min=-40 max=40 step=1 default=0 value=0
    white_balance_temperature_auto 0x0098090c (bool)   : default=1 value=1
                            gamma 0x00980910 (int)    : min=72 max=500 step=1 default=100 value=100
                            gain 0x00980913 (int)    : min=0 max=100 step=1 default=0 value=0
            power_line_frequency 0x00980918 (menu)   : min=0 max=2 default=1 value=1
                                    0: Disabled
                                    1: 50 Hz
                                    2: 60 Hz
        white_balance_temperature 0x0098091a (int)    : min=2800 max=6500 step=1 default=4600 value=4600 flags=inactive
                        sharpness 0x0098091b (int)    : min=0 max=6 step=1 default=4 value=4
            backlight_compensation 0x0098091c (int)    : min=0 max=2 step=1 default=1 value=1
                    exposure_auto 0x009a0901 (menu)   : min=0 max=3 default=3 value=3
                                    1: Manual Mode
                                    3: Aperture Priority Mode
                exposure_absolute 0x009a0902 (int)    : min=1 max=5000 step=1 default=156 value=156 flags=inactive
            exposure_auto_priority 0x009a0903 (bool)   : default=0 value=0