# Implementation
The flag is a website written in [React](https://reactjs.org/) a library for creating dynamic websites. This React client is based on a [CRA](https://create-react-app.dev/) template for [Typescript](https://www.typescriptlang.org/). A React project is structured into components which can be placed into each other. This helps encapsulating the different tasks. 

## Component Communication

These components can communicate with their children by passing variables called properties, "props", and their parents by passing callbacks as properties a method called "hoisting". With only these methods it would be quite tedious to pass variables to a neighboring component branch, requiring hoisting and subsequent "prop drilling" a pattern in which properties are passed on from child to child in order to reach the destination. To streamline this process it is possible to use either a state management library or implement this functionality. In this project the library [react-hookstore](https://github.com/jhonnymichel/react-hookstore) was used which is based on Reacts useState-hook. 

!!! note "useState"
    The useState-hook is a new state management method in React. When calling ```[state,setState] = useState(initialValue)``` the value and a setState function are created. If this function is called the component in which the useState was used is notified of the new state and rerenders.

With this library a similar "useStore" hook can be used to access the same variables, in multiple independent components without needing the mentioned "hoisting" and "prop drilling". 


## Layout

The general Layout of the webpage is:

* Header
* Content
    * Chart
    * Controls
    * Live Feed
* Footer

Both Header and Footer are static. The functionality of the client stems from the content component. It has 4 major sub components:

* The chart to display the current data
* The controls for influencing the Arduino
* and a live view of the project.

In addition a settings modal can be opened on top of the website.

## Startup

On load the content container queries the bridge for the configuration of the project it should display. Once the query returns the configuration is passed to the child components. These then can dynamically adapt their appearance depending on the amount of variables needed to be displayed or controlled and their configuration. 

## Chart

Spanning the top the most important feature of the client is displayed: the chart of the current information from the Arduino project. To draw the chart a library called [uPlot](https://github.com/leeoniya/uPlot) is used. This library was chosen, because it is a no frills, small bundle size, fast draw time ([benchmarks](https://github.com/leeoniya/uPlot#Performance)) kind of library. An alternative would have been a webGL based chart renderer, utilizing the GPU, but they are bigger, slower to start, harder to integrate and not as fully featured.

The Chart component has a set of tasks:

### Generating the Chart

On the first render or when the configuration is changed the component analyzes the configuration and creates data structures that can store the expected data and have the format the uPlot library needs for its charts. Once this is generated a new uPlot instance is generated with the desired configuration.

Because this is a charting application strings and chars are not supported. Support for these might come in a later release.

Additionally listeners are generated to watch for resizing events of the window, so that the chart always stretches the whole width of the window. 

### Source Data
In order to be modular this component also sources the Arduino data directly and registers for the SSE-Stream on "/stream". This creates a stream of events which the [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) runtime cyclicly processes. This cycle time is approximately 50 ms. If the chart were to be updated on the events directly multiple rerenders would be batched into a cycle of 50 ms at a minimum. To smooth out the experience the events themselves only store the received data in a queue to be processed when the chart is updated on a higher and regular interval.

### Update Chart
To allow for smooth animation the chart is not updated, when the stream events are processed, but on each redraw of the website. Each redraw a appropriate portion of the previously mentioned queue is used to update the chart. In normal conditions this results in frame times of sub 16 ms. When more points are displayed on screen this time gradually increases. In tests with 6 graphs and 5000 timestamps render times increased to around 50 ms. Which is equal to around 20 frames per second. This is still acceptable and even resulted in a smoother experience, because the plots moved at a slower pace.

!!! note "Amount of Timestamps"
    The amount of timestamps the chart plots can be set in the settings modal. Depending on this number a larger or smaller time frame is shown.

### Pause

To analyze or export a specific period the plotting can be paused. While it is paused the Data is still updated in the background but a snapshot is stored and displayed. During such a pause it is possible to utilize the charts full capability with zooming and value readouts on mouse hover. 

During a pause the export button is enabled.

### Export Data

When the export is triggered the snapshot is transposed, the column names are added and both are converted into a .csv compatible string. This string is then downloaded as a .csv file named "export.csv".

## Controls

The control section is located under the Chart. This components job is to display the current value of the control variables on the Arduino and to enable the client to send control messages back to the Arduino and modify these variables. For that the component has the following functions.

### Display Controls

The parent content container passes it the configuration received from the Pirate-Hook. The control container generates a list of sub components that each control a single variable. Depending on the data type of the variable to be controlled the control surface could be different, but currently only the number datatype is supported and represented by a slider. In the future text inputs can be used for the string and char data types.

Each of these sub components receives the id, name, data type, current value, min value and max value. With this it can display a suitable set of controls. 

### Send Control Requests

When the user changes the value by for instance dragging the slider updates get sent to the POST "/ctrl" endpoint on the Bridge. As to not overload the connection these updates get throttled. They can only occur every 700 ms and the last value ist sent too. With this the value where the user let go of the slider is sent but during sliding infrequent updates are sent too.

### Sync Control between Clients

To enable multiple users concurrently accessing the Arduino the controls need to be synchronized. When one user modifies the values and another user joins the session the current values should be displayed. When any user now changes a value this change should also be reflected on the controls of the other user.

This is achieved by listening to the SSE-Stream at the GET "/configUpdates" endpoint. Here all changes get broadcasted back to the clients. This does not achieve the desired effect yet, because the own client listens to its own changes echoed back at it. This would create a feed back loop. To avoid this each client sends a unique identifier, a UUIDv4, with the control messages. These unique identifiers are broadcasted back to all clients with the updates and the client from which the changes originated can ignore said changes. For all other clients the identifiers don't match and they update accordingly.

To get notified of variable changes this component registers at another SSE-Stream at the GET "/configUpdates" endpoint. Here all clients can listen to the rebroadcasted changes. The unique identifier here is used to ignore all updates that originate from the own client.

So that not every sub component needs to listen to the event stream only the control component listens to the stream and notifies the correct subcomponent via a callback it has registered.

## Settings

To change general settings an options button opens a modal, a overlay, can be opened. Currently the visibility of the graphs in the chart and the amount of timestamps can be set. This information is passed via "useStore" hooks, notifying the correct other components.

## Live View

To display the live stream broadcasted by the [Priate-Spyglass](../Pirate-Spyglass/00-spyglass.md) the [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) library provided by [janus-gateway](https://github.com/meetecho/janus-gateway) was adapted to work within a React project. Old dependencies where removed and a missing dependency was added. Furthermore the module needs to be exported to be usable within the React application.

With the library included a provided streaming example could be adopted to work without [jquery](http://www.jquery.com) and with React. This example has the following workflow:

1. On first render a new instance of the Janus client ist instantiated.
2. A session is automatically connected with the janus-gateway via the "/janus" endpoint.
3. With the session available the client can request a videostream over WebRTC from the gateway.
4. When the gateway opens the stream it is attached to a video element on the webpage.

While streaming the live view generates, depending on the source the gateway publishes, around 1 Mbps of traffic.


TODO WebRTC no longer Part using WebSockets
### WebRTC Primer

[[WebRTC]] is a open framework to enable real time peer-to-peer communication. It supports video, audio and data. To establish a WebRTC connection another signaling channel is needed to establish and manage the hight throughput connections. The high throughput channels are directly peer-to-peer. Establishing them is sadly not as straight forward as one might hope. To establish a connection both parties have to negotiate a way to navigate network boundaries, firewalls and NATs. This is normally done via STUN/ICE. These protocols fail sometimes on more complex networks and symmetric NATs, so as a last resort it is possible to relay the peer-to-peer connection via TURN over a relay server, kind of defeating the purpose of a peer-to-peer connection. 

The target network turned out, on first glance, to be of the complex variety and creates problems during negotiation a residential connection might not pose. These have as of writing not been resolved. Further investigation is necessary to enable this functionality on premise.



