# GOV4L2 Lib

This Go Lib for accessing v4l2 in Go is used in berryMSE. https://github.com/thinkski/go-v4l2

It is also created by Chris Hiszpanski and was only coded to provide basic function for the usage with the [RaspberryPi Camera](rpicamera.md).

!!! description

    A pure Go implementation of Video4Linux2 stream capture with a simple channel based interface:

    - No C code. No separate cross-compiler required.
    - Zero copy. Memory-mapped double-buffer scheme makes kernel memory reference available via Go channel.

For the Project we Improved it a little bit to fix some Bugs (Source didn't started correctly) and add some extra configuration functions.
The new Rotation function is already used in BerryMSE and works only for the RaspberryPi.
The new CustomConfig Functions are not used yet, but would allow in further work that custom settings can be applied to different Cameras without adding any new code to the Lib.

## CustomControls

The new implemented Custom Control function allows the setting of camera v4l2 controls via ID.

    // Custom Configuration possible with
	dev.SetCustomUserControl(id uint32, value int32)
	dev.SetCustomCodecControl(id uint32, value int32)
	// Check device with "v4l2-ctl --all -d /dev/videoX" for IDs
	// User stuff = 0x00980000 - 0x0098ffff
	// Codec stuff = 0x00990000 - 0x0099ffff
	// e.g. user control vertical flip = 0x00980915

The Control IDs can be extracted by using the ``4vl2-ctl -all -d /dev/videoX`` command.

e.g. RPI Camera

    ...
    User Controls

                        brightness 0x00980900 (int)    : min=0 max=100 step=1 default=50 value=50 flags=slider
                        contrast 0x00980901 (int)    : min=-100 max=100 step=1 default=0 value=0 flags=slider
                        saturation 0x00980902 (int)    : min=-100 max=100 step=1 default=0 value=0 flags=slider
                        red_balance 0x0098090e (int)    : min=1 max=7999 step=1 default=1000 value=1000 flags=slider
                    blue_balance 0x0098090f (int)    : min=1 max=7999 step=1 default=1000 value=1000 flags=slider
                    horizontal_flip 0x00980914 (bool)   : default=0 value=0
                    vertical_flip 0x00980915 (bool)   : default=0 value=0
            power_line_frequency 0x00980918 (menu)   : min=0 max=3 default=1 value=1
    ...