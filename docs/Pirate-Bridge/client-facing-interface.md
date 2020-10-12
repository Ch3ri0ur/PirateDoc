# Client API

The Pirate-Bridge provides a set of endpoints:

| Endpoint       | Request type | Function                    |
| -------------- | ------------ | --------------------------- |
| /              | GET          | serves website              |
| /stream        | GET          | stream of variable data     |
| /getconfig     | GET          | variable meta data          |
| /conf          | POST         | updates a variable          |
| /configupdates | GET          | stream of changes via /conf |

In the following sections these endpoints are further explained.

## Datastream
GET /stream

Behind this Endpoint a Server-Sent-Event stream is served. On this stream "message" events are provided. Each message has an data element attached. This element is a JSON encoded Object. In it is a list of Timestamp, Variable objects pairs.

Stream messages are sent to each client with an 16 ms interval to enable update rates of 60 Hz.

```
    event: message
    data: JSON.String

    event: message
    data: JSON.String
```

Here an example data object can be seen (first abstract then concrete)

``` JSON
{
    timestamp: {
        id1: value,
        id2: value,
    },
    "124252245635": {
        "2": 3203,
        "3": 123.1,
    },
}


```

## Configuration

GET /getconfig

The config endpoint provides a JSON object, in which the current project state and meta data is provided. 
There are three major components:

* clientsend_config
* arduinosend_config
* arduinoDatatypeSizes

### clientsend_config

This configuration describes the variables which the Bridge can send to the client. For each variable the name, type, scale and optionally the unit are ordered under the corresponding ID. These IDs are provided automatically in order of the declaration in the Arduino code. 

### arduinosend_config

Under the this object all the data the Bridge can send to the Arduino is listed. In addition to name and type, the current value is stored under default and a min and max values are provided too.

Values of the string type are handled a little differently: Instead of providing a min or max value the max size is saved in the max value.

### arduinoDatatypeSizes

Here the byte size of the base data types of the Arduino controller are listed to ensure that values that are sent to the arduino have the correct size and data is not corrupted. 


Example:

``` JSON
{
    "clientsend_config": {
        id_string: { "name": name_string, "type": type_string, "scale": scale_string_containing[unit_string] },
        "1": { "name": "Target Value", "type": "F", "scale": "Height in [cm]" },
        "2": { "name": "PID", "type": "F", "scale": "PID Values" }
    },
    "arduinosend_config": {
        id: { "name": name_string, "type": type_string, "default": current_value, "max": max_value, "min": min_value },
        "1": { "name": "Setpoint", "type": "F", "default": 100, "max": 1000, "min": 0 },
        "2": { "name": "kp", "type": "F", "default": 4.97, "max": 5, "min": 0 }
    },
    "arduinoDatatypeSizes": { "I": 2, "U": 2, "L": 4, "u": 4, "F": 4, "D": 4, "B": 1, "W": 2, "b": 1, "C": 1, "S": 53 }
}
```


## set Variable 

POST /conf

Exposed variables can be changed with a POST request to the /conf endpoint. Here the data is also to be structured in JSON. An object with id, value pairs is expected. Each conf is to be labeled with a UUID

Example:

``` JSON
{
    "uuid": uuid,
    "data": {
        id_string: value,
        id_string: value,
        }
}
```

## Config update Stream

GET /configUpdates

Under this endpoint another stream is provided, in which all the updates triggered via a POST request to /conf are reflected to all clients together with the uuid connected to that change.

``` JSON
event: message
data: {
    "uuid": uuid,
    "data": {
        "id": id_string, 
        "value": value
        }
    }

```

In addition a keep alive message ":keepalive" is sent every 15 seconds to keep the connection alive. It would otherwise disconnect after 90 seconds.

