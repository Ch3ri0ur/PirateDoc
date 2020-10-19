# Validation and Future Steps

In this section the initial requirements are measured against the current implementation.

## Functional Requirements

The proposed requirements are solved in this solution.

### See variables from Arduino Project

* With the chart component the variables that have been designated to be streamed are displayed. 
* The variable type is currently limited to only numbers and booleans.

### Change variables on Arduino Project

* The control component allows the user to change the variables on the Arduino which have been designated to be changeable.
* The variable type is currently limited to only numbers and booleans.

### Live-view of Arduino Project

* The live view can be started.
* The latency has been measured to be around 300 ms.
    * This measurement has been done by creating a feedback loop of a accurate timer on screen and filming that timer and displaying the output below. With careful placement of the camera multiple iterations could be captured. The loop time fluctuated but a full cycle time of around 300 ms could be measured over 5 cycles.
* This requirement has not been full met:
    * Because of limitations with WebRTC and NAT traversal the live view does not work reliably.

## Non-Functional Requirements

* The frontend must run stably for 3 hours.
    * In long term tests the frontend ran for more than 3 hours consistently.
* The delay to display the information may not exceed two seconds.
    * The delay of the graph has not been measured, but rough estimates place it well below two seconds.
    * The controls have been throttled as to not overwhelm the server. This introduces a latency of above 700 ms which is still acceptable.
    * The delay of the live view has been measured to be around 300 ms.
* The client must be usable with LTE.
    * The client has been tested with 
* It should be possible to support multiple different projects
    * The frontend is created dynamically and thus project independent.
* It should be possible to support multiple projects simultaneously 
    * The frontend does not yet support multiple simultaneous projects or project switching.
* The client should be a website.
    * The client is a website.
* A single Project should be implemented.
    * A mock project is implemented.
* It should be possible to export the measured data.
    * When the chart is paused, it is possible to download the data into a .csv file.
* The client should use the client API as specified.
    * The client communicates with the backend over the specified client API

## Shortcomings and Future Steps

The most important future steps include an implementation for managing and accessing multiple projects. Further steps include developing a more robust live view implementation and improving overall appearance of the website.