# Architecture and Protocol

## Architecture

Each display client may be autonomous, but tries to connect to a display server.
It connects via websocket, and receives real-time events.

A server acts as a Hub that gathers all data and dispatches requests to the client(s).

The server can get data from a WebSocket connection as well as via HTTP POST requests.

(TODO: picture needed here)

## Server => Display client protocol

Each WebSocket message is a message string and a data payload.
The message string is 'file', and the data a simple json string,
Here is an example

```{ "Type": "StaticId",
"Payload" : [
	[1,6,0,0,0,0,6,1],
	[6,1,6,0,0,6,1,6],
	[0,6,1,6,6,1,6,0],
	[0,0,6,1,1,6,0,0],
	[0,0,6,1,1,6,0,0],
	[0,6,1,6,6,1,6,0],
	[6,1,6,0,0,6,1,6],
	[1,6,0,0,0,0,6,1]
]
}```

### Type "Static"

Payload is an 8 by 8 Array, with an (int) [r ,g ,b] color for each pixel.

Example with [static.json](display-client/static.json):

```{ "Type": "Static",
"Payload" : [
    [[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0]],
    [[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0]],
    [[0,255,0],[0,255,0],[0,255,0],[0,255,0],[0,255,0],[0,255,0],[0,255,0],[0,255,0]],
    [[0,0,255],[0,0,255],[0,0,255],[0,0,255],[0,0,255],[0,0,255],[0,0,255],[0,0,255]],
    [[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0]],
    [[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0]],
    [[0,255,0],[0,255,0],[0,255,0],[0,255,0],[0,255,0],[0,255,0],[0,255,0],[0,255,0]],
    [[0,0,255],[0,0,255],[0,0,255],[0,0,255],[0,0,255],[0,0,255],[0,0,255],[0,0,255]]
]
}```

### Type "StaticId"

This payload is more compact, as it uses a fixed color palette.
The dict with id => colors association is [colors.json](display-client/colors.json)
Payload is an 8 by 8 Array, with an (int) color id for each pixel.

Example with start.json :

```{ "Type": "StaticId",
"Payload" : [
	[1,6,0,0,0,0,6,1],
	[6,1,6,0,0,6,1,6],
	[0,6,1,6,6,1,6,0],
	[0,0,6,1,1,6,0,0],
	[0,0,6,1,1,6,0,0],
	[0,6,1,6,6,1,6,0],
	[6,1,6,0,0,6,1,6],
	[1,6,0,0,0,0,6,1]
]
}```


## Any => Server

Anything can send commands to a display server.
The data to send maybe a display payload, but must include more properties 

Channel :
... :

```
blabla
```

This data can be sent to the server via WebSocket or HTTP POST

### Via websocket

Event "file"
Data : a display Payload

```
blabla
```


#### code sample

##### Python

##### JavaScript


### Via HTTP POST

#### HTTP Endpoint

Post to /display/
The body of the request should be a properly formatted json string of a display payload.

#### code sample

##### Python

##### PHP


