import time
import sys
sys.path.append("classes" )
from AsyncWorker import AsyncWorker

__version__ = '0.0.1'

Worker = None

def autoscan(func, value):
    func()
    
    time.sleep(value)
    

def start(func,value):
    global Worker
    if Worker:
        Worker.stop()
    Worker = AsyncWorker(autoscan, func, value)
    Worker.start() 


def stop():
    if Worker:
        Worker.stop()
