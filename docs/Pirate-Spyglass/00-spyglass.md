# Overview

In order to directly monitor the setup and to make the measurements more engaging, a webcam solution was found.

This solution uses the existing Raspberry Pi and a Raspberry Pi camera to capture video and provides a endpoint to stream this data to a webpage.

[Getting Started](10-spyglass-getting-started.md){: .md-button .md-button--primary }

## Requirements

The Goals for the Camera Implementation have been:

- Low Ressourcen Usage on Host and User side
- Low Latency
- Low Bandwidth
- Works on Raspberry Pi

[Requirements](20-spyglass-requirements.md){: .md-button}



## Implementation

This video implementation is based on the project [berrymse](https://github.com/thinkski/berrymse) from Chris Hiszpanski. 

!!! note "Description from the berrymse project"

        H.264 Network Abstraction Layer (NAL) units are read from `/dev/video0`, a
        Video4Linux2 compatible camera interface. Each unit corresponds to one frame.
        Frames are packaged into MPEG-4 ISO BMFF (ISO/IEC 14496-12) compliant
        fragments and sent via a websocket to the browser client. The client appends
        each received buffer to the media source for playback.

This camera stack has three major components, the hardware/driver stack, the server and the client.

### Hardware

Matching the used Raspberry Pi, a Raspberry Pi camera module is used to capture image data. This data is provided in a [v4l2] format 
- A Raspberry Pi camera module provides the driver with raw image data.
- The v4l2 video driver (Legacy Raspberry Pi Buster Stack)
  - hardware accelerated encoding
  - generates mp4 part 10 NAL units

### Server
- A server to
  -  wrap the encoded h264 fragments into 
  - Provide websocket endpoints to send the fragments

### Client
- Client side the MSE is used to enable playback in a \<video\> tag.




H.264 Network Abstraction Layer (NAL) units are read from `/dev/video0`, a
Video4Linux2 compatible camera interface. Each unit corresponds to one frame.
Frames are packaged into MPEG-4 ISO BMFF (ISO/IEC 14496-12) compliant
fragments and sent via a websocket to the browser client. The client appends
each received buffer to the media source for playback.


[Further details on Implementation](30-spyglass-implementation.md){: .md-button}
## Validation

Currently the Implementation runs with:
    - Bandwidth: 1.5 Mbit/s 
    - Latency: < 300ms 
    - Resolution: 960x540
    - Problems with HS Network
    - USB Video Class devices are not supported

Tests to other Resolutions and the Setup can be found in [Janus WebRTC Broadcaster](../Streamers/janus.md).

[Validation](40-spyglass-validation.md){: .md-button}


## Research

In the Theory tab,

### Video Streaming

In the Theory, Streamer, Sources and in [Streaming method's](../streamingmethods.md) the research Material can be found

### Licensing

## Legacy Solution