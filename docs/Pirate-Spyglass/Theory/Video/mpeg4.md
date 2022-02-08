# MPEG-4 (ISO/IEC-14496)

MPEG-4 is a Standard for Coding of audio-visual objects from MPEG (The Moving Picture Experts Group).

Important for the project berryMSE are only a view Parts from this standard needed. The most important and used one can be found in this Section.


## MPEG-4 Part 10 Advanced Video Coding (AVC) H.264 ISO/IEC 14496-10

Part 10 of MPEG-4 defines the H.264 Compression. The RPI Camera outputs data in this format in the Device Node e.g. ``/dev/video0`` channel, if Pixelformat "H264" in V4L2 driver is selected. The BerryMSE code configures the Device Node in that way that two NAL Units can be stored and retrieved.

BerryMSE uses the given H264 directly. After adding MPEG-4 Part 12 and Part 15 extensions, it sends it to the Client. The Client uses the Media Source Extensions (MSE) to display the video. The MSE can decode the H264 Video on its own, this is why Encoding and Decoding isn't needed in this Project.

More to MPEG-4 Part 10 can be found here in [H.264](h264.md).


## MPEG-4 Part 12 ISO Base Media File Format (ISOBMFF) ISO/IEC 14496-12

MPEG-4 Part 12 defines the structure for time-based files for video and audio.
The file-structure is object oriented, mean all Data is contained in blocks called boxes. Sometimes they get called Containers or Atoms. Every Box is identified by a 4 byte/char Type indicator (e.g. "ftyp") followed by its size/length in bytes (int32). The Content of the Box is depending on its type and can also be other boxes.

The file-structure supports Streaming of Media Data by allowing the splitting of media data files.

https://en.wikipedia.org/wiki/ISO/IEC_base_media_file_format
https://mpeg.chiariglione.org/standards/mpeg-4/iso-base-media-file-format

## MPEG-4 Part 14 MP4 File Format ISO/IEC 14496-14

MPEG-4 Part 14 set the standard for MP4 Files. It stores the video and audio in a File as MP4 based on the ISOBMFF File Structure (MPEG-4 Part 12).

The Video can be a H264 (MPEG Part 10), H265 (MPEG-H Part 2) or an older MPEG Compression Format.

https://mpeg.chiariglione.org/standards/mpeg-4/mp4-file-format
https://en.wikipedia.org/wiki/MPEG-4_Part_14

## MPEG-4 Part 15 Advanced Video Coding (AVC) file format ISO/IEC 14496-15

MPEG-4 Part 15 defines the storage and transport of AVC/H264 (MPEG-4 Part 10) Streams in ISOBMFF File Format (MPEG-4 Part 12) and is similar to MP4 (MPEG-4 Part 14).
Every Frame/NAL Unit is stored in its own independent ISOBMFF sample. The Initial sample holds some separate Settings and Parameters for the streaming and can be highly configured to adjust bitrate and others.

The Media Source Extension (MSE) of Browsers can handle a Streams based on MPEG-4 Part 15. Each NAL Unit can be send separate and gets combined in the SourceBuffer of MSE. This would allow to send the H.264 from a Camera directly to the User, which means the host would no longer need to decode and encode the video stream.

https://mpeg.chiariglione.org/standards/mpeg-4/carriage-nal-unit-structured-video-iso-base-media-file-format

The project [BerryMSE](https://github.com/thinkski/berrymse) and [pi_streaming](https://www.codeinsideout.com/blog/pi/stream-picamera-h264/) use this Methode of sending each NAL Unit separate as a Websocket Msg to the User. BerryMSE uses the MSE and pi_streaming uses a Javascript to decode video.
