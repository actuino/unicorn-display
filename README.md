# unicorn-display
A real-time RGB LED display for the Raspberry Pi.

## Hardware

* A Raspberry Pi Zero with Raspbian
* A [Unicorn pHAT or HAT from @Pimoroni](https://shop.pimoroni.com/products/unicorn-phat)

## Fast setup with Docker

* Install Docker Engine : `curl -sSL get.docker.com |sh`
* See the Readmes of both [display-client](display-client/README.md) and [server](server/README.md) (Node.Js Hub). 
* Install and run at least one of each (same Pi or not)

* If you want to know more about Docker and the Pi, check [5 things about Docker on Raspberry Pi](http://blog.alexellis.io/5-things-docker-rpi/) from Alex Ellis

## Manual install

TODO

## Test the thing
* Open a browser and point it to the IP of the display server.
* "Next" and "Previous" buttons will increment and decrement a counter
* "Visual Editor link" opens an editor. Select a color, paint the grid, then click "Send" to update the Physical Display

![](https://raw.githubusercontent.com/actuino/unicorn-display/master/res/unicorn-editor.png)

## Flow for the Basic Demo, all on a Pi
![](https://raw.githubusercontent.com/actuino/unicorn-display/master/res/unicorn-flow1.png)

## Flow with an online Node JS Hub
Several config are possible.

![](https://raw.githubusercontent.com/actuino/unicorn-display/master/res/unicorn-flow2.png)

## More info

Blog post with a [Quick Demo Video](http://www.actuino.fr/raspi/minecraft-raspberry.html)
(Please leave comments and questions over on our blog)

If you want to replicate the full Demo with Minecraft, you'll need some more directions.
See [Minecraft Demo how-to](Minecraft/readme.md).

Some more [details about the stack](doc/stack.md)

## Roadmap

* Post doc about communication protocol
* Add data providers code and demos
* Add real world use cases


Follow us on Twitter [@Actuino](https://twitter.com/actuino)

Our Blog [Http://www.actuino.fr/](http://www.actuino.fr)
