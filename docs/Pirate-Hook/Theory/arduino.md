# Arduino

Arduino Hardware Information and Limitations can be found here.

## Serial USB (RX/TX)
- Serial buffer
    - Size: 64 byte
    - Source: https://www.arduino.cc/reference/en/language/functions/communication/serial/available/
- UART Protocol Default Setting is "SERIAL_8N1"
    - No Parity
    - 1 Stop Bit
    - Source: https://www.arduino.cc/reference/en/language/functions/communication/serial/begin/
- Baudrates (Some Standards)
    - 9600
    - ...
    - 115200
    - Source: https://de.wikipedia.org/wiki/Universal_Asynchronous_Receiver_Transmitter
- Auto Restart on establishing
        

## Boards Specific
Some parameter are different from Board to Board. To keep the Pirate Hook optimal designed they ahd to be analysed.

In further development, aspects like SPI and I2C need to be inspected to, currently only the basic Serial USB UART Communication is supported.

### Uno
Source: https://store.arduino.cc/arduino-uno-rev3

- Prozessor
    - 16 MHz
    - 32KB  Flash Memory program storage
    - 2 KB SRAM dynamic storage for global variables
- Serial Pin
    - 0(RX), 1(TX) = (USB)

### Nano
Source: https://store.arduino.cc/arduino-nano-every

- Prozessor
    - 16 MHz
    - 48KB Flash Memory program storage
    - 6KB SRAM dynamic storage for global variables
- Serial Pin
    - 0(RX), 1(TX) = (USB)


### Mega
Source: https://store.arduino.cc/arduino-mega-2560-rev3

- Prozessor
    - 16 MHz
    - 256 KB Flash Memory program storage
    - 8 KB SRAM dynamic storage for global variables
- Serial Pin
    -  4 UARTs
- Serial buffer size 64 byte


### Micro
Source: https://store.arduino.cc/arduino-micro-without-headers

- Prozessor
    - 16 MHz
    - 32KB Flash Memory program storage
    - 2.5 KB SRAM dynamic storage for global variables
- Serial Pin
    - 0(RX), 1(TX) + (USB)


