import time, datetime
import sys
sys.path.append("../classes" )
from AsyncWorker import AsyncWorker

Worker = None
Name = "Binary-clock"


def display_binary(unicorn,value, row, color):
	binary_str = "{0:8b}".format(value)
	for x in range(0, 8):
		if binary_str[x] == '1':
			unicorn.set_pixel(x, row, color[0], color[1], color[2])
		else:
			unicorn.set_pixel(x, row, 0, 0, 0)

def my_func(unicorn, param):
    t = datetime.datetime.now()
    display_binary(unicorn,t.hour, 0, (0, 255, 0))
    display_binary(unicorn,t.minute, 1, (0, 0, 255))
    display_binary(unicorn,t.second, 2, (255, 0, 0))
    unicorn.show();
    time.sleep(1)
    
    

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

