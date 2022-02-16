# MPEG AVC File Format

The Shown structure and values are from the currently used Project BerryMSE and contains almost the complete possible AVC File Format defined in MPEG-4 Part 15. There is still room to add, change or remove Parts of it.

More detailed Information can be found in the Public Document to Common File Format & Media Formats Specification https://www.uvcentral.com/files/CFFMediaFormat-2_1.pdf. It is a extension of the ISOBMFF and extends it by a few more Boxes, but provides good information to each Box.

 Fragmented Movie Architecture:
![Fragmented Movie https://alexzambelli.com/blog/wp-content/uploads/smooth_slide16.png](../../../attachment/Spyglass/FragmentedMovie.png)
Source: https://alexzambelli.com/blog/wp-content/uploads/smooth_slide16.png

In the Project the FTYP, MOOV, MOOF and MDAT Boxes are used to send the Metadata and Media Data of the H264 Video Stream. MOOV and MOOF contain more Boxes and in this project a lot of them are implemented. Only a few Boxes are active used by us, but many are just filled with default Values. Ee don't know what impact it has to use change, remove or add Boxes. The MFRA Box isn't used in this project.

The Boxes of the AVC File Format Structure and the used sub Boxes are shown bellow. The Bytestream is displayed on the right. Not all values are fixed so some will change and the bytes are only listed as Array Index of the Variable.

## FTYP Box (File Type Box)

Defines Type of File, Version and Compatible ISO Files.

- FTYP Box (File Type Box)
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
    - Name of Box, "ftyp", 4byte, <div align="right">'f' 't' 'y' 'p'</div>
    - major brand,"isom", 4byte, <div align="right">'i' 's' 'o' 'm'</div>
    - minor version, x = 0x200, 4byte, <div align="right">0x00 0x00 0x02 0x00</div>
    - compatible brands, "isomiso2iso5avc1mp41", nbyte, <div align="right">"isomiso2iso5avc1mp41"</div>

## MOOV Box (Movie Box, Movie Metadata Box)

Metadata Container for Presentation.

- MOOV Box (Movie Box)
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
    - Name of Box, "moov", 4byte, <div align="right">'m' 'o' 'o' 'v'</div>
    - MVHD Box (Movie Header Box)
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
        - Name of Box, "mvhd", 4byte, <div align="right">'m' 'v' 'h' 'd'</div>
        - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - creation time, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - modification time, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - timescale, x = 1000, 4byte, <div align="right">0x00 0x00 0x03 0xe8</div>
        - duration (all 1s == unknown), x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - rate (1.0 == normal), x = 0x00010000, 4byte, <div align="right">0x00 0x01 0x00 0x00</div>
        - volume (1.0 == normal), x = 0x0100, 2byte, <div align="right">0x01 0x00</div>
        - reserved, x = 0, 2byte, <div align="right">0x00 0x00</div>
        - reserved, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - reserved, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - matrix, x = 0x00010000, 4byte, <div align="right">0x00 0x01 0x00 0x00</div>
        - matrix, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - matrix, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - matrix, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - matrix, x = 0x00010000, 4byte, <div align="right">0x00 0x01 0x00 0x00</div>
        - matrix, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - matrix, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - matrix, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - matrix, x = 0x40000000, 4byte, <div align="right">0x40 0x00 0x00 0x00</div>
        - pre-defined, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - pre-defined, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - pre-defined, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - pre-defined, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - pre-defined, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - pre-defined, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - next track id, x = -1, 4byte, <div align="right">0xff 0xff 0xff 0xff</div>
    - TRAK Box (Track Box)
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
        - Name of Box, "trak", 4byte, <div align="right">'t' 'r' 'a' 'k'</div>
        - TKHD Box (Track Header Box)
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "tkhd", 4byte, <div align="right">'t' 'k' 'h' 'd'</div>
            - version and flags (track enabled), x = 7, 4byte, <div align="right">0x00 0x00 0x00 0x07</div>
            - creation time, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - modification time, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - track id, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
            - reserved, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - duration, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - reserved, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - reserved, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - layer, x = 0, 2byte, <div align="right">0x00 0x00</div>
            - alternate group, x = 0, 2byte, <div align="right">0x00 0x00</div>
            - volume (ignored for video tracks), x = 0, 2byte, <div align="right">0x00 0x00</div>
            - reserved, x = 0, 2byte, <div align="right">0x00 0x00</div>
            - matrix, x = 0x00010000, 4byte, <div align="right">0x00 0x01 0x00 0x00</div>
            - matrix, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - matrix, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - matrix, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - matrix, x = 0x00010000, 4byte, <div align="right">0x00 0x01 0x00 0x00</div>
            - matrix, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - matrix, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - matrix, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - matrix, x = 0x40000000, 4byte, <div align="right">0x40 0x00 0x00 0x00</div>
            - width (fixed-point 16.16 format), x = width<<16, 4byte, <div align="right">x[3] ... x[0]</div>
            - height (fixed-point 16.16 format), x = height<<16, 4byte, <div align="right">x[3] ... x[0]</div>
        - MDIA Box (Media Box)
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "mdia", 4byte, <div align="right">'m' 'd' 'i' 'a'</div>
            - MDHD Box (Media Header Box)
                - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                - Name of Box, "mdhd", 4byte, <div align="right">'m' 'd' 'h' 'd'</div>
                - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                - creation time, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                - modification time, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                - timescale, x = 1000, 4byte, <div align="right">0x00 0x00 0x03 0xe8</div>
                - duration, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                - language ('und' == undefined), x = 0x55c4, 2byte, <div align="right">0x55 0xc4</div>
                - pre-defined, x = 0, 2byte, <div align="right">0x00 0x00</div>
            - HDLR Box (Handler Box)
                - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                - Name of Box, "hdlr", 4byte, <div align="right">'h' 'd' 'l' 'r'</div>
                - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                - pre-defined, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                - handler type, "vide", 4byte, <div align="right">'v' 'i' 'd' 'e'</div>
                - reserved, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                - reserved, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                - reserved, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                - name, "MicroMSE Video Handler", nbyte, <div align="right">"MicroMSE Video Handler"</div>
                - null-terminator, x = 0, 1byte, <div align="right">0x00</div>
            - MINF Box (Media Information Box)
                - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                - Name of Box, "minf", 4byte, <div align="right">'m' 'i' 'n' 'f'</div>
                - VMHD Box (Video Media Header Box)
                     - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                     - Name of Box, "vmhd", 4byte, <div align="right">'v' 'm' 'h' 'd'</div>
                     - version and flags, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
                     - graphics mode, x = 0, 2byte, <div align="right">0x00 0x00</div>
                     - opcolor, x = 0, 2byte, <div align="right">0x00 0x00</div>
                     - opcolor, x = 0, 2byte, <div align="right">0x00 0x00</div>
                     - opcolor, x = 0, 2byte, <div align="right">0x00 0x00</div>
                - DINF Box (Data Information Box)
                     - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                     - Name of Box, "dinf", 4byte, <div align="right">'d' 'i' 'n' 'f'</div>
                     - DREF Box (Data Reference Box)
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "dref", 4byte, <div align="right">'d' 'r' 'e' 'f'</div>
                        - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                        - entry count, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
                        - URL Box (URL Box)
                            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                            - Name of Box, "url ", 4byte, <div align="right">'u' 'r' 'l' ' '</div>
                            - version and flags, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
                - STBL Box (Sample Table Box)
                     - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                     - Name of Box, "stbl", 4byte, <div align="right">'s' 't' 'b' 'l'</div>
                     - STSD Box (Sample Description Box)
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stsd", 4byte, <div align="right">'s' 't' 's' 'd'</div>
                        - reserved, x = 0, 6byte, <div align="right">0x00 0x00 0x00 0x00 0x00 0x00</div>
                        - data reference index, x = 1, 2byte, <div align="right">0x00 0x01</div>
                        - AVC1 Box (Advanced Codec (H264) Box)
                            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                            - Name of Box, "avc1", 4byte, <div align="right">'a' 'v' 'c' '1'</div>
                            - reserved, x = 0, 6byte, <div align="right">0x00 0x00 0x00 0x00 0x00 0x00</div>
                            - data reference index, x = 1, 2byte, <div align="right">0x00 0x01</div>
                            - pre-defined, x = 0, 2byte, <div align="right">0x00 0x00</div>
                            - reserved, x = 0, 2byte, <div align="right">0x00 0x00</div>
                            - pre-defined, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                            - pre-defined, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                            - pre-defined, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                            - width, x = width, 2byte, <div align="right">x[1] ... x[0]</div>
                            - height, x = height, 2byte, <div align="right">x[1] ... x[0]</div>
                            - horizontal resolution: 72 dpi, x = 0x00480000, 4byte, <div align="right">0x00 0x48 0x00 0x00</div>
                            - vertical resolution: 72 dpi, x = 0x00480000, 4byte, <div align="right">0x00 0x48 0x00 0x00</div>
                            - data size: 0, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                            - frame count: 1, x = 1, 2byte, <div align="right">0x00 0x01</div>
                            - compressor Length, x = 0, 32byte, <div align="right">0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00</div>
                            - depth, x = 0x18, 2byte, <div align="right">0x00 0x18</div>
                            - pre-defined, x = 0xffff, 2byte, <div align="right">0xff 0xff</div>
                            - AVCC Box (AVC Configuration Box)
                                - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                                - Name of Box, "avcC", 4byte, <div align="right">'a' 'v' 'c' 'C'</div>
                                - configuration version, x = 1, 1byte, <div align="right">0x01</div>
                                - H.264 profile (0x64 == high), x = 0x64, 1byte, <div align="right">0x64</div>
                                - H.264 profile compatibility, x = 0x00, 1byte, <div align="right">0x00</div>
                                - H.264 level (0x28 == 4.0), x = 0x28, 1byte, <div align="right">0x28</div>
                                - nal unit Name - 1 (upper 6 bits == 1), x = 0xff, 1byte, <div align="right">0xff</div>
                                - number of sps (upper 3 bits == 1), x = 0xe1, 1byte, <div align="right">0xe1</div>
                                - len of sps, x = lengthSPS, 2byte, <div align="right">x[1] ... x[0]</div>
                                - sps, x = sps, nbyte, <div align="right">x[n] ... x[0]</div>
                                - number of pps, x = 1, 1byte, <div align="right">0x01</div
                                - len pps, x = lengthPPS, 2byte, <div align="right">x[1] ... x[0]</div>
                                - pps, x = pps, nbyte, <div align="right">x[n] ... x[0]</div>
                     - STSZ Box (Sample Size Box)
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stsz", 4byte, <div align="right">'s' 't' 's' 'z'</div>
                        - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                        - sample size, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                        - sample count, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                     - STSC Box (Sample to Chunk Box)
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stsc", 4byte, <div align="right">'s' 't' 's' 'c'</div>
                        - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                        - entry count, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                     - STTS Box (Time to Sample Box)
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stts", 4byte, <div align="right">'s' 't' 't' 's'</div>
                        - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                        - entry count, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                     - STCO Box (Chunk Offset Box)
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stco", 4byte, <div align="right">'s' 't' 'c' 'o'</div>
                        - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                        - entry count, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
    - MVEX Box (Movie Extends Box)
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
        - Name of Box, "mvex", 4byte, <div align="right">'m' 'v' 'e' 'x'</div>
        - MEHD Box (Movie Extends Header Box)
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "mehd", 4byte, <div align="right">'m' 'e' 'h' 'd'</div>
            - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - fragment duration, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - TREX Box (Track Extends Box)
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "trex", 4byte, <div align="right">'t' 'r' 'e' 'x'</div>
            - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - track id, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
            - default sample description index, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
            - default sample duration, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - default sample size, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - default sample flags, x = 0x00010000, 4byte, <div align="right">0x00 0x01 0x00 0x00</div>


### AVC1 and AVCC Box

The most Important Boxes of the MOOV for the H264 Streaming are the AVC1 and AVCC Box. They contain needed Information for the Decoder, which settings/parameter are used.
This Includes Profile, Constraints, Level, SPS and PPS.
More info to this can be found in [H.264](h264.md).


## MOOF Box (Movie Fragment Box)

The MOOF Box holds the information to a Movie Fragment, which is in the following MDAT Object.

- MOOF Box (Movie Fragment Box)
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
    - Name of Box, "moof", 4byte, <div align="right">'m' 'o' 'o' 'f'</div>
    - MFHD Box (Movie Fragment Header Box)
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
        - Name of Box, "mfhd", 4byte, <div align="right">'m' 'f' 'h' 'd'</div>
        - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - sequence number, x = sequence, 4byte, <div align="right">x[3] ... x[0]</div>
    - TRAF Box (Track Fragment Box)
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
        - Name of Box, "traf", 4byte, <div align="right">'t' 'r' 'a' 'f'</div>
        - TFHD Box (Track Fragment Header Box)
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "tfhd", 4byte, <div align="right">'t' 'f' 'h' 'd'</div>
            - version and flags, x = 0x020020, 4byte, <div align="right">0x00 0x02 0x00 0x20</div>
            - track ID, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
            - default sample flags, x = 0x01010000, 4byte, <div align="right">0x01 0x01 0x00 0x00</div>
        - TFDT Box (Track Fragment Base Media Decode Time Box)
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "tfdt", 4byte, <div align="right">'t' 'f' 'd' 't'</div>
            - version and flags, x = 0x01000000, 4byte, <div align="right">0x01 0x00 0x00 0x00</div>
            - base media decode time, x = 330*sequence, 8byte, <div align="right">x[7] ... x[0]</div>
        - TRUN Box (Track Fragment Run Box)
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "trun", 4byte, <div align="right">'t' 'r' 'u' 'n'</div>
            - version and flags, x = 0x00000305, 4byte, <div align="right">0x00 0x00 0x01 0x31</div>
            - sample count, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
            - data offset, x = 0x70, 4byte, <div align="right">0x00 0x00 0x00 0x70</div>
            - first sample flags (i-frame or not), x = 0x02000000 or x = 0x01010000 , 4byte, <div align="right">0x20 0x00 0x00 0x00 or 0x01 0x01 0x00 0x00</div>
            - sample duration, x = 330, 4byte, <div align="right">0x00 0x00 0x01 0x4a</div>
            - sample size, x = 4+lengthData, 4byte, <div align="right">x[3] ... x[0]</div>

## MDAT Box (Media Data Box)

The Media Box holds an Media Sample. In this Project this is a NAL Unit.

- MDAT Box (Media Data Box)
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
    - Name of Box, "mdat", 4byte, <div align="right">'m' 'd' 'a' 't'</div>
    - data length, x = lengthData, 4byte, <div align="right">x[3] ... x[0]</div>
    - data, x = data, nbyte, <div align="right">x[0] ... x[n]</div>