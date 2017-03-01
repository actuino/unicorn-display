# Unicorn Display Client
The Python client, must run on the Pi with the Unicorn pHAT or HAT.

## How to run on a Raspberry Pi (Docker) :
    * docker pull actuino/unicorn-display-client:1
    * docker run --privileged -e DISPLAY_SERVER_HOST=192.168.7.3 actuino/unicorn-display-client:1
      (replace 192.168.7.3 by the IP of the display server, same Pi or not)

A default scheme is displayed. Send commands from the server to update.

## How to run on a Raspberry Pi (manual install) :

(TODO)
    