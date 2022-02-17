# Requirements

The Spyglass component has a set of functional and non functional Requirements.

The following requirements are derived from the accepted overarching requirements approved by the customer.

## Functional Requirements

### See Experiment on Webpage

* It must be possible to integrate a live view of the experiment into a webpage.

### Automatically start on Bootup

* The solution needs to be able to start and broadcast without user input, when booting.


### Simple integration into existing Projects

* The solution should be easy to integrate into a existing webpage.


## Non-Functional Requirements

* The solution should to work with chrome, firefox and safari.
* The frontend must run stably for 3 hours.
* The video should run with more than 10 fps.
* The delay to display the information may not exceed two seconds.
* Multiple clients should be able to view the stream at the same time
* The image should be rotatable by 90°.
* The client must be usable with LTE.
* Should target Raspberry Pi OS 32-bit Buster.
  * Current project is based on Buster and video stack on Bullseye has breaking changes, see [[libcamera]]
