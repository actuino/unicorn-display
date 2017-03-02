# Unicorn Display Client
The Python client, must run on the Pi with the Unicorn pHAT or HAT.

## How to run on a Raspberry Pi (Docker) :

`docker pull actuino/unicorn-display-client:1`
`docker run --privileged -e DISPLAY_SERVER_HOST=192.168.7.3 actuino/unicorn-display-client:1`

(replace 192.168.7.3 by the IP of the display server, same Pi or not)

A default scheme is displayed. Send commands from the server to update.

## How to run on a Raspberry Pi (manual install) :

### Install

* Clone the repo and enter the client directory
  `git clone https://github.com/actuino/unicorn-display.git; cd unicorn-display/display-client`
* Install Python 2.7 and PIP if needed
  `apt-get update; apt-get install python-dev python-pip`
* Install the [Unicornhat Library](https://github.com/pimoroni/unicorn-hat)
  pip should work : `pip install unicornhat`
* Install socketIO-client
  `pip install socketIO-client`
* Alternatively, you can install both pip requirements in one shot with 
  `pip install -r requirements.txt`
      
### Setup

* Set the environnement variables DISPLAY_SERVER_HOST and DISPLAY_SERVER_PORT (defaults to 80) to point to your display server
  `export DISPLAY_SERVER_HOST='ip.of.display.server'`
  (replacing ip.of.display.server with the actual ip of the display server)
      
### Run

* python client.py
  A default scheme is displayed. Send commands from the server to update.
  Some logs will be printed on the console.