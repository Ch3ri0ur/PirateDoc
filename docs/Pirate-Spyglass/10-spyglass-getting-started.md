# Getting Started

This section contains instructions to create a streaming Raspberry Pi.

It contains:
- The Requirements
- How to start the server
- How to enable autostart
- How to include into clients

## Requirements
This solution was tested on a Raspberry Pi 4 with the legacy Debian 10 (Buster) based 32-bit Raspberry Pi OS.
(Bullseye works if legacy camera stack is activated)
Hardware wise a Raspberry Pi camera module is necessary. It was tested with v1 and v2 versions of the module.

## Fast Method
Connect the camera with the included ribbon cable. 

Install the OS and then activate the camera interface (`raspi-config`). (Optional on Bullseye, activate legacy stack [[libcamera]])

Download newest precompiled version from [repository](https://github.com/Ch3ri0ur/berrymse/releases).

Unzip with and move into folder with

``` bash
tar xf berrymse.tar.gz
cd berrymse_release
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
./berrymse
```
This runs a server that provides a demo website. Port 2020 is standard. To open it visit `localhost:2020`.

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
sudo ./register.sh
```

## Compile Manually

Install [Golang](https://go.dev/dl/)
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
