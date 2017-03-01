import time
import unicornhat as unicorn
import json
from socketIO_client import SocketIO, LoggingNamespace

# The socker server Hostname
DISPLAY_SERVER_HOST = 'localhost'
# The socker server Port
DISPLAY_SERVER_PORT = 80


unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width, height = unicorn.get_shape()

def set_my_pixels(payload):
  for x in range(width): #8
    for y in range(height): #4 or 8
      r,g,b=payload[y][x]
      unicorn.set_pixel(x, y, r, g, b)

def set_my_pixels_id(payload):
    with open('colors.json') as json_data:
        id_list = json.load(json_data)
    for x in range(width): #8
        for y in range(height): #4 or 8
            my_id = payload[y][x]
            r, g, b = id_list[str(my_id)]
            unicorn.set_pixel(x, y, r, g, b)
    unicorn.show()
    
def on_file(*args):
    if args[0]["Type"] == "Static":
        set_my_pixels(args[0]["Payload"])
    elif args[0]["Type"] == "StaticId":
        set_my_pixels_id(args[0]["Payload"])
    else:
        print "Unknown Type"
    
def start():
    with open('start.json') as json_data:
        d=json.load(json_data)
        set_my_pixels_id(d["Payload"])

start()


with SocketIO(DISPLAY_SERVER_HOST, DISPLAY_SERVER_PORT) as socketIO:
    socketIO.on('file', on_file)
    socketIO.wait()          