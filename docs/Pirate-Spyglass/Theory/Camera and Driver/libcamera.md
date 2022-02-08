# libcamera 
New open source camera driver for RPI 11+ (Bullseye or later). Libcamera is a Linux focused driver that allows the usage of more complex cameras and runs on the (ARM) processors.
[0](https://www.raspberrypi.com/documentation/accessories/camera.html)

/dev/video0 and /dev/video1 are V4L2 drivers for Unicam / CSI-2 receiver

Camera Serial Interface 2 (CSI2) "Unicam"

## Usage


## Difference to old Driver (Legacy Camera Stack)


## Problems

The API changed a bit, so that currently the rpi camera cannot be used on the new RPI OS Version Bullseye. Also old Applications got problems and cant run on the rpi when using rpi camera
[1](https://raspberrypi.stackexchange.com/questions/135364/libcamera-stack-does-not-work-with-bullseye)

[2](https://forums.raspberrypi.com/viewtopic.php?p=1958297)

## Back to Legacy Camera Stack

A Quickfix is to use the old legacy Camera Stack. This can be achieved by changing some lines in the ``boot/config.txt``.

