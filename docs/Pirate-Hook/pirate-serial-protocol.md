# Pirate Serial Protocol

The Pirate Serial Protocol is used by the [[Pirate Hook]] and the [[Pirate Bridge]] to transmit data from the [[Arduino]] over a serial connection. It also allows to send commands and values back to the Arduino to control it.

The Arduino side of this Communication implements the [[Pirate Hook]. It needed to be simple to use and less intensive in computing time. It also shouldn't block the loop of the Arduino to much or other needed calculations and action could be delayed. For this the Arduino side of the Protocol will use the data in its byte format directly from the Memory and will not perform any parsings. This also shrinks the amount of bytes to send in the Serial Communication and generates fixed size Messages.

The [[Pirate Bridge]] on the other side needs to do some extra work, what is not so problematic, because this side has an OS to manage tasks and cannot block itself. Also the System can perform much more calculations with its much higher Clock frequency (Arduino Uno 16MHz) and its multi core processor.

To allow different [[Arduino]] Boards to use the Protocol even if the byte size of some datatypes are different, the Arduino sends at the start the byte size of each datatype. This way the parser in the Pirate Bridge can handle it and can also prepare data for the way back.

To make the Website [[Pirate Flag]]as dynamic as possible and to reduce the effort of creating one, the Arduino also sends information about each generated Send and Receive variable. This way the Website generates from this Data directly a basic Layout with all Components. The Informations Contain Name, Type and Some more Parameter that will be Listed in a Section below. 

## General Aspects

All symbols used by the protocol on the [[Pirate Hook]] site are based on ASCII values (see http://www.asciitable.com/).
The message type symbols are often a repräsentation of the content. Means an Integer Message will be signed with an 'I'. This makes it easier to read the stream from the Arduino in the console and allows investigation and tests without the [[Pirate Bridge]].
ID's of receive and send messages have an offset of 0x30 (48), so that the Index 0 is a  char '0' in ASCII. This way when observing a the arduino output and input the ID is a printable char character and Index 0-9 can be directly read.


## [[Pirate Hook]] to [[Pirate Bridge]]
All Messages from the Arduino have to Start with a Unique Symbol to show its content

All Messages from the Arduino have to End with a Delimiter so the Messages can be 

All Strings End with an '\0'

PirAtE_NO_DATA 0x29

//Value Offset 0x30
PirAtE_MSG_DATAID_OFFSET ((byte)'0')




## Node to Arduino

The Arduino Side is kept small, means the Node side hast to Convert the Data in bytes before sending

|  Symbol  |    Msgtype    |       Style        |                    Content                    |
| :------: | :-----------: | :----------------: | :-------------------------------------------: |
|   0x29   |    No Data    |        0x29        | Informs the Arduino that no Data is available |
| >=0x30 | Data Transfer | [ID][ValueInBytes] |              Transfer of a Value              |




## Arduino to Node

byte PirAtE_SERIAL_START[PirAtE_SERIAL_START_LENGTH] = {0xee, 'P', 'i', 'r', 'A', 't', 'E', '\n'};

PirAtE_DATATYPE_INFO 'P'

PirAtE_TRANSMIT_SEPERATOR '$'

byte PirAtE_MSG_DELIMITER[PirAtE_MSG_DELIMITER_LENGTH] = {0xff, 'P', 'i', 'r', 'A', 't', 'E', '\n'};

### Msg Types 
| Symbol |               Msgtype                |                       Style                       |                   Content                   |
| :----: | :----------------------------------: | :-----------------------------------------------: | :-----------------------------------------: |
|   P    |            Datatype Sizes            |                P[Type][Bytes]\$..                 | All datatypes with Size in Bytes get Listed |
|   T    |     Configuration of one SendMsg     | T[ID]\$[Name]\$[Type]\$[DefaultV]\$[MaxV]\$[MinV] |  Every Definition of a Send Msg gets Send   |
|   t    |   Configuration of one ReceiveMsg    |         t[ID]\$[Name]\$[Type]\$[DefaultV]         | Every Definition of a Receive Msg gets Send |
|   R    |         Request for new Data         |                         R                         |        Request to Node for more Data        |
|   I    |      Data Msg containing an int      |                I[ID][ValueInBytes]                |                 sizeof(int)                 |
|   U    | Data Msg containing an unsigned int  |                U[ID][ValueInBytes]                |            sizeof(unsigned int)             |
|   L    |     Data Msg containing an long      |                L[ID][ValueInBytes]                |                sizeof(long)                 |
|   u    | Data Msg containing an unsigned long |                u[ID][ValueInBytes]                |            sizeof(unsigned long)            |
|   F    |     Data Msg containing an float     |                F[ID][ValueInBytes]                |                sizeof(float)                |
|   D    |    Data Msg containing an double     |                D[ID][ValueInBytes]                |               sizeof(double)                |
|   B    |     Data Msg containing an byte      |                   B[ID][1Byte]                    |                sizeof(byte)                 |
|   W    |     Data Msg containing an word      |                   W[ID][2Bytes]                   |                sizeof(word)                 |
|   b    |     Data Msg containing an bool      |                   b[ID][1Byte]                    |                sizeof(bool)                 |
|   C    |     Data Msg containing an char      |                    C[ID][Char]                    |                sizeof(char)                 |
|   S    |    Data Msg containing an char[]     |                   S[ID][String]                   |                      *                      |

[*1]
```
hallo ich bin code
```

### Datatypes
|   Datatype    | Symbol |    Size Definition    |
| :-----------: | :----: | :-------------------: |
|      int      |   I    |      sizeof(int)      |
| unsigned int  |   U    | sizeof(unsigned int)  |
|     long      |   L    |     sizeof(long)      |
| unsigned long |   u    | sizeof(unsigned long) |
|     float     |   F    |     sizeof(float)     |
|    double     |   D    |    sizeof(double)     |
|     byte      |   B    |     sizeof(byte)      |
|     word      |   W    |     sizeof(word)      |
|     bool      |   b    |     sizeof(bool)      |
|     char      |   C    |     sizeof(char)      |
|    char[]     |   S    |           *           |
*MaxLength depends on buffer size and Overhead
PirAtE_RECEIVE_DATATYPE_STRING_MAXLENGTH = PirAtE_Serial_Buffer_Size - PirAtE_CHARARRAY_END_LENGTH - PirAtE_MSG_DATAID_LENGTH
PirAtE_MSG_DATATYPE_STRING_MAXLENGTH = PirAtE_MSG_DATA_MAXLENGTH - PirAtE_CHARARRAY_END_LENGTH


//Offset of actual Data to DataMsg Start
PirAtE_MSG_DATA_OVERHEAD (PirAtE_MSG_DATAID_LENGTH + PirAtE_MSG_DATATYPE_LENGTH)
//MaxData Length
PirAtE_MSG_DATA_MAXLENGTH (PirAtE_Serial_Buffer_Size - PirAtE_MSG_DATA_OVERHEAD - PirAtE_MSG_DELIMITER_LENGTH)

[//begin]: # "Autogenerated link references for markdown compatibility"
[Pirate Hook]: pirate-hook "Pirate Hook"
[Pirate Bridge]: ..\Pirate-Bridge\pirate-bridge "Pirate Bridge"
[Arduino]: arduino "Arduino"
[Pirate Flag]: ..\Pirate-Flag\pirate-flag "Pirate Flag"
[//end]: # "Autogenerated link references"