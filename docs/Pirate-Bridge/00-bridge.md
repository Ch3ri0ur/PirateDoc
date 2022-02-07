# Overview Pirate Bridge

The Bridge component translates the serial communication with the Arduino and provides an API for the clients.

[Getting Started](10-bridge-getting-started.md){: .md-button .md-button--primary }

## Requirements

* Managing the connection with the Pirate Hook on the connected Arduino
* Serving an API for
    * Sending the project data 
    * Receiving and forwarding control commands
* Serving the client website 

[Requirements](20-bridge-requirements.md){: .md-button}

## Implementation

The Bridge is a [[nodejs]] application which reads the serial port on the Raspberry PI and broadcasts the information to all connected clients. (more about this interface here: [client facing API](client-facing-interface.md)). 

When polled the Bridge will supply the Arduino with the values the clients sent to it. 

It also serves the client website, the [Pirate Flag](../Pirate-Flag/00-flag.md).

[Implementation](30-bridge-implementation.md){: .md-button}

## Validation

In this section the requirements are compared with the current state of the project and future steps outlined.

[Validation](40-bridge-validation.md){: .md-button}

