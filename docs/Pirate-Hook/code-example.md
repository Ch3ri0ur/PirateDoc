# Code Example


## Define Amount in Pirate_Config.h

```c++
//Modify Max amount of Send and Receive Variables
#define PirAtE_SendVar_Amount 2
#define PirAtE_RecvVar_Amount 2
```

## Global Section in .ino

```c++
//Include Pirate
#include "PirAtE.h"

//Create some Global Variables
float actualValue = 0;
int offset = 0;
float setpoint = 0;

```


## Setup in .ino

```c++
void setup()
{
    ...
    //Start Pirate
    PirAtE_START();

    //Add 'actualValue' to Send-register
    PirAtE_ADD_SEND_VAR("Actual Value", &actualValue, PirAtE_DATATYPE_FLOAT);
    
    //Add 'offset' to Receive-register with control limitation
    PirAtE_ADD_RECV_VAR("Offset", &offset, PirAtE_DATATYPE_INT, offset, 200, -200);

    //Add 'setpoint' to Send-register
    PirAtE_ADD_SEND_VAR("Setpoint", &setpoint, PirAtE_DATATYPE_FLOAT);
    //Add 'setpoint' to Receive-register with control limitation
    PirAtE_ADD_RECV_VAR("Setpoint", &setpoint, PirAtE_DATATYPE_FLOAT, 0, 100, 0.01);
    ...
}
```

## Loop in .ino

```c++
void loop()
{
    ...
    //Perform Send and Receive in main Loop
    PirAtE_SEND();
    PirAtE_RECV();
    ...
}
```

## Result

Graph with Actual and Setpoint

Control with offset and setpoint