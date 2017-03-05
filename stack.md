# Unicorn Display - The software Stack

The software stack is pretty eclectic, but thanks to Docker on Armbian, all play well together.

* Docker on Raspbian
Docker allows to simplify the installation and setup of the components, and runs each one in a separate environment.
Each physical display client is a Docker container. The NodeJs server another one. Once our code is properly polished, it’s just a question of pulling the right Docker images to get all the demo running. It runs fine on the Pis (even the Zero) and renders complex architectures modular.
The Raspberry Pi Zero supports USB OTG and an « Ethernet over USB » mode. You can then power and network the Pi via a single USB cable.
* A NodeJs Server
It’s the hub that ties everything (but doesn’t do much on its own). It’s an HTTP and WebSocket server. The display connects via WebSocket and gets real-time events. Other clients can connect via WebSocket too and send commands to be broadcasted, or send HTTP POST Requests as well.
NodeJs seems like the way to go to get a simple Web and WebSocket server running without hassle.
* Some HTML/JS for a debug editor.
Jquery and Socket.Io did the job. The HTML and JS files are served by the NodeJs server. The client browser then connects via WebSocket.
* Some Python Code
The Unicorn Hat library is available as Python code, so we built upon that. We used the Python WebSocket Library socketIO-client.
* A Cuberite server
Cuberite is an alternative Minecraft server written in C. It’s way more efficient than the Java version, and ships with a full featured (and well documented) API. Server plugins can be written in Lua. In our case, a plugin allows to define reactive areas and maps them to a LED display. Each time a block in such an area changes, an event is fired and the LUA script posts an HTTP request to the NodeJs Server. Communication can be bidirectional: the Cuberite server can accept web hooks of sort.
* A legacy Minecraft client
No hack here, just the standard Java client on a Desktop PC. All the control/command logic is server-side.

[Main Readme](README.md)
