# Getting Started

!!! note "Warning!"
    The function names have changed over the versions and can be different in old ones.



## 1. Include Library

The Pirate Library needs to be inserted in the Arduino Project folder. After ```pirate.h``` and ```pirate_config.h``` are in the Folder the Programm/Arduino IDE can be opened again and the Code can be included in the Programm with:
```
#include "pirate.h"
```


## 2. Configs & Help

Config and Help can be found in the ```pirate_config.h```. It Provides the main Config-Parameter that can be adjusted and also the Function descriptions ```!NO DESCRIPTIONS YET!ONLY FUNCTION HEADERS ARE LISTED!```

With the Defines, the amount of possible Send and Receive Variables can be adjusted.

```
#define PirAtE_SendVar_Amount 2
#define PirAtE_RecvVar_Amount 2
```

The defined amount needs to be equal or higher the amount used. It will cause Illegal Memory access when this is violated. When the defined amount is higher only a little bit more memory is used, but it will still work.


## 3. Usage

### 3.1. Start<a id=start></a>

The Serial communication with the Host needs to be started, this means at the start of the Setup the Start Function needs to be called. It also sends out the System (Arduino) Based Informations.

    ```
    PirAtE_START();
    ```



### 3.2. Add Variables

This needs to happen in the Setup once for each Variable that should be send or received (both at once will work but the sliders in the Website will not adjust with it). It needs to happen after the [Pirate Start](#start)

- Add Variables to Send

    ```
    key = PirAtE_ADD_SEND_VAR(Data_Name, Global_VariableAddress, PirAtE_MSG_DATATYPE);

    key = PirAtE_ADD_SEND_VAR(Data_Name, Global_VariableAddress, PirAtE_MSG_DATATYPE, PirAtE_Scale);

    key = PirAtE_ADD_SEND_VAR(Data_Name, Global_VariableAddress, PirAtE_MSG_DATATYPE, PirAtE_Scale, PirAtE_MSG_SENDMODE);
    ```



- Add Variables to Receive

    ```
    // key = PirAtE_ADD_RECV_VAR(Data_Name, Global_VariableAddress, PirAtE_MSG_DATATYPE, Default_Value, Max_Value, Min_Value);
    ```




### debug
buffer always full no working
disable debug define


### Strings
```
// key = PirAtE_ADD_SEND_STRING(Data_Name, Global_VariableAddress);
// key = PirAtE_ADD_SEND_STRING(Data_Name, Global_VariableAddress, PirAtE_MSG_SENDMODE);
// key = PirAtE_ADD_SEND_STRING(Data_Name, Global_VariableAddress, PirAtE_MSG_SENDMODE, StringBufferLength);
```

```
// key = PirAtE_ADD_RECV_STRING(Data_Name, Global_VariableAddress, StringBufferLength);
```

strings länge begrenzt serial buffer full \0 fehler verhalten

## More Infos
more defines
disbale com
tweak send revc intervall
serialbuffersize


## good to know
bugs issues features
baudrate datarate