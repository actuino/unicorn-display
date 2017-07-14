from random import randint
import time
import sys
sys.path.append("../classes" )
from AsyncWorker import AsyncWorker

Worker = None
Name = "alea"


def my_func(unicorn, param):
    unicorn.set_pixel(randint(0,7),randint(0,7),randint(0,255),randint(0,255),randint(0,255))
    unicorn.show()
    time.sleep(param)
    

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
