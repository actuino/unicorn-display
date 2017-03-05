# Command a physical LED display from within a Minecraft Virtual World

## What you'll need

* A Raspberry Pi Zero with Raspbian
* A [Unicorn pHAT or HAT from @Pimoroni](https://shop.pimoroni.com/products/unicorn-phat)
* A vanilla Minecraft client that supports Minecraft protocol versions 1.8 to 1.11
  (See below what client may work or not)

## The Video

Blog post with a [Quick Demo Video](http://www.actuino.fr/raspi/minecraft-raspberry.html)

(Please leave comments and questions over on our blog)

## The communication flow

![](https://raw.githubusercontent.com/actuino/unicorn-display/master/res/unicorn-minecraft.png)

## Setup options

You can install the components where and how you want.
The various dependencies are listed in the sources (requirements.txt, package.json).

However, Docker and the pre-built images we provide for the Pi render the experience plainless.

### Setup with Docker

* Install the Docker engine on the Pi `curl -sSL get.docker.com |sh`
* Pull the images
```
docker pull actuino/unicorn-display-client:1
docker pull actuino/unicorn-server-armhf:1
docker pull actuino/cuberite-webhooks-armhf:1
```
* Run the 3 components
```
docker run -d -p 80:80 actuino/unicorn-server-armhf:1
docker run --privileged -d -e DISPLAY_SERVER_HOST=192.168.7.3 actuino/unicorn-display-client:1
docker run -p 8080:8080 -p 25565:25565 actuino/cuberite-webhooks-armhf:1
```
(replace 192.168.7.3 by the actual IP of the Pi)

### Enjoy

* When running actuino/unicorn-display-client, a default scheme should appear on the physical display within a few seconds.
* After launching the Cuberite server, wait about 10 seconds.
* Connect your Minecraft client to `ip.of.the.pi:25565` 
* If you need to change the IP of the Unicorn Server (192.168.7.3 by default), use that command from Minecraft : `/changeaddress ip.of.unicorn.server`
* Craft ! You spawned on a platform above the world. Look around to find the Display artefact.

### Debug

Note that if Cuberite is running on a Pi Zero, it may be a little choppy.

* Point a brower to http://ip.of.the.pi/ and test the server/client flow.
* Run the cuberite image with `-it` flags, or attach to the running docker container: you'll see the log output of the server.
* Head over to our [Actuino blog post for help](http://www.actuino.fr/raspi/minecraft-raspberry.html).

## Compatible Minecraft clients

Microsoft released several incompatible versions of the Minecraft client (protocol as well as features differs).
The cuberite server supports Minecraft protocol versions 1.8 to 1.11. That is, the legacy Mojang clients, not the last Microsoft ones.

The best choice is to use a legacy Minecraft client: 
Classic edition, also known as Minecraft: Java edition, Minecraft for Windows or Minecraft for Linux.
(costs about $25)

The Minecraft Windows 10 edition is not compatible.
The Minecraft Pi edition is a stripped down version, not compatible either.

You may try http://wiki.vg/Client_List for alternative open source clients (not tested yet, tell us if you did!).


[Main Readme](../README.md)

[@Actuino](https://twitter.com/actuino)

Http://www.actuino.fr/
