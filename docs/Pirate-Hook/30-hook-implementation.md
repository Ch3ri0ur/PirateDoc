# Implementation

!!! note "Warning!"
    The function names have changed over the versions and can be different in old ones.

The low memory and time usage aspect are partly the reason, why many functions are just macros, that get optimized by the compiler.

!!! note "Note:"
    Functions mostly covered in [Getting Started](10-hook-getting-started.md)!

## Overview of Implementation

- Requirement: Simple to use

    - Only 3 needed Stages for the User

        1. Start Communication (Setup)
        2. Add Variables (Setup)
        3. Perform Send & Receive (Main Loop)

    - Default Configuration already in "PirAtE_Config.h"

- Requirement: Time Usage

    - No Active Waiting
    - Maximum Blocktime adjustable
    - Uses Macros for Send and Receive

- Requirement: Resource Usage

    - Uses Pointer on Variables
    - Mostly optimized with Macros and Defines

## Main functions

start

define vars
receive
send overloaded


send

recv

code

focus

hardcoded aspects




psoible modififcations
defines ifndef

debug
comtype func
baudrate
buffersize
serial functions
allowwdblocktime send
allow block on send
interval send

allowedblocktime recive
interval request





bugs
features
need to be done
missing


already for later
serial define
other comtype replacement
