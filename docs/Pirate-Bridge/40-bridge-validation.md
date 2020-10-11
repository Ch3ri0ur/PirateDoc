# Bridge Validation and Future Steps

In this section the initial requirements are measured against the current implementation.

## Functional Requirements

The functional requirements are matched by the implementation.

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
    * In stress tests the Bridge ran stably for more than 72 hours.
* The connection should be available 24/7
    * In stress tests the Bridge ran stably for more than 72 hours.
* The latency of the whole chain may not exceed 2 seconds
    * For the Bridge communication to the client 300 ms are allocated
        * The latency has not yet been measured but in preliminary tests the Bridge can operate at speeds above 25 variables sent per 16 ms interval. With an estimate of 10 bytes per message and a serial send buffer size of 64 bytes the buffer is cycled through multiple times per 16 ms interval placing the latency well below the targeted 300 ms.
* The Bridge must implement the Serial Protocol defined in: [Serial Protocol](../Pirate-Hook/pirate-serial-protocol.md)
    * The Bridge implements the Protocol.
* The Bridge must implement the HTTP API defined in: [HTTP API](client-facing-interface.md)
    * The Bridge implements the API.

## Future Steps

* to improve performance the data sending protocol will be adapted to send the delimiter not every variable but but batch multiple messages.
* to improve security the types and indexes should be checked before sending in either direction.
* a suit of tests is needed to further prove the stability of the Bridge.