from random import randint
import time
import sys
sys.path.append("../classes" )
from AsyncWorker import AsyncWorker

Worker = None
Name = "Snake"
snakes = [[randint(0,7),randint(0,7),randint(0,3),[255,0,0]],[randint(0,7),randint(0,7),randint(0,3),[0,255,0]],[randint(0,7),randint(0,7),randint(0,3),[0,0,255]]]

def my_func(unicorn, param=1):
    global snakes
    for i in range(3):
        unicorn.set_pixel(snakes[i][0],snakes[i][1],snakes[i][3][0],snakes[i][3][1],snakes[i][3][2])
    turn()
    unicorn.show()
    time.sleep(param)

def turn():
    global snakes
    for i in range(3):
        n = randint(1,10)
        if n ==9:
            snakes[i][2]+=1
            snakes[i][2] = snakes[i][2]%4
        elif n == 10:
            snakes[i][2]-=1
            snakes[i][2] = snakes[i][2]%4

        if snakes[i][2] == 0:
            snakes[i][0]+=1
        elif snakes[i][2] == 1:
            snakes[i][1]+=1
        elif snakes[i][2] == 2:
            snakes[i][0]-=1
        else:
            snakes[i][1]-=1
        snakes[i][0] = snakes[i][0]%8
        snakes[i][1] = snakes[i][1]%8

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

