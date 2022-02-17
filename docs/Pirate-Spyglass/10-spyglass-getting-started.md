# Getting Started

This section contains instructions to create a streaming Raspberry Pi.

It contains:

- The Requirements
- How to start the server
- How to enable autostart
- How to include into clients

## Requirements

This solution was tested on a Raspberry Pi 4 with the 32-bit Raspberry Pi OS Debian 10 (Buster) and 11 (Bullseye).

Camera wise a [Raspberry Pi Camera Module](Theory/Camera%20and%20Driver/rpicamera.md) is necessary or a [USB Webcam with integrated H264 encoder](Theory/Camera%20and%20Driver/h264camera.md). It was tested with V1 and V2 of the RPI Camera and Victure SC30 USB Webcam. USB Webcams don't have many supported settings and the Bitrate is trash.

### Raspberry Pi Camera

The Camera driver needs to be activated. This can be done in the Raspberry Pi Config in the interface section.

    sudo raspi-config

### USB H264 Camera

The [Camera](Theory/Camera%20and%20Driver/h264camera.md) needs to have a Device Node ``/dev/video*`` that provides Video with the [H264](Theory/Video/h264.md) Codec.

Some Cameras will provide multiple Device Nodes, you can check what Formats they provide by using:

    v4l2-ctl --list-formats -d /dev/video0

## Fast Method

* Connect the camera with the included ribbon cable.

* Install the OS (Raspberry Pi OS (Legacy) with desktop) and 

* then activate the camera interface (`raspi-config`). (for additional information see[[setupraspberrypi]]) (Optional on Bullseye, activate legacy stack [[libcamera]])

* Download newest precompiled version from [repository](https://github.com/Ch3ri0ur/berrymse/releases).

Unzip with and move into folder with

``` bash
tar xf berrymse.tar.gz
cd berrymse
```

The folder should contain:

* berrymse, the executable
* config.yml a config file
* for_autorstart a folder with convenience scripts
* readme.md 

Make executable exectuable:

```chomd +x ./berrymse```

and run it.

## Run

```
sudo ./berrymse
```
This runs a server that provides a demo website. Without a config file port 2020 is standard. To open it visit `localhost:2020`.

The server provides a webpage (`index.html`), a websocket stream of the camera (`/video_websocket`) and the javascript (`/msevideo.js`) to run it. For more information on how to integrate this into another project please see the chapter below.

For HTTP port 80 use sudo and specify port (0.0.0.0:80). 

``` bash
sudo ./berrymse -l <raspberry pi ip address>:<port> -d /dev/video<X>
```
or configure the executable by placing a `config.yml`  with the following content in the same folder as the executable. The possible parameters can be seen under `berrymse -h`.

!!! info inline end
    If these configurations don't work/match your camera this can freeze the camera stack. e.g. using resolutions above 1920 times 1080 created crashes.

``` yaml title="config.yml"
camera:
  sourceFD: "/dev/video0"
  width: 1280
  height: 720
  bitrate: 1500000

server:
  url: "0.0.0.0:80"
```

Run with sudo and visit website under ```localhost```.


## Register Service
To register the executable as an autostart service:

- download the repository or release folder
- compile or place the executable in the armv7l folder (path must match the path in the `berrymse.service` file)
Then use the provided convenience scripts in the for_autostart folder. 

```
cd for_autostart
chmod +x ./register.sh
sudo ./register.sh
```

Restart to test the service.

## Compile Manually

Install [Golang](https://go.dev/dl/) (use either armv6l for 32-bit or arm64)

```
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.17.7.linux-armv7l.tar.gz
```

Add PATH and GOPATH
```
export PATH=$PATH:/usr/local/go/bin
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
```


Clone the [repository](https://github.com/Ch3ri0ur/berrymse)

Install pkger and dependencies:
```
GOOS=linux go get -v ./...
go install github.com/markbates/pkger/cmd/pkger
```

Build:
```
make
```
Find executable in the arm7l folder.

Execute from folder with config.yml

```
sudo ./armv7l/berrymse
```

## How to integrate into another Project

Add the following snippets to the html file.
Add the script to the header.
``` html
<script src="msevideo.js"></script>
```

Add the video element and Buttons inside the body.
```html
<video autoplay controls muted></video>
<button id="play-button" type="button">Pause</button>
<button id="auto-skip-button" type="button">Auto Skip Enabled</button>
<button id="reset-button" type="button">Reset</button>
``` 

The `msevideo.js` expects the websocket connection under `/video_websocket` at the same origin as the website. This is done because it is expected that a reverse proxy is used for this application.

The `autoplay controls muted` classes are advised.
