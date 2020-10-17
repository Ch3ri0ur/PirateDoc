# Overview Pirate Hook

The Pirate Hook hooks into the users arduino program and provides functionality for the data transfer from and to the [Pirate Flag](../Pirate-Flag/00-flag.md) over the [Pirate Bridge](../Pirate-Bridge/00-bridge.md).

The communication to the [Pirate Bridge](../Pirate-Bridge/00-bridge.md) uses the [Pirate Serial Protocol](pirate-serial-protocol.md) that was created for this project. The protocol is kept simple and is focused on reducing the amount of actions on the Arduino side. Also the thinking is mostly exported on the [Pirate Bridge](../Pirate-Bridge/00-bridge.md) side.

Pirate Hook uses a serial connection of the [Arduino's](Theory/arduino.md) to transmit and receive data by the protocol. In the current implementation only Serial communication over UART/USB is supported.


## [Getting Started](10-hook-getting-started.md)

In the [Getting Started](10-hook-getting-started.md) you find all needed steps to get it running on the Arduino. Also some more modification that can be done by Defines can found there. 
[Getting Started](10-hook-getting-started.md){: .md-button .md-button--primary }


## [Requirements](20-hook-requirements.md)

The [Requirements](20-hook-requirements.md) have been created from the first wishes and got extended by needed features and aspects, that occurred during the development. Some of them are currently very focused on the initial setup of Raspberry Pi and Arduino. This will maybe in further Steps change.

## Theory

In the Theory Folder some knowledge can be found, that influenced the decisions of the specifications. Also it includes data sheets and other research material.

## [Implementation](30-hook-implementation.md)

In the [Implementation](30-hook-implementation.md) Section all function descriptions and their requirements to function probably can be found here. Also the possible user modifications and the normal and special behavior in situations are described. This includes the wanted features and known bugs or tradeoffs.

## [Validation](40-hook-validation.md)

The [Validation](40-hook-validation.md) contains a overview of the requirement fulfillment of the created Hook implementation. Used concepts get rated and further needed and planned steps get introduced.






