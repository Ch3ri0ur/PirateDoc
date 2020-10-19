# Implementation

!!! note "Warning!"
    The function names have changed over the versions and can be different in old ones.

!!! note "Warning!"
    Current Implementation supports only the normal Serial communication.

The low memory and time usage aspect are partly the reason, why many functions are just macros, that get optimized by the compiler.

!!! note "Note:"
    Functions mostly covered in [Getting Started](10-hook-getting-started.md)!

!!! note "Note:"
    When in the Implementation the Datatype String is mentioned, than it refers to the Char Array Sting with an ```\0``` at the end. The String Object would use more memory and can also create holes in the stack, when resizing.

## Overview of Implementation

- Requirement: Simple to use

    - Only 3 needed Stages for the User

        1. Start Communication (Setup)
        2. Add Variables (Setup)
        3. Perform Send & Receive (Main Loop)

    - Default Configuration already in "PirAtE_Config.h"

- Requirement: Time Usage

    - No Active Waiting
    - Maximum Blocktime adjustable
    - Uses Macros for Send and Receive

- Requirement: Resource Usage

    - Uses Pointer on Variables
    - Mostly optimized with Macros and Defines

## User functions, macros and defines

### PirAtE_START() : Macro

**Must be used once in the Setup! Before any other PirAtE Functions.**

```c++
PirAtE_START()
```

Arguments:

- None

Returns:

- void

Activates the Serial Communication and also sends out the Datatype information and Buffersize. This is defined in the Initial steps of [Pirate Serial Protocol](pirate-serial-protocol.md).

When [Pirate Communication is Disabled](#disablepirate) it will skip the Initial steps of the [Pirate Serial Protocol](pirate-serial-protocol.md), but still start the Serial Port.

### Datatypes: Defined char Values<a id="datatypes"></a>

All Datatypes that can be used for Receive and Send Variables come from the [Pirate Serial Protocol](pirate-serial-protocol.md) and are listed below with their Define Name.

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

### PirAtE_MSG_SENDMODE_... : Defined int Values<a id="sendmodes"></a>

For the Sending some modes got defined, which configure how the sending should happen.

|  Type  |        Defined Name        |              Description              |
| :----: | :------------------------: | :-----------------------------------: |
|  auto  |  PirAtE_MSG_SENDMODE_AUTO  |         Sends every Intervall         |
| manuel | PirAtE_MSG_SENDMODE_MANUEL | Sends only when [Flag](#flags) is set |


### PirAtE_ADD_SEND_VAR() : Macro

**Should be used only in the Setup! After PirAtE_START() for each Send Var to Add. The Times used can not exceed the [Defined Send Amount](#sendamount).**

```c++
byte key = PirAtE_ADD_SEND_VAR(Data_Name, Global_VariableAddress, PirAtE_MSG_DATATYPE, PirAtE_Scale, PirAtE_MSG_SENDMODE);
```

Arguments:

- Data_Name : String
    - Displayed Name in Graph.
- Global_VariableAddress : (byte*)
    - Address of Variable.
- PirAtE_MSG_DATATYPE : [PirAtE_MSG_DATATYPE_...](#datatypes)
    - Datatype that the Variable uses
- PirAtE_Scale : String
    - Scale used for the Var, with "[unit]" in the String, a Unit can  be defined.
    - default: "y"
- PirAtE_MSG_SENDMODE : [PirAtE_MSG_SENDMODE_...](#sendmodes)
    - Mode allows to control sending behavior.
    - default: PirAtE_MSG_SENDMODE_AUTO

Returns:

- key : byte
    - "Can only be Assigned to a Variable!"

Is overloaded and registrates the variables for the PirAtE_SEND() methode.

When [Pirate Communication is Disabled](#disablepirate) it will skip the Initial steps of the [Pirate Serial Protocol](pirate-serial-protocol.md), but still start the Serial Port.

!!! note "Note:"
    Suggested is it to use programm memory for the Strings in this functions.

    ```c++
    byte key = PirAtE_ADD_SEND_VAR("Name", &..., PirAtE_MSG_DATATYPE_..., "Y in [unit]", PirAtE_MSG_SENDMODE_...);
    ```

### PirAtE_SendVar_Amount : Define<a id="sendamount"></a>

**Needs to be defined in PirAtE_Config.h!**

```c++
#define PirAtE_SendVar_Amount 5
```

Defines the Amount of possible Send Variables. Can be Higher than the actual used amount, but than it will use more memory than needed.

For amount x, an Array for x byte-Pointer will be defined. Also two byte Arrays that are X/8 Bytes long and get rounded up. One is a Register that holds the [Sendmode](#sendmodes) for each Send variable in one bit. The other one is to hold the Flag that signals, if the data Value needs to be send again.

### PirAtE_ADD_RECV_VAR() : Macro

**Should be used only in the Setup! After PirAtE_START() for each Receive Var to Add. The Times used can not exceed the [Defined Send Amount](#recvamount).**

```c++
byte key = PirAtE_ADD_RECV_VAR(Data_Name, Global_VariableAddress, PirAtE_MSG_DATATYPE, Default_Value, Max_Value, Min_Value);
```

Arguments:

- Data_Name : String
    - Displayed Name in the Controls.
- Global_VariableAddress : (byte*)
    - Address of Variable.
- PirAtE_MSG_DATATYPE : [PirAtE_MSG_DATATYPE_...](#datatypes)
    - Datatype that the Variable uses
- Default_Value: any
    - Initial Value for the Controls.
- Max_Value: any
    - Max Value for the Control.
- Min_Value: any
    - Min Value for the Control.

Returns:

- key : byte
    - "Can only be Assigned to a Variable!"

Is overloaded and registrates the variables for the PirAtE_RECV() methode. Can only be done up to the Defined maximum amount of Receive Messages.

When [Pirate Communication is Disabled](#disablepirate) it will skip the Initial steps of the [Pirate Serial Protocol](pirate-serial-protocol.md), but still start the Serial Port.

!!! note "Note:"
    Suggested is it to use programm memory for the Strings in this functions.

    ```c++
    byte key = PirAtE_ADD_RECV_VAR("Name", &..., PirAtE_MSG_DATATYPE_..., ..., ..., ...);
    ```


### PirAtE_RECVVar_Amount : Define<a id="recvamount"></a>

**Needs to be defined in PirAtE_Config.h!**

```c++
#define PirAtE_RecvVar_Amount 5
```

Defines the Amount of possible Receive Variables. Can be Higher than the actual used amount, but than it will use more memory than needed.

For amount x, an Array for x byte-Pointer will be defined. Also one byte Arrays that is X/8 Bytes long and get rounded up. It is a Register that holds the Flag that signals, if the data Value is new.

### PirAtE_SEND() : Macro

**Has to be used in the Main Loop! To get called often as possible!**

```c++
PirAtE_SEND();
```

Arguments:

- None

Returns:

- void

Performs Sending over the serial connection following the [Pirate Serial Protocol](pirate-serial-protocol.md). With Defines the Send intervall, blocktime and active wait behavior can be adjusted.

Is influenced by the Defines:
- PirAtE_SendMSGInterVal_micros
    - default: 1000ul
- PirAtE_AllowedSendBlockTime_micros
    - default: 200ul
- PirAtE_AllowActiveWaitingOnSend
    - default: false


### PirAtE_RECV() : Macro

**Has to be used in the Main Loop! To get called often as possible!**

```c++
PirAtE_RECV();
```

Arguments:

- None

Returns:

- void

Performs Receiving over the serial connection following the [Pirate Serial Protocol](pirate-serial-protocol.md). With Defines the Request intervall and blocktime behavior can be adjusted.

Is influenced by the Defines:
- PirAtE_RequestInterVal_micros
    - default: 1000ul
- PirAtE_AllowedReceiveBlockTime_micros
    - default: 200ul


### PirAtE_COM_OFF<a id="disablepirate"></a>

```c++
#define PirAtE_COM_OFF
```

### PirAtE_DEBUG_DISABLED<a id="disabledebug"></a>

```c++
#define PirAtE_DEBUG_DISABLED
```

## Flags<a id="flags"></a>



# Unfinished

code

focus

hardcoded aspects




psoible modififcations
defines ifndef

debug
comtype func
baudrate
buffersize


bugs
features
need to be done
missing


already for later
serial define
other comtype replacement
