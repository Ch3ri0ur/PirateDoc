# Getting Started

The Pirate Bridge is a single file application. 

As a prerequisite the Raspberry PI should have been set up according to the [setup](../setupraspberrypi.md).

To run it first download the repository and move into that folder, if this has not already been done.

```
git clone https://github.com/Ch3ri0ur/pirate_modules.git
cd pirate_modules
```

If the server repository has not been installed yet run:
```
npm i
```

Then run the application with:
```
node index.js
```

The application expects a running arduino with a configured [Pirate-Hook](../Pirate-Hook/00-hook.md) to be plugged into any USB port.


Optionally it expects a production build version of the [Pirate-Flag](../Pirate-Flag/00-flag.md) to be present in a ./build/ folder to be served.