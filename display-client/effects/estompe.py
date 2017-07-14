import time
import sys
sys.path.append("../classes" )
from AsyncWorker import AsyncWorker
Worker = None

def my_estompe(unicorn, param):
    

def start(unicorn, param):
    global Worker
    if Worker:
        Worker.stop()
    Worker = AsyncWorker(my_estompe, unicorn, param)
    unicorn.clear();
    Worker.start() 

def stop():
    global Worker
    if Worker:
        Worker.stop()
    print "stopalea"
