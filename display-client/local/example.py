import time
import sys
sys.path.append("../classes" )
from AsyncWorker import AsyncWorker

Worker = None

# name of your plugin
Name = "Example"


################################
# use this only if you want to send a file to the unicorn display script
Receive_file_callback = None

def set_received(receive_file):
    global Receive_file_callback
    Receive_file_callback = receive_file
# use like this:
def a():
     global Receive_file_callback
     Receive_file_callback(my_file) 
################################

# put your code here, it will be executed in loop 
# don't change the function name
def my_func(unicorn, param):
    unicorn.set_pixel(5,5,0,0,255)
    unicorn.show()
    time.sleep(param)
    
# you can create other functions


# you don't need to change this
def start(unicorn, param):
    global Worker
    if Worker:
        Worker.stop()
    Worker = AsyncWorker(my_func, unicorn, float(param))
    unicorn.clear()
    print "starting ",Name
    Worker.start() 

# and this one too
def stop():
    global Worker
    if Worker:
        print "stopping ", Name
        Worker.stop()

