# AVC FF

## FTYP Box

- FTYP Box
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
    - Name of Box, "ftyp", 4byte, <div align="right">'f' 't' 'y' 'p'
    - major brand
    - minor version
    - compatible brands

## MOOV Box

- MOOV Box
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
    - Name of Box, "moov", 4byte, <div align="right">'m' 'o' 'o' 'v'
    - MVHD Box
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
        - Name of Box, "mvhd", 4byte, <div align="right">'m' 'v' 'h' 'd'
        - version and flags
        - creation time
        - modification time
        - timescale
        - duration (all 1s == unknown)
        - rate (1.0 == normal)
        - volume (1.0 == normal)
        - reserved
        - reserved
        - reserved
        - matrix
        - matrix
        - matrix
        - matrix
        - matrix
        - matrix
        - matrix
        - matrix
        - matrix
        - pre-defined
        - pre-defined
        - pre-defined
        - pre-defined
        - pre-defined
        - pre-defined
        - next track id
    - TRAK Box
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
        - Name of Box, "trak", 4byte, <div align="right">'t' 'r' 'a' 'k'
        - TKHD Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
            - Name of Box, "tkhd", 4byte, <div align="right">'t' 'k' 'h' 'd'
            - version and flags (track enabled)
            - creation time
            - modification time
            - track id
            - reserved
            - duration
            - reserved
            - reserved
            - layer
            - alternate group
            - volume (ignored for video tracks)
            - reserved
            - matrix
            - matrix
            - matrix
            - matrix
            - matrix
            - matrix
            - matrix
            - matrix
            - matrix
            - width (fixed-point 16.16 format)
            - height (fixed-point 16.16 format)
        - MDIA Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
            - Name of Box, "mdia", 4byte, <div align="right">'m' 'd' 'i' 'a'
            - MDHD Box
                - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                - Name of Box, "mdhd", 4byte, <div align="right">'m' 'd' 'h' 'd'
                - version and flags
                - creation time
                - modification time
                - timescale
                - duration
                - language ('und' == undefined)
                - pre-defined
            - HDLR Box
                - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                - Name of Box, "hdlr", 4byte, <div align="right">'h' 'd' 'l' 'r'
                - version and flags
                - pre-defined
                - handler type
                - reserved
                - reserved
                - reserved
                - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                - null-terminator
            - MINF Box
                - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                - Name of Box, "minf", 4byte, <div align="right">'m' 'i' 'n' 'f'
                - VMHD Box
                     - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                     - Name of Box, "vmhd", 4byte, <div align="right">'v' 'm' 'h' 'd'
                     - version and flags
                     - graphics mode
                     - opcolor
                     - opcolor
                     - opcolor
                - DINF Box
                     - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                     - Name of Box, "dinf", 4byte, <div align="right">'d' 'i' 'n' 'f'
                     - DREF Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                        - Name of Box, "dref", 4byte, <div align="right">'d' 'r' 'e' 'f'
                        - version and flags
                        - entry count
                        - URL Box
                            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                            - Name of Box, "url ", 4byte, <div align="right">'u' 'r' 'l' ' '
                            - version and flags
                - STBL Box
                     - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                     - Name of Box, "stbl", 4byte, <div align="right">'s' 't' 'b' 'l'
                     - STSD Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                        - Name of Box, "stsd", 4byte, <div align="right">'s' 't' 's' 'd'
                        - reserved
                        - data reference index
                        - AVC1 Box
                            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                            - Name of Box, "avc1", 4byte, <div align="right">'a' 'v' 'c' '1'
                            - reserved
                            - data reference index
                            - pre-defined
                            - reserved
                            - pre-defined
                            - pre-defined
                            - pre-defined
                            - width
                            - height
                            - horizontal resolution: 72 dpi
                            - vertical resolution: 72 dpi
                            - data size: 0
                            - frame count: 1
                            - compressor Length
                            - depth
                            - pre-defined
                            - AVCC Box
                              - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                              - Name of Box, "avcC", 4byte, <div align="right">'a' 'v' 'c' 'C'
                                - configuration version
                                - H.264 profile (0x64 == high)
                                - H.264 profile compatibility
                                - H.264 level (0x28 == 4.0)
                                - nal unit Name - 1 (upper 6 bits == 1)
                                - number of sps (upper 3 bits == 1)
                                - len of sps
                                - sps
                                - number of pps
                                - len pps
                                - pps
                     - STSZ Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                        - Name of Box, "stsz", 4byte, <div align="right">'s' 't' 's' 'z'
                        - version and flags
                        - sample size
                        - sample count
                     - STSC Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                        - Name of Box, "stsc", 4byte, <div align="right">'s' 't' 's' 'c'
                        - version and flags
                        - entry count
                     - STTS Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                        - Name of Box, "stts", 4byte, <div align="right">'s' 't' 't' 's'
                        - version and flags
                        - entry count
                     - STCO Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
                        - Name of Box, "stco", 4byte, <div align="right">'s' 't' 'c' 'o'
                        - version and flags
                        - entry count
    - MVEX Box
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
        - Name of Box, "mvex", 4byte, <div align="right">'m' 'v' 'e' 'x'
        - MEHD Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
            - Name of Box, "mehd", 4byte, <div align="right">'m' 'e' 'h' 'd'
            - version and flags
            - fragment duration
        - TREX Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
            - Name of Box, "trex", 4byte, <div align="right">'t' 'r' 'e' 'x'
            - version and flags
            - track id
            - default sample description index
            - default sample duration
            - default sample size
            - default sample flags




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
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
    - Name of Box, "moof", 4byte, <div align="right">'m' 'o' 'o' 'f'
    - MFHD Box
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
        - Name of Box, "mfhd", 4byte, <div align="right">'m' 'f' 'h' 'd'
        - version and flags
        - sequence number
    - TRAF Box
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
        - Name of Box, "traf", 4byte, <div align="right">'t' 'r' 'a' 'f'
        - TFHD Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
            - Name of Box, "tfhd", 4byte, <div align="right">'t' 'f' 'h' 'd'
            - version and flags
            - track ID
            - default sample flags
        - TFDT Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
            - Name of Box, "tfdt", 4byte, <div align="right">'t' 'f' 'd' 't'
            - version and flags
            - base media decode time
        - TRUN Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
            - Name of Box, "trun", 4byte, <div align="right">'t' 'r' 'u' 'n'
            - version and flags
            - sample count
            - data offset
            - first sample flags (i-frame or not)
            - sample duration
            - sample size

## MDAT Box

- MDAT Box
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]
    - Name of Box, "mdat", 4byte, <div align="right">'m' 'd' 'a' 't'
    - data length
    - data