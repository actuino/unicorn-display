from random import randint
import time
import sys
sys.path.append("../classes" )
from AsyncWorker import AsyncWorker

Worker = None
Name = "Filante"

def my_func(unicorn, param):
    r = randint(100,255)
    g = randint(100,255)
    b = randint(100,255)
    y = randint(0,7)
    for x in range(8):
        unicorn.set_pixel(x,y,r,g,b)
        if x >1:
            unicorn.set_pixel(x-2,y,0,0,0)
        if x >0:    
            unicorn.set_pixel(x-1,y,r/2,g/2,b/2)
        unicorn.show()
        time.sleep(0.1)

    for x in range(8):
        unicorn.set_pixel(7-x,y,r,g,b)
        if 7-x >-1:
            unicorn.set_pixel(7-x+2,y,0,0,0)
        unicorn.set_pixel(7-x+1,y,r/2,g/2,b/2)
        unicorn.show()
        time.sleep(0.1)


def start(unicorn, param):
    global Worker
    if Worker:
        Worker.stop()
    Worker = AsyncWorker(my_func, unicorn, float(param))
    unicorn.clear()
    print "starting ",Name
    Worker.start() 

def stop():
    global Worker
    if Worker:
        print "stopping ", Name
        Worker.stop()

