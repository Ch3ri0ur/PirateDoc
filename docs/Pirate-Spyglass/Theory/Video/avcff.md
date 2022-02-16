# AVC FF

## FTYP Box

- FTYP Box
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
    - Name of Box, "ftyp", 4byte, <div align="right">'f' 't' 'y' 'p'</div>
    - major brand,"isom", 4byte, <div align="right">'i' 's' 'o' 'm'</div>
    - minor version, x = 0x200, 4byte, <div align="right">0x00 0x00 0x02 0x00</div>
    - compatible brands, "isomiso2iso5avc1mp41", nbyte, <div align="right">"isomiso2iso5avc1mp41"</div>

## MOOV Box

- MOOV Box
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
    - Name of Box, "moov", 4byte, <div align="right">'m' 'o' 'o' 'v'</div>
    - MVHD Box
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
    - TRAK Box
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
        - Name of Box, "trak", 4byte, <div align="right">'t' 'r' 'a' 'k'</div>
        - TKHD Box
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
        - MDIA Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "mdia", 4byte, <div align="right">'m' 'd' 'i' 'a'</div>
            - MDHD Box
                - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                - Name of Box, "mdhd", 4byte, <div align="right">'m' 'd' 'h' 'd'</div>
                - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                - creation time, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                - modification time, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                - timescale, x = 1000, 4byte, <div align="right">0x00 0x00 0x03 0xe8</div>
                - duration, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                - language ('und' == undefined), x = 0x55c4, 2byte, <div align="right">0x55 0xc4</div>
                - pre-defined, x = 0, 2byte, <div align="right">0x00 0x00</div>
            - HDLR Box
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
            - MINF Box
                - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                - Name of Box, "minf", 4byte, <div align="right">'m' 'i' 'n' 'f'</div>
                - VMHD Box
                     - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                     - Name of Box, "vmhd", 4byte, <div align="right">'v' 'm' 'h' 'd'</div>
                     - version and flags, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
                     - graphics mode, x = 0, 2byte, <div align="right">0x00 0x00</div>
                     - opcolor, x = 0, 2byte, <div align="right">0x00 0x00</div>
                     - opcolor, x = 0, 2byte, <div align="right">0x00 0x00</div>
                     - opcolor, x = 0, 2byte, <div align="right">0x00 0x00</div>
                - DINF Box
                     - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                     - Name of Box, "dinf", 4byte, <div align="right">'d' 'i' 'n' 'f'</div>
                     - DREF Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "dref", 4byte, <div align="right">'d' 'r' 'e' 'f'</div>
                        - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                        - entry count, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
                        - URL Box
                            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                            - Name of Box, "url ", 4byte, <div align="right">'u' 'r' 'l' ' '</div>
                            - version and flags, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
                - STBL Box
                     - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                     - Name of Box, "stbl", 4byte, <div align="right">'s' 't' 'b' 'l'</div>
                     - STSD Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stsd", 4byte, <div align="right">'s' 't' 's' 'd'</div>
                        - reserved, x = 0, 6byte, <div align="right">0x00 0x00 0x00 0x00 0x00 0x00</div>
                        - data reference index, x = 1, 2byte, <div align="right">0x00 0x01</div>
                        - AVC1 Box
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
                            - AVCC Box
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
                     - STSZ Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stsz", 4byte, <div align="right">'s' 't' 's' 'z'</div>
                        - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                        - sample size, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                        - sample count, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                     - STSC Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stsc", 4byte, <div align="right">'s' 't' 's' 'c'</div>
                        - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                        - entry count, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                     - STTS Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stts", 4byte, <div align="right">'s' 't' 't' 's'</div>
                        - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                        - entry count, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                     - STCO Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stco", 4byte, <div align="right">'s' 't' 'c' 'o'</div>
                        - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
                        - entry count, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
    - MVEX Box
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
        - Name of Box, "mvex", 4byte, <div align="right">'m' 'v' 'e' 'x'</div>
        - MEHD Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "mehd", 4byte, <div align="right">'m' 'e' 'h' 'd'</div>
            - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - fragment duration, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - TREX Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "trex", 4byte, <div align="right">'t' 'r' 'e' 'x'</div>
            - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - track id, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
            - default sample description index, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
            - default sample duration, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - default sample size, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
            - default sample flags, x = 0x00010000, 4byte, <div align="right">0x00 0x01 0x00 0x00</div>




## Raspberry Pi 3B+ SPS/PPS for H.264 Main 4.0 1280x720
### Sequence Parameter Set
sps := []byte{
    0x27, 0x64, 0x00, 0x28, 0xac, 0x2b, 0x40, 0x28,
    0x02, 0xdd, 0x00, 0xf1, 0x22, 0x6a,
}
### Picture Parameter Set
pps := []byte{
    0x28, 0xee, 0x02, 0x5c, 0xb0, 0x00,
}


## MOOF Box

- MOOF Box
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
    - Name of Box, "moof", 4byte, <div align="right">'m' 'o' 'o' 'f'</div>
    - MFHD Box
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
        - Name of Box, "mfhd", 4byte, <div align="right">'m' 'f' 'h' 'd'</div>
        - version and flags, x = 0, 4byte, <div align="right">0x00 0x00 0x00 0x00</div>
        - sequence number, x = sequence, 4byte, <div align="right">x[3] ... x[0]</div>
    - TRAF Box
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
        - Name of Box, "traf", 4byte, <div align="right">'t' 'r' 'a' 'f'</div>
        - TFHD Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "tfhd", 4byte, <div align="right">'t' 'f' 'h' 'd'</div>
            - version and flags, x = 0x020020, 4byte, <div align="right">0x00 0x02 0x00 0x20</div>
            - track ID, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
            - default sample flags, x = 0x01010000, 4byte, <div align="right">0x01 0x01 0x00 0x00</div>
        - TFDT Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "tfdt", 4byte, <div align="right">'t' 'f' 'd' 't'</div>
            - version and flags, x = 0x01000000, 4byte, <div align="right">0x01 0x00 0x00 0x00</div>
            - base media decode time, x = 330*sequence, 8byte, <div align="right">x[7] ... x[0]</div>
        - TRUN Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "trun", 4byte, <div align="right">'t' 'r' 'u' 'n'</div>
            - version and flags, x = 0x00000305, 4byte, <div align="right">0x00 0x00 0x01 0x31</div>
            - sample count, x = 1, 4byte, <div align="right">0x00 0x00 0x00 0x01</div>
            - data offset, x = 0x70, 4byte, <div align="right">0x00 0x00 0x00 0x70</div>
            - first sample flags (i-frame or not), x = 0x02000000 or x = 0x01010000 , 4byte, <div align="right">0x20 0x00 0x00 0x00 or 0x01 0x01 0x00 0x00</div>
            - sample duration, x = 330, 4byte, <div align="right">0x00 0x00 0x01 0x4a</div>
            - sample size, x = 4+lengthData, 4byte, <div align="right">x[3] ... x[0]</div>

## MDAT Box (Media Data Box)

- MDAT Box (Media Data Box)
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
    - Name of Box, "mdat", 4byte, <div align="right">'m' 'd' 'a' 't'</div>
    - data length, x = lengthData, 4byte, <div align="right">x[3] ... x[0]</div>
    - data, x = data, nbyte, <div align="right">x[0] ... x[n]</div>