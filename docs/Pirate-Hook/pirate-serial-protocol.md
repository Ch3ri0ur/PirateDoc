# Pirate Serial Protocol

The Pirate Serial Protocol is used by the [Pirate Hook](00-hook.md) and the [Pirate Bridge](../Pirate-Bridge/00-bridge.md) to transmit data between them. It was for the usage with an [Arduino](Theory/arduino.md) and a Raspberry Pi generated and uses the serial connection. The protocol makes the [Arduino](Theory/arduino.md) to a Master and the the Raspberry Pi to a Slave of the communication.

The Master side of this Communication is implemented by the [Pirate Hook](00-hook.md) and is limited by the Arduino performance. It needed to be less intensive in computing time and bandwidth. Also it shouldn't block the loop of the Arduino to much or other needed calculations and action on the single processed controller could be delayed. For this the Master side of the Protocol will use the data in its byte format directly from the Memory and will not need to perform any parsings. This also shrinks the amount of bytes to send in the Serial Communication and generates fixed size Messages. Also it will never need to wait on the Slave, it will send asynchron Data or request some Data, which also will arrive asynchron. The reason for the Request is to stop an overflow in the input buffer of the Master.

The Slave in this case will be the [Pirate Bridge](../Pirate-Bridge/00-bridge.md), that will have to read all incoming data and wait for delimiter and messsagetype symbols from the Master. That shouldn't be a problem for this side, because we expect that it would be a Raspberry Pi or something equal or better. It should own an OS to manage tasks, so that blocking couldn't occurs. With the multi core System and high Clock frequency ([Arduino](Theory/arduino.md) Uno 16MHz) the parsing and handeling of the data on event base shouldn't be a problem. With a virtual buffersize of 4KB an overflow shouldn't happen, too.

To allow different [Arduino](Theory/arduino.md) Boards as Master, even if the byte size of some datatypes are different, the Master sends at the start the byte size of each datatype and its own Buffersize. This way the parser in the Slave can modify its data the way it needs to be.

To make the Website [Pirate Flag](../Pirate-Flag/00-flag.md) as dynamic as possible and to reduce the effort of creating one, the Master also sends information about each generated Send and Receive variable. This way the website generates from this data directly a basic layout with all Components. The informations contain Name, Type and some more parameter that will be listed in a section below. 

All Symbols used in the Protocol are based on ASCII (http://www.asciitable.com/) values and are only one character long and Strings are only char arrays with an '\0' at the end.

<a id="idoffset"></a>
ID's of Messages have an offset of '0x30', what represents a '0' in ASCII. This is to make the first 10 Messages better readable in the Terminal. 

<a id="byteformat"></a>
When something refers to Value in "byteformat", than it means that the value of any Datatype is split in bytes that are order in LSB (least significant Byte first). Strings are unaffected by this.


## Master to Slave

All Messages from the Master to the Slave End with a Delimiter, so that the Slave can easy separate the different messages.
```
0xff, 'P', 'i', 'r', 'A', 't', 'E', '\n'
```
The length of the Delimiter is chosen to never get mixups with data. The Newline and the choice of readable symbol's was chosen to allow reading of the data Stream in Serial Terminal from the Arduino IDE.

<a id="datatypes"></a>
Data containing messages get signed with a Datatype Symbol, these Symbols are listed in the table below.

|   Datatype    | Symbol |
| :-----------: | :----: |
|      int      |   I    |
| unsigned int  |   U    |
|     long      |   L    |
| unsigned long |   u    |
|     float     |   F    |
|    double     |   D    |
|     byte      |   B    |
|     word      |   W    |
|     bool      |   b    |
|     char      |   C    |
|    char[]     |   S    |


The Master to Slave Communication can be separated in 3 different Categories
- Initial Informations
- Sending of Informations
- Requesting of Informations



### Initial Communication

To allow the Website auto generation and inform the Slave, what data can be Received or Send and what bytesize is used for the different [Message Datatypes](#datatypes) the Master has to send this informations at the start.

1. Synced Start

    To Sync the Communications and to ignore all Data send before the Communication starts with a Start Sequence:

    ```
    0xee, 'P', 'i', 'r', 'A', 't', 'E', '\n'
    ```

    It has no Delimiter at the end

2. Datatypes info 'P'

    To inform the Slave about the Bytesize of the different Datatypes an information about each Datatype and its size gets send at the start. This Message starts with a 'P' and contains each [Message Datatype Symbol](#datatypes) followed with its bytesize as number. All the Types are separated by a Separator '$'.

3. Send Message info 'T'

    For the Website generation a list of all incoming data is needed. For this Reason an information of all Send messages need to be send at the start. This type of Message is signed with an 'T' and gets repeated for each Send Message index.

    The content of this Message is ID (with [Offset](#idoffset)), Name, [Datatype](#datatypes) and Scale separated by a Separator '$':

    ```
    T<ID>$<Name>$<Type>$<Scale>
    ```

    !!! note "For Example:"
        ```
        T0\$X1\0\$I\$Y
        ```

        Is the Information about the Send Message with ID = 0 that has the Name = X1, Datatype = Int and gets displayed in the Scale 'Y'.

4. Receive Message info 't'

    All Values that can be controlled by the Website need also be listed. This information get also be send at the start and is signed with a 't'. It gets repeated for each Message ID

    The content of this Message is ID (with [Offset](#idoffset)), Name, [Datatype](#datatypes), DefaultValue, MaxValue and MinValue separated by a Separator '$':

    ```
    t<ID>$<Name>$<Type>$<Default>$<Max>$<Min>
    ```

    !!! note "For Example:"
        ```
        t0\$X1\0\$I\$0$100$-100
        ```

        Is the Information about the Receive Message with ID = 0 that has the Name = X1, Datatype = Int, that starts with a default value = 0 and can be set to values between -100 and 100.

    In case of [Datatype](#datatypes) String the Max Value is the max length of the String without the '\0'.

### Sending of Informations

All Informations that get send to the Slave start with a [Datatype Symbol](#datatypes) followed by the Message ID (with [Offset](#idoffset)) and the Datavalue in [raw Bytes](#byteformat):

```
<Type><ID><ValueAsBytes>
```

!!! note "For Example:"
    ```
    C0A
    ```

    A 'C' Char Message that is for Data with the Index = 0 contains the Value 'A'.

### Requesting of Informations <a id="request"></a>

When the Master can receive new Informations and no Data is available in the Buffer, than the Master can Request new Data by Sending out an Request. This is signed by an 'R' and contains no other informations.

```
R
```

It should be only send after all Received Data is read and no [NoData](#nodata) from the Slave was received. After an Intervall of not receiving any Data or [NoData](#nodata) the Master can request again to keep the Communication running.

## Slave to Master

Slave can only Answer on the Master [Request](#request), but the Master has to restart the Communication, when the Serial Connection is established and send all the Initial informations again.

On the [Request](#request) the Slave can answer with a Data Transfer or a No Data.

### Data Transfer

When a [Request](#request) is received the Slave can send Data till the buffer size is reached or end it with a [NoData](#nodata). The Sending of multiple Values for one Message Index in one Message shouldn't be done. The Values could get ignored or could slowly be readout and cause unpredictable changes.

All Data that gets transmitted has to start with the Message ID followed by the Value in [Byteformat](#byteformat) and bytesize that got defined in the start.

```
<ID><ValueAsBytes>
```

!!! note "For Example:"
    ```
    00
    ```

    A Message for the Data with Index = 0 and it contains an one Byte long data with the value 0x30.

### No Data <a id="nodata"></a>

When on a Request no Data available is, the Slave can send a "No Data" '0x29' to the Master, to inform it to not ask for more Data till the next intervall.

```
0x29
```

0x29 is used because the Indexes start with the [Offset](#idoffset) 0x30.