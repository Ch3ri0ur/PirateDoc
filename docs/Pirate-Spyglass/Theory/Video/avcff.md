# AVC FF

## FTYP Box

- FTYP Box
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
    - Name of Box, "ftyp", 4byte, <div align="right">'f' 't' 'y' 'p'</div>
    - major brand
    - minor version
    - compatible brands

## MOOV Box

- MOOV Box
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
    - Name of Box, "moov", 4byte, <div align="right">'m' 'o' 'o' 'v'</div>
    - MVHD Box
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
        - Name of Box, "mvhd", 4byte, <div align="right">'m' 'v' 'h' 'd'</div>
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
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
        - Name of Box, "trak", 4byte, <div align="right">'t' 'r' 'a' 'k'</div>
        - TKHD Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "tkhd", 4byte, <div align="right">'t' 'k' 'h' 'd'</div>
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
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "mdia", 4byte, <div align="right">'m' 'd' 'i' 'a'</div>
            - MDHD Box
                - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                - Name of Box, "mdhd", 4byte, <div align="right">'m' 'd' 'h' 'd'</div>
                - version and flags
                - creation time
                - modification time
                - timescale
                - duration
                - language ('und' == undefined)
                - pre-defined
            - HDLR Box
                - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                - Name of Box, "hdlr", 4byte, <div align="right">'h' 'd' 'l' 'r'</div>
                - version and flags
                - pre-defined
                - handler type
                - reserved
                - reserved
                - reserved
                - name
                - null-terminator
            - MINF Box
                - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                - Name of Box, "minf", 4byte, <div align="right">'m' 'i' 'n' 'f'</div>
                - VMHD Box
                     - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                     - Name of Box, "vmhd", 4byte, <div align="right">'v' 'm' 'h' 'd'</div>
                     - version and flags
                     - graphics mode
                     - opcolor
                     - opcolor
                     - opcolor
                - DINF Box
                     - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                     - Name of Box, "dinf", 4byte, <div align="right">'d' 'i' 'n' 'f'</div>
                     - DREF Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "dref", 4byte, <div align="right">'d' 'r' 'e' 'f'</div>
                        - version and flags
                        - entry count
                        - URL Box
                            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                            - Name of Box, "url ", 4byte, <div align="right">'u' 'r' 'l' ' '</div>
                            - version and flags
                - STBL Box
                     - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                     - Name of Box, "stbl", 4byte, <div align="right">'s' 't' 'b' 'l'</div>
                     - STSD Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stsd", 4byte, <div align="right">'s' 't' 's' 'd'</div>
                        - reserved
                        - data reference index
                        - AVC1 Box
                            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                            - Name of Box, "avc1", 4byte, <div align="right">'a' 'v' 'c' '1'</div>
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
                                - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                                - Name of Box, "avcC", 4byte, <div align="right">'a' 'v' 'c' 'C'</div>
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
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stsz", 4byte, <div align="right">'s' 't' 's' 'z'</div>
                        - version and flags
                        - sample size
                        - sample count
                     - STSC Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stsc", 4byte, <div align="right">'s' 't' 's' 'c'</div>
                        - version and flags
                        - entry count
                     - STTS Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stts", 4byte, <div align="right">'s' 't' 't' 's'</div>
                        - version and flags
                        - entry count
                     - STCO Box
                        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
                        - Name of Box, "stco", 4byte, <div align="right">'s' 't' 'c' 'o'</div>
                        - version and flags
                        - entry count
    - MVEX Box
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
        - Name of Box, "mvex", 4byte, <div align="right">'m' 'v' 'e' 'x'</div>
        - MEHD Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "mehd", 4byte, <div align="right">'m' 'e' 'h' 'd'</div>
            - version and flags
            - fragment duration
        - TREX Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "trex", 4byte, <div align="right">'t' 'r' 'e' 'x'</div>
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
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
    - Name of Box, "moof", 4byte, <div align="right">'m' 'o' 'o' 'f'</div>
    - MFHD Box
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
        - Name of Box, "mfhd", 4byte, <div align="right">'m' 'f' 'h' 'd'</div>
        - version and flags
        - sequence number
    - TRAF Box
        - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
        - Name of Box, "traf", 4byte, <div align="right">'t' 'r' 'a' 'f'</div>
        - TFHD Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "tfhd", 4byte, <div align="right">'t' 'f' 'h' 'd'</div>
            - version and flags
            - track ID
            - default sample flags
        - TFDT Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "tfdt", 4byte, <div align="right">'t' 'f' 'd' 't'</div>
            - version and flags
            - base media decode time
        - TRUN Box
            - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
            - Name of Box, "trun", 4byte, <div align="right">'t' 'r' 'u' 'n'</div>
            - version and flags
            - sample count
            - data offset
            - first sample flags (i-frame or not)
            - sample duration
            - sample size

## MDAT Box

- MDAT Box
    - Length of Box, x = length of Box Content, 4byte, <div align="right">x[3] ... x[0]</div>
    - Name of Box, "mdat", 4byte, <div align="right">'m' 'd' 'a' 't'</div>
    - data length
    - data