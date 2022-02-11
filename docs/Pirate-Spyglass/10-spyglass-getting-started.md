# Getting Started

## Requirements

1. Rasbian 32bit
2. Legacy camerastack
## Fast Method

Download newest precompiled version from [repository](https://github.com/Ch3ri0ur/berrymse/releases).

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

## Run
Find executable in arm7l folder. For HTTP port 80 use sudo.

```
sudo ./berrymse
```

```
./berrymse -l <raspberry pi ip address>:<port> -d /dev/video<X>
```

Visit website under ```localhost```

## Register Service
To register the executable as an autostart service run

```
cd for_autostart
sudo ./register.sh
```
