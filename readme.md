# PirAtE Documentation

The PirAtE Documentation is done with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). It converts Markdown files to a static Website, which can be used as Project Documentation.

Our static Project Documentation for PirAtE can be found under https://ch3ri0ur.github.io/piratedocs/.

The Documentation Builds it self on the Github, if changes were made.


## Run mkdocs Local

Optionally create a virtual environment.

    python -m venv venv

Activate with:

    ./venv/Scripts/activate

A Local installation for the compiling is done with Python. The following Python Programms/Plugins are needed:

    pip install -r requirements.txt

Now you can just run MkDocs and Display the Website in the Own Browser.

    mkdocs serve

It will update each time automatically when changing files.

## Miscellaneous

The Folder Misc Contains some Formatting Examples and some Formatting Tests we have done.

## Diagramms

How to create the Diagramms can be found [here](createDiagram/readme.md).