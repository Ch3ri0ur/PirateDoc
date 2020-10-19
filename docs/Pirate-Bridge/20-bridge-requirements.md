# Requirements

The Bridge component has a set of functional and non functional requirements.

The following requirements are derived from the accepted overarching requirements approved by the customer. 

## Functional Requirements

### Pass on stream of variables from Arduino to clients

* The client is connects to the Bridge
* The Arduino sends current variables
* The Bridge send said variables to the client

### Pass on commands to change variables from clients to Arduino

* The client is connects to the Bridge
* The client sends new variable values to the Bridge
* The Bridge send said variables to the Arduino

## Non-Functional Requirements

* The Bridge must run stably for at least 3 hours of continuos use
* The connection should be available 24/7
* The Bridge must be usable with a LTE connection
* The latency of the whole chain may not exceed 2 seconds
    * For the Bridge communication to the client 300 ms are allocated
* The Bridge must implement the Serial Protocol defined in: [Serial Protocol](../Pirate-Hook/pirate-serial-protocol.md)
* The Bridge must implement the HTTP API defined in: [HTTP API](client-facing-interface.md)

