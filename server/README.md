# Unicorn Display Server
A NodeJs server for a connected RGB LED display.

## How to run on a Raspberry Pi :
    * docker pull actuino/unicorn-display-server:1
    * docker run -d -p 80:80 actuino/unicorn-display-server:1

## HTTP Server
    * Listens on port 80
    * Serves index.html and editor.html

## WebSocket server
    * Via socket.IO
    
    