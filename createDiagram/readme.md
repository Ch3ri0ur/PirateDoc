# Generating Diagram 

The Python codes use https://diagrams.mingrammer.com/ and generate the diagram png 


## Installation/Setup Diagrams
Instruction can be found here: https://diagrams.mingrammer.com/docs/getting-started/installation.

The Python installation doesn't need any other package than diagrams.

Diagrams uses/needs Graphviz to be installed on the computer. The newest version is needed, on
- Windows you can do it with chocolatey ``choco install graphviz --head`` (admin cmd)
- Linux you can do it with brew ``sudo brew install graphviz --head``

This will also cause graphviz to update.

Make sure to update your graphviz path in the pythoncode or add it to your path variables.

    os.environ["PATH"] += os.pathsep + "C:\Program Files\Graphviz 2.44.1/bin/"

## Usage

The Python codes can be run and it creates the diagrams.

    python create_x

Examples and Instructions for creating own code can be found on https://diagrams.mingrammer.com/docs/getting-started/installation#quick-start.

Some Nodes with Icons can be found on the https://diagrams.mingrammer.com/docs/nodes/aws website. Custom nodes can be created by using Custom Node and giving it a path to a picture to use as Icon.

    ...
    from diagrams.custom import Custom
    ...
    Gstreamer = Custom("Gstreamer", "./customImages/gstreamer-logo.png")

The Custom images already used can be found in the Folder ``customImages``.

## Note

Used pictures should be put into the ``docs/attachment`` folder!



