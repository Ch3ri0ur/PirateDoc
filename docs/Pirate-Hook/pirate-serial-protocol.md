# Pirate Serial Protocol

The Pirate Serial Protocol is used by the [Pirate Hook](00-hook.md) and the [Pirate Bridge](../Pirate-Bridge/00-bridge.md) to transmit data between them. It was for the usage with an [Arduino](Theory/arduino.md) and a Raspberry Pi generated and uses the serial connection. The protocol makes the [Arduino](Theory/arduino.md) to a Master and the the Raspberry Pi to a Slave of the communication.

The Master side of this Communication is implemented by the [Pirate Hook](00-hook.md) and is limited by the Arduino performance. It needed to be less intensive in computing time and bandwidth. Also it shouldn't block the loop of the Arduino to much or other needed calculations and action on the single processed controller could be delayed. For this the Master side of the Protocol will use the data in its byte format directly from the Memory and will not need to perform any parsings. This also shrinks the amount of bytes to send in the Serial Communication and generates fixed size Messages. Also it will never need to wait on the Slave, it will send asynchron Data or request some Data, which also will arrive asynchron. The reason for the Request is to stop an overflow in the input buffer of the Master.

The Slave in this case will be the [Pirate Bridge](../Pirate-Bridge/00-bridge.md), that will have to read all incoming data and wait for delimiter and messsagetype symbols from the Master. That shouldn't be a problem for this side, because we expect that it would be a Raspberry Pi or something equal or better. It should own an OS to manage tasks, so that blocking couldn't occurs. With the multi core System and high Clock frequency ([Arduino](Theory/arduino.md) Uno 16MHz) the parsing and handeling of the data on event base shouldn't be a problem. With a virtual buffersize of 4KB an overflow shouldn't happen, too.

To allow different [Arduino](Theory/arduino.md) Boards as Master, even if the byte size of some datatypes are different, the Master sends at the start the byte size of each datatype and its own Buffersize. This way the parser in the Slave can modify its data the way it needs to be.

To make the Website [Pirate Flag](../Pirate-Flag/00-flag.md) as dynamic as possible and to reduce the effort of creating one, the Master also sends information about each generated Send and Receive variable. This way the website generates from this data directly a basic layout with all Components. The informations contain Name, Type and some more parameter that will be listed in a section below. 

All Symbols used in the Protocol are based on ASCII (http://www.asciitable.com/) values and are only one character long and Strings are only char arrays with an '\0' at the end.

<a id="IDOffset"></a>
ID's of Messages have an offset of '0x30', what represents a '0' in ASCII. This is to make the first 10 Messages better readable in the Terminal. 

## Master to Slave

All Messages from the Master to the Slave End with a Delimiter, so that the Slave can easy separate the different messages.
```
0xff, 'P', 'i', 'r', 'A', 't', 'E', '\n'
```
The length of the Delimiter is chosen to never get mixups with data. The Newline and the choice of readable symbol's was chosen to allow reading of the data Stream in Serial Terminal from the Arduino IDE.

<a id="Datatypes"></a>
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

To allow the Website auto generation and inform the Slave, what data can be Received or Send and what bytesize is used for the different [Message Datatypes](#Datatypes) the Master has to send this informations at the start.

1. Synced Start

    To Sync the Communications and to ignore all Data send before the Communication starts with a Start Sequence:
    ```
    0xee, 'P', 'i', 'r', 'A', 't', 'E', '\n'
    ```
    It has no Delimiter at the end

2. Datatypes info 'P'

    To inform the Slave about the Bytesize of the different Datatypes an information about each Datatype and its size gets send at the start. This Message starts with a 'P' and contains each [Message Datatype Symbol](#Datatypes) followed with its bytesize as number. All the Types are separated by a Separator '$'.

3. Send Message info 'T'

    For the Website generation a list of all incoming data is needed. For this Reason an information of all Send messages need to be send at the start. This type of Message is signed with an 'T' and gets repeated for each Send Message index.

    The content of this Message is ID (with [Offset](#IDOffset)), Name, [Datatype](#Datatypes) and Scale separated by a Separator '$':
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

    The content of this Message is ID (with [Offset](#IDOffset)), Name, [Datatype](#Datatypes), DefaultValue, MaxValue and MinValue separated by a Separator '$':
    ```
    t<ID>$<Name>$<Type>$<Default>$<Max>$<Min>
    ```
    !!! note "For Example:"
        ```
        t0\$X1\0\$I\$0$100$-100
        ```

        Is the Information about the Receive Message with ID = 0 that has the Name = X1, Datatype = Int, that starts with a default value = 0 and can be set to values between -100 and 100.

### Sending of Informations

All Informations that get send to the Slave start with a [Datatype Symbol](#Datatypes) followed by the Message ID (with [Offset](#IDOffset)) and the Datavalue in raw Bytes:
```
<Type><ID><ValueAsBytes>
```
!!! note "For Example:"
    ```
    C0A
    ```

    A 'C' Char Message that is for Message Index 0 contains the Value 'A'.

### Requesting of Informations

*MaxLength depends on buffer size and Overhead
PirAtE_RECEIVE_DATATYPE_STRING_MAXLENGTH = PirAtE_Serial_Buffer_Size - PirAtE_CHARARRAY_END_LENGTH - PirAtE_MSG_DATAID_LENGTH
PirAtE_MSG_DATATYPE_STRING_MAXLENGTH = PirAtE_MSG_DATA_MAXLENGTH - PirAtE_CHARARRAY_END_LENGTH


//Offset of actual Data to DataMsg Start
PirAtE_MSG_DATA_OVERHEAD (PirAtE_MSG_DATAID_LENGTH + PirAtE_MSG_DATATYPE_LENGTH)
//MaxData Length
PirAtE_MSG_DATA_MAXLENGTH (PirAtE_Serial_Buffer_Size - PirAtE_MSG_DATA_OVERHEAD - PirAtE_MSG_DELIMITER_LENGTH)


## Slave to Master

eventbased
The Arduino Side is kept small, means the Node side hast to Convert the Data in bytes before sending

|  Symbol  |    Msgtype    |       Style        |                    Content                    |
| :------: | :-----------: | :----------------: | :-------------------------------------------: |
|   0x29   |    No Data    |        0x29        | Informs the Arduino that no Data is available |
| >=0x30 | Data Transfer | [ID][ValueInBytes] |              Transfer of a Value              |


arduino hook master low computing time slave bridge event triggered

rewrite to hook and bridge ignore arduino in protocol just that master slow low computing time and cannot manage tasks and bridge faster more time can manage task event driven

simplyfy master sends type info msg info recv and send 
send happens asynchronus  and compacted

recive after request, request can be repeated immedatly except "no data" was reviced  else send new request after interval after last request to not spam events. data is send compacted in buffer size because request only when empty
