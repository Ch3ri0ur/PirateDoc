# Getting Started

This section contains instructions to create a streaming Raspberry Pi.

It contains:
- The Requirements
- The Server
- The Client
- Possible architecture
- Access over the Internet

## Requirements
This solution was tested on a Raspberry Pi 4 with the legacy Debian 10 (Buster) based 32-bit Raspberry Pi OS.
(Bullseye works if legacy camera stack is activated)
Hardware wise a Raspberry Pi camera module is necessary. It was tested with v1 and v2 versions of the module.

## Fast Method

Download newest precompiled version from [repository](https://github.com/Ch3ri0ur/berrymse/releases).

Make executable:

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
or configure the executable by placing a `config.yml`  with the following content in the same folder as the executable.

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

In order to 

## Register Service
To register the executable as an autostart service:

download the repository, compile or place the executable in the armv7l folder. 
Then 

```
cd for_autostart
sudo ./register.sh
```

## Compile Manually

Install [Golang](https://go.dev/dl/)
Clone repository https://github.com/Ch3ri0ur/berrymse

Install pkger and dependencies:
```
GOOS=linux go get -v ./...
go install github.com/markbates/pkger/cmd/pkger
```

Build:
```
GOOS=linux go get -v ./...
go install github.com/markbates/pkger/cmd/pkger
```
Find executable in arm7l folder.

## How to integrate into another Project

