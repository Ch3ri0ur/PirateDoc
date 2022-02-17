# libcamera

New open source camera driver that is used for RPI 11+ (Bullseye or later). Libcamera is a Linux focused driver that allows the usage of more complex cameras (not only [RPi Camera](rpicamera.md)) and runs on the (ARM) processors.

https://www.raspberrypi.com/documentation/accessories/camera.html

The Libcamera will provided /dev/video0 and /dev/video1 as Device Nodes for the [RPi Camera](rpicamera.md). These are Camera Serial Interface 2 (CSI2) "Unicam" that are provide and managed in combination with the V4L2 driver.

## Usage

Pictures

    libcamera-still

Videos

    libcamera-vid

https://www.raspberrypi.com/documentation/accessories/camera.html

## Problems

The API changed a bit, so that currently the rpi camera cannot be used on the new RPI OS Version Bullseye. Also old Applications got problems and cant run on the rpi.

https://raspberrypi.stackexchange.com/questions/135364/libcamera-stack-does-not-work-with-bullseye

https://forums.raspberrypi.com/viewtopic.php?p=1958297

## Back to [Legacy Camera Stack](legacycameraStack.md)

The Old Driver can be reactivated in the RaspberryPi Config:

1. ```
    sudo raspi-config
    ```

2. Interface Options and select Legacy camera 

3. reboot

https://www.raspberrypi.com/documentation/accessories/camera.html#re-enabling-the-legacy-stack

or by changing in the ``/boot/config.txt`` a view Parameters. Remove camera_auto_detect and add the two lines. Than Reboot.

!!! File

    /boot/config.txt
    ```
    ...
    # Automatically load overlays for detected cameras
    #camera_auto_detect=1
    start_x=1
    gpu_mem=128
    ...
    ```

https://forums.raspberrypi.com/viewtopic.php?t=323390

