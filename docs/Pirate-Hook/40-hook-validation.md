# Validation

## tests

The Test Files can be found in the Repository

### Pirate_arduino_Library.ino

Was the Implementation Environment with current feature tests.

### test.ino

Used to Test first Implementation and used for Echo test with Bridge

### testbandwidth.ino

First test to search for bottlenecks and check transmitting rate.

### simulatedPID.ino

For Demonstration a simulation of a controller Project was created.

## Future Steps

- Tests with other [Arduinos](Theory/arduino.md).

- Test with other com types
    - serial RX TX pins
    - SPI
    - I2C


- Adding data security/checks
    - parity

- [Pirate Serial Protocol](pirate-serial-protocol.md) improvement
    - optimize Overhead

- More tests
    - analyzing Speed
    - durability Test

- Compare [Pirate Serial Protocol](pirate-serial-protocol.md) with xcp (Extended Calibration Protocol)
    - Was the creation unnecessary?
