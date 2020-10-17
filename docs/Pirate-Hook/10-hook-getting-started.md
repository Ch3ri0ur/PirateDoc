# Getting Started

!!! note "Warning!"
    The function names have changed over the versions and can be different in old ones.

In this [Code Example](code-example.md) a really basic Setup can be found and can be extended easily.


## 1. Include Library

The Pirate Library needs to be inserted in the Arduino Project folder. After ```pirate.h``` and ```pirate_config.h``` are in the Folder the Programm/Arduino IDE can be opened again and the Code can be included in the Programm with:

```
#include "pirate.h"
```


## 2. Configs & Help

Config and Help can be found in the ```pirate_config.h```. It Provides the main Config-Parameter that can be adjusted and also the Function descriptions ```!NO DESCRIPTIONS YET!ONLY FUNCTION HEADERS ARE LISTED!```

With the Defines, the amount of possible Send and Receive Variables can be adjusted.

```c++
#define PirAtE_SendVar_Amount 2
#define PirAtE_RecvVar_Amount 2
```

The defined amount needs to be equal or higher the amount used. It will cause Illegal Memory access when this is violated. When the defined amount is higher only a little bit more memory is used, but it will still work.


## 3. Usage

### 3.1. Start<a id=start></a>

The Serial communication with the Host needs to be started, this means at the start of the Setup the Start Function needs to be called. It also sends out the System (Arduino) Based Informations.

    ```c++
    PirAtE_START();
    ```



### 3.2. Add Variables

This needs to happen in the Arduino ```void setup()``` once for each Variable that should be send or received (both at once will work but the sliders in the Website will not adjust with it). It needs to happen after the [Pirate Start](#start) or the information can not be send out!

Datatypes:<a id="datatypes"></a>

|   Datatype    |        Defined Name        |
| :-----------: | :------------------------: |
|      int      |  PirAtE_MSG_DATATYPE_INT   |
| unsigned int  |  PirAtE_MSG_DATATYPE_UINT  |
|     long      |  PirAtE_MSG_DATATYPE_LONG  |
| unsigned long | PirAtE_MSG_DATATYPE_ULONG  |
|     float     | PirAtE_MSG_DATATYPE_FLOAT  |
|    double     | PirAtE_MSG_DATATYPE_DOUBLE |
|     byte      |  PirAtE_MSG_DATATYPE_BYTE  |
|     word      |  PirAtE_MSG_DATATYPE_WORD  |
|     bool      |  PirAtE_MSG_DATATYPE_BOOL  |
|     char      |  PirAtE_MSG_DATATYPE_CHAR  |
|    char[]     | PirAtE_MSG_DATATYPE_STRING |

Strings have some limitations and are handelt different this can be found [here](#strings) or in the [Implementation](30-hook-implementation.md)!

- Add Variables to Send

    All Variables that the user wants to be send and displayed on the website, need to be defined in the Arduino Setup with one of the following functions:

    ```c++
    byte key = PirAtE_ADD_SEND_VAR(Data_Name, Global_VariableAddress, PirAtE_MSG_DATATYPE);

    byte key = PirAtE_ADD_SEND_VAR(Data_Name, Global_VariableAddress, PirAtE_MSG_DATATYPE, PirAtE_Scale);

    byte key = PirAtE_ADD_SEND_VAR(Data_Name, Global_VariableAddress, PirAtE_MSG_DATATYPE, PirAtE_Scale, PirAtE_MSG_SENDMODE);
    ```

    The Function uses these arguments:

    - key: byte
        - Returns a ID that can be used for [Flag management](#flags)
    - Data_Name: String
        - Name of the Variable on the Website. ```E.g. "Var1"```
        - Should be short
    - Global_VariableAdress: *any
        - Pointer to any supported [Datatype](#datatypes)
    - PirAtE_MSG_DATATYPE: [PirAtE_MSG_DATATYPE](#datatypes)
    - PirAtE_Scale: String
        - Scale Name in which the Variable should be displayed. ```E.g. "Distance"```
        - Units can be defined in Square Brackets and will. ```E.g. "Distance in [m]"```
        - Default is "y" with no unit
        - Should be short
    - PirAtE_MSG_SENDMODE
        - PirAtE_MSG_SENDMODE_AUTO
            - Send automatically each time it can
        - PirAtE_MSG_SENDMODE_MANUEL
            - Flag needs to be set each time it should be send
        - Default is PirAtE_MSG_SENDMODE_AUTO



- Add Variables to Receive

    All Variables that the user wants to be controllable on the website, need to be defined in the Arduino Setup with the following function:
    ```c++
    byte key = PirAtE_ADD_RECV_VAR(Data_Name, Global_VariableAddress, PirAtE_MSG_DATATYPE, Default_Value, Max_Value, Min_Value);
    ```

    The Function uses these arguments:

    - key: byte
        - Returns a ID that can be used for [Flag management](#flags)
    - Data_Name: String
        - Name of the Variable on the Website. ```E.g. "Var1"```
        - Should be short
    - Global_VariableAdress: *any
        - Pointer to any supported [Datatype](#datatypes)
    - PirAtE_MSG_DATATYPE: [PirAtE_MSG_DATATYPE](#datatypes)
    - Default_Value: any
        - Initial Value
    - Max_Value: any
        - Max Value for the Control
    - Min_Value: any
        - Min Value for the Control


### 3.3. Send and Receive

To be able to Receive and Send the registered variables the Functions for ```Send``` and ```Receive``` need to be performed. They will try to Send and Receive, while trying to not exceed defined maximum Blocktimes, that can be defined.

```c++
PirAtE_SEND();
PirAtE_RECV();
```

They need to be used in the Arduino ```void loop()``` and can be used multiple time, but this will increase the code size. Directly in the main loop, where it is very often called, is the best way to include it. The other code in the Loop should be nonen Blocking, so try to not use any ```delay(ms);```, this way the sending and receiving happens frequently.

## Debug

All Messages need to be Send in the correct format, see [Pirate Serial Protocol](pirate-serial-protocol.md). For Debug the [Pirate Hook](00-hook.md) provides a Function to send Debug message. It can be used like the [Serial.println()](https://www.arduino.cc/reference/de/language/functions/communication/serial/println/).

```c++
PirAtE_DEBUG(content);
PirAtE_DEBUG(content, format);
```

The Function uses these arguments:

- content: any
- format: a format modifier of Serial.println()

Keep in Mind that this will fill the send buffer of the Arduino, especially intensive usage of Debug messages. When used before the Send Methode a full Buffer could cause a skip of the sending. When intensive debugging a [disabling of the Pirate Communication](#disablepirate) and using the serial monitor is recommended.

For better performance in the final application the [Debug Messages can also be turned off](#disabledebug).

### Disable Pirate Protocol<a id="disablepirate"></a>

All Message use the [Pirate Serial Protocol](pirate-serial-protocol.md), this means also all Debug Messages start with an ```M``` and end with the Pirate Delimiter. Also all Send Variables get send all the time.

To make Debugging in the Serial Monitor of the Arduino IDE easier, all Pirate related communication can be disabled with a Define. All Debug Message will than appear like a basic ```Serial.println()``` and the normal Sending gets Disabled. 

```c++
#define PirAtE_COM_OFF
```

The Code size gets reduced dramatically by this, so keep in mind when turning it back on it will turn normal again.

**This can only be used when not connected to the [Pirate Bridge](../attachment/pirate_bridge.png)!**

### Disable Debug<a id="disabledebug"></a>

When this is defined all Debug messages will be deactivated completely.

```c++
#define PirAtE_DEBUG_DISABLED
```

## Strings<a id="strings"></a>

Strings have some special properties, that are different from normal vars. The Send and Receive Var can be added with the basic Add methode, but in these cases the size of the String is set to the maximum possible length, which is depending on the Serial buffersize.

- In case of Sending its defined as ```PirAtE_DATATYPE_STRING_MAXLENGTH```
- In case of Receiving it is ```PirAtE_RECEIVE_DATATYPE_STRING_MAXLENGTH```

This is the char symbol count without the String endsymbole ```\0```.
Long Strings can Influence the behavior of Send and Receive.

- Send String

    For adding Strings to the Send-register the following functions need to be used.
    ```c++
    byte key = PirAtE_ADD_SEND_STRING(Data_Name, Global_VariableAddress);
    byte key = PirAtE_ADD_SEND_STRING(Data_Name, Global_VariableAddress, PirAtE_MSG_SENDMODE);
    byte key = PirAtE_ADD_SEND_STRING(Data_Name, Global_VariableAddress, PirAtE_MSG_SENDMODE, StringBufferLength);
    ```

    - key: byte
        - Returns a ID that can be used for [Flag management](#flags)
    - Data_Name: String
        - Name of the Variable on the Website. ```E.g. "Var1"```
        - Should be short
    - Global_VariableAdress: *any
        - Pointer to any supported [Datatype](#datatypes)
    - PirAtE_MSG_DATATYPE: [PirAtE_MSG_DATATYPE](#datatypes)
    - PirAtE_MSG_SENDMODE
        - PirAtE_MSG_SENDMODE_AUTO
            - Send automatically each time it can
        - PirAtE_MSG_SENDMODE_MANUEL
            - Flag needs to be set each time it should be send
        - Default is PirAtE_MSG_SENDMODE_AUTO
    - StringBufferLength: int
        - Needs to be the Size of the allocated String Buffer (including ```\0``` space)
        - Needs to be Smaller or Equal to ```PirAtE_DATATYPE_STRING_MAXLENGTH + 1```

    **When a String isn't ended correctly it will be replaced with just a ```\0```!**

    **When long strings are used, no Debug messages should be used, because the Buffer could be to full for sending and it will always skip. By Enabling ```PirAtE_AllowActiveWaitingOnSend``` and a long enough blocktime it can be fixed, but cycle time will increase.**

- Receive String

    For adding Strings to the Recv-register the following function needs to be used.

    ```c++
    byte key = PirAtE_ADD_RECV_STRING(Data_Name, Global_VariableAddress, StringBufferLength);
    ```

    - key: byte
        - Returns a ID that can be used for [Flag management](#flags)
    - Data_Name: String
        - Name of the Variable on the Website. ```E.g. "Var1"```
        - Should be short
    - Global_VariableAdress: *any
        - Pointer to any supported [Datatype](#datatypes)
    - PirAtE_MSG_DATATYPE: [PirAtE_MSG_DATATYPE](#datatypes)
    - StringBufferLength: int
        - Needs to be the Size of the allocated String Buffer (including ```\0``` space)
        - Needs to be Smaller or Equal to ```PirAtE_DATATYPE_STRING_MAXLENGTH + 1```

    **When a String isn't ended correctly it will try to read as much character as it finds and end it with a ```\0```! This means some messages could become a part of the string.**

    When using the Default Add Variable Function, these Parameters are handelt different.

    - Default_Value: any
        - No effect
    - Max_Value: any
        - Limits the Size that can be created on the [Pirate Bridge](../Pirate-Bridge/00-bridge.md) side
    - Min_Value: any
        - No effect

     It shouldn't be used to prevent unpredictable and unwanted behavior.

## Flags<a id="flags"></a>

There are two Flags, one for the Send  and one for the Receive Variables.

### Send Flag

This Flag signals the Send function that "New Data is available for sending". It is only needed to be set when the ```PirAtE_MSG_SENDMODE``` is ```PirAtE_MSG_SENDMODE_MANUEL``` of the variable. When set it will send the Data just one Time in the next Send cycle.

```c++
PirAtE_SET_SEND_FLAG(key);
```

- key: byte
    - Is the returned ID of the Add Variable to Send Function.

### Receive Flag

With this Flag, the Receive function will signal that "New Data is available for reading". The Flag can be Read with the Get-function and needs to be reset with the Reset-Function.

```c++
byte PirAtE_GET_RECV_FLAG(key)
PirAtE_RST_RECV_FLAG(key);
```

- key: byte
    - Is the returned ID of the Add Variable to Receive Function.

## More Defines

There are more small Defines for changing the Communication behavior of the Hook.

### Com Defines

The Communication can be adjusted with the following Defines, but the modification has to also happen on the [Pirate Bridge Side](../Pirate-Bridge/00-bridge.md).

```c++
#define PirAtE_Serial_Baudrate 115200
```

When changing the Baudrate, make sure it is supported by the [Arduino](Theory/arduino.md) and in case of debugging in Serial Monitor, its supported Baudrates need to be accounted, too.

### Intervall Defines

With this Defines the message speed can be tweaked, what also has an impact on the Resource intensity on the [Bridge side](../Pirate-Bridge/00-bridge.md). 

```c++
#define PirAtE_SendMSGInterVal_micros 1000ul
#define PirAtE_AllowedSendBlockTime_micros 2000ul
#define PirAtE_RequestInterVal_micros 1000ul
#define PirAtE_AllowedReceiveBlockTime_micros 200ul
```

Detailed description coming soon!

## Good to know

Coming soon!

## Known Bugs

Coming soon!