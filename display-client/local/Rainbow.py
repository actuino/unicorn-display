import math
import time
import sys
sys.path.append("../classes" )
from AsyncWorker import AsyncWorker

Worker = None
Name = "Rainbow"
i = 0.0
offset = 30
def my_func(unicorn, param):
    global i, offset
    i = i + 0.3
    for y in range(8):
            for x in range(8):
                    r = 0
                    g = 0
                    r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
                    g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
                    b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
                    r = max(0, min(255, r + offset))
                    g = max(0, min(255, g + offset))
                    b = max(0, min(255, b + offset))
                    unicorn.set_pixel(x,y,int(r),int(g),int(b))
    unicorn.show()
    time.sleep(0.01)
    

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

