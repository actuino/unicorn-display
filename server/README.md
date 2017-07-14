# Unicorn Display Server (Hub)
A NodeJs server for a connected RGB LED display.

## How to run on a Raspberry Pi (Docker):

`docker pull actuino/unicorn-server-armhf:latest`

`docker run -d -p 80:8080 actuino/unicorn-server-armhf:latest`

Open a browser and point it to your Pi IP address

## How to run on a Linux64 host (Docker):

`docker pull actuino/unicorn-server-linux64:latest`

`docker run -d -p 80:8080 actuino/unicorn-server-linux64:latest`

Open a browser and point it to your host IP address

## How to install manually :

(Todo)

## HTTP Server
    * Listens on port 8080 by default, routed to port 80 via docker
    * Serves index.html and editor.html

## WebSocket server
    * Via socket.IO
    
[Main Readme](../README.md)
    