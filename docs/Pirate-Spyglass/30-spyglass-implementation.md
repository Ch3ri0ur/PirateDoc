# Implementation



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
