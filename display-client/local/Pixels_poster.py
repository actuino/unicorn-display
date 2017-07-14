from random import randint
import time
import sys
sys.path.append("../classes" )
from AsyncWorker import AsyncWorker

Worker = None
Name = "Pixels_poster"
Receive_file_callback = None

def set_received(receive_file):
    global Receive_file_callback
    Receive_file_callback = receive_file
    
def my_func(unicorn, param):
    global Receive_file_callback,i
    n = randint(3,10)
    list_ = {'Type': 'P','Payload':{}, 'Channel': 'Pixels_poster'}
    for i in range(n):
        list_['Payload'][i] = [randint(1,7),randint(1,7),[255,0,0],randint(10000,3000000)]

    Receive_file_callback(list_)
    while i<11:
        time.sleep(1)
        i+=1
    i=0



def start(unicorn, param):
    global Worker
    if Worker:
        Worker.stop()
    Worker = AsyncWorker(my_func, unicorn, float(param))
    unicorn.clear()
    print "starting ",Name
    i=0
    Worker.start() 

def stop():
    global Worker
    if Worker:
        print "stopping ", Name
        Worker.stop()

