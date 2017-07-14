import math

__version__ = '0.0.1'

def effect(data,params={}):
    #
    print "todo"

def static_effect(data,delta=20,div=10):
    global width, height
    #delta=20;
    #div=10;
    if 'frame' in data:
        if data['frame'] < 100*math.pi:
            data['frame'] += 1
        else:
            data['frame'] = 0
    else:
        data['frame'] = 0
    for x in range(width): #8
        for y in range(height): #4 or 8
            r,g,b=data['Payload'][y][x]
            r=int(round(r+delta*math.sin(data['frame']/div+x+y)))
            g=int(round(r+delta*math.sin(data['frame']/div+x+y)))
            b=int(round(r+delta*math.sin(data['frame']/div+x+y)))
            r=max(0,min(255,r))
            g=max(0,min(255,g))
            b=max(0,min(255,b))
            unicorn.set_pixel(x, y, r, g, b)
    unicorn.show()
    #time.sleep(0.1)

