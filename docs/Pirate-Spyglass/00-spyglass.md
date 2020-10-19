# Overview


!!! note "Warning!"
    The Spyglass Implementation will change in MEM Project 2 and the detailed Documentation will follow.

## Requirements

The Goals for the Camera Implementation have been:

- Low Ressourcen Usage on Host and User side
- Low Latency
- Low Bandwidth
- Works on Raspberry Pi

## Theory

In the Theory, Streamer, Sources and in [Streaming method's](streamingmethods.md) the research Material can be found

## Implementation

The Implementation uses a [Janus WebRTC Broadcaster](Streamers/janus.md) and its documentation and results are currently a bit mixed up.

## Validation

Currently the Implementation runs with:
    - Bandwidth: 1.2 Mbit/s 
    - Latency: < 300ms 
    - Resolution: 960x540
    - Problems with HS Network

Tests to other Resoulutions and the Setup can be found in [Janus WebRTC Broadcaster](Streamers/janus.md).