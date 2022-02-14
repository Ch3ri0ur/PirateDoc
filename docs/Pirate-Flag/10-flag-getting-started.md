# Getting Started

The assumption is that the Raspberry PI was correctly [set up](../Getting%20Started/setupraspberrypi.md) and [[NodeJS]] was installed.

To start install this project follow these steps:

## Fetch and install the Github repository

```
git clone https://github.com/Ch3ri0ur/pirate.git
cd pirate
npm install
```

## Run in a Development Mode
```
npm run start
```

## Build for Production
```
npm run build
```
This command compresses the client and strips out unnecessary symbols. The resulting bundle is saved to the ./build directory.

## Serve the Production build

Any static HTTP server can serve this build, but the [Pirate-Bridge](../Pirate-Bridge/00-bridge.md) already serves the ./build folder in its root directory. So the build folder can just be moved.

Alternatively can the caddy server of the Map be configured to serve this folder instead of routing the "/" endpoint to the Bridge.

