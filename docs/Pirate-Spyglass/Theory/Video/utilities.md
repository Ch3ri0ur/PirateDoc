# Utilities for H264

Jus a small collection of useful tools that have been used in the research of the Project:

## SPS and PPS extracting h264 bit streamer

With the H264Bitstreamer Application from https://github.com/aizvorski/h264bitstream, the H264 input device node or files can be checked for H264. It produces and very detailed list of each bit of the SPS and PPS.

### fix error

https://github.com/aizvorski/h264bitstream/issues/25

### Result

https://www.cardinalpeak.com/blog/the-h-264-sequence-parameter-set


## ffprobe

FF Probe allows to analyse Files or input Devices and lets you see detailed information about the stream that is provided.

https://bitmovin.com/fun-with-container-formats-2/
https://stackoverflow.com/questions/8954609/how-to-get-h264-video-info

## mp4ff

A Go Lib that can created the [AVC File Format](mpeg4.md)

https://github.com/edgeware/mp4ff/blob/v0.26.1/examples/initcreator/main.go


## Module in JS

When including a JS in a HTML all function will be loaded in and if the function have the same name only the last loaded one will stay. To prevent this, it is good to capsule the Code as a Module or Class.

https://stackoverflow.com/questions/14765571/calling-a-function-with-same-name-in-another-js-file/14765929
