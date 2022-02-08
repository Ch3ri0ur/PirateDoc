# Media Source Extension (MSE) aka Media Source API

Is an API/Extension many Browser already have integrated and Support. This means now Plugins or extra Software is needed to use it. Only Safari on iOS seem to still not support it completely, see https://caniuse.com/mediasource.

MSE allows websites to run more advanced Video and Audio application, without any extra Software. By using a MediasSource Object to replaces the single Video/Audio track in the ''src'' of Video and Audio Element. This adds new methods to manipulate and control the video.

https://developer.mozilla.org/en-US/docs/Web/API/Media_Source_Extensions_API

## MediaSource Object

The MediaSource object from MSE can be used as ''src'' for Audio and Video. The MediaSource Object controls the Video and Audio, this allows the usage of more complex Video and Audio formats like MP4 Container or H.264 Video Codec. The Website now can use H.264 and doesn't need a Plugin or extra Code to encode the Video.

The MediaSource Object needs a SourceBuffer that stores/buffers the Video/Audio data. When creating the SourceBuffer by ``mediaSourceObject.addSourceBuffer(mimeCodec)`` a ``mimeCodec`` is needed.

https://developer.mozilla.org/en-US/docs/Web/API/MediaSource

## SourceBuffer

The SourceBuffer holds and controls the stored/buffered Audio/Video. When adding a SourceBuffer to the MediaSource a ``mimeCodec`` information is needed so the Buffer knows what type of codec got used.

The SourceBuffer has an append function that allows the appending of new sections of a video. This allows the usage of a Stream based on [MPEG-4 Part 15](mpeg4.md) to be stored and displayed.

The default video Element with the MediaSource will always Buffer a small section before displaying the stream, this would cause some latency for the Enduser. By forcing it to jump to the last Frame received it will be much less Latency, but a check need to performed to check if the source finished decoding.

The Buffer only stores a few 100MB of Video (15min by 1280/720@30fps) and will discard older data, even if seekable range in the video field shows older video data.  

https://developer.mozilla.org/en-US/docs/Web/API/SourceBuffer

## MimeCodec

MIME (Multipurpose internet mail extensions) Codec holds the Codec information of the Video and Audio. In case of a H264 Video this would be the Codec, Profile, Constraints and Level e.g. "AVC1.640028"(see [H.264](h264.md)).

https://developer.mozilla.org/en-US/docs/Glossary/MIME_type

https://developer.mozilla.org/en-US/docs/Web/Media/Formats/codecs_parameter#avc_profiles