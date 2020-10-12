# Getting Started

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

1. Start

    ```
    PirAtE_START();
    ```



2. Add Variables
    - send

        ```
        key = PirAtE_ADD_SEND_VAR(Data_Name, Global_VariableAddress, PirAtE_MSG_DATATYPE);

        key = PirAtE_ADD_SEND_VAR(Data_Name, Global_VariableAddress, PirAtE_MSG_DATATYPE, PirAtE_Scale);

        key = PirAtE_ADD_SEND_VAR(Data_Name, Global_VariableAddress, PirAtE_MSG_DATATYPE, PirAtE_Scale, PirAtE_MSG_SENDMODE);
        ```



    - recv

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