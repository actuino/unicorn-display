import json
import time, math
import sys
sys.path.append("classes" )
from AsyncWorker import AsyncWorker
import autoscan
import os.path



try:
    import unicornhat as unicorn
except ImportError:
    exit("This library requires the Unicorn Hat module\nInstall with: sudo pip install unicornhat")

__version__ = '0.0.3'

payload_worker = None
effect_worker = []
local_worker = None
pixels_list = []
radar_json = 0
frame = 0
pixels = []
current_local = ''
command_module = None
'''first=data['Payload'][0][0]
data['Payload'][0].remove(first)
data['Payload'][0].append(first)'''




def init(config_file_name=''):
    global width, height, total_pages, pages, current_page, palette, current_channel
    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(0)
    unicorn.brightness(0.5)
    current_page = 0
    current_channel = ["default","startup",""]
    width,height=unicorn.get_shape()
    with open('res/colors.json') as json_data:
        palette = json.load(json_data)
        
    if not os.path.isfile(config_file_name):
        config_file_name = 'res/config.default.json'
        
    with open(config_file_name) as config:
        data = json.load(config)
        pages = data["Pages"]
        total_pages = len(pages)
        print "Unicorn started"
        print "there is ",total_pages," pages"
        set_autoscan(data["Autoscan"])
        

def stop_payload_worker():
    global payload_worker
    if payload_worker:
        payload_worker.stop()

def stop_page_workers():
    global local_worker, effect_worker
    if effect_worker:
        print len(effect_worker), " workers"
        for i in range(len(effect_worker)):
            print "stop worker",i
            effect_worker[i].stop()
        effect_worker = []
    if local_worker:
        local_worker.stop()

def set_autoscan(value):
    if value > 0:
        #next_page()
        autoscan.start(next_page,value)
    else:
        with open('res/startgif.json') as start:
            show_json(json.load(start))
        autoscan.stop()

    
def set_my_pixels_id(payload):
    global width,height, palette
    for x in range(width): #8
        for y in range(height): #4 or 8
            my_id=payload[y][x]
            #print "t", str(my_id)
            r,g,b=palette[str(my_id)]
            unicorn.set_pixel(x, y, r, g, b)
    unicorn.show()

def set_my_pixels(payload):
  for x in range(width): #8
    for y in range(height): #4 or 8
      r,g,b=payload[y][x]
      unicorn.set_pixel(x, y, r, g, b)
  unicorn.show()

def radar_frame(frame):
    global width,height, palette, pixels
    for x in range(width): #8
        for y in range(height): #4 or 8
            my_id=frame[y][x]
            if my_id != 0:
                r,g,b=palette[str(my_id)]
                unicorn.set_pixel(x, y, r, g, b)
                pixels_list.append([x,y,1,r,g,b,int(round(time.time() * 1000))])
                for i in range(len(pixels)):
                        if pixels[i][1] == x and pixels[i][0] == y:
                            unicorn.set_pixel(x, y, 255, 0, 0)
                            pixels_list.append([x,y,1,255,0,0,int(round(time.time() * 1000)),2200])
                
def gif(data, param):
    if param == None:
        param = 1
    if 'frame' in data:
        if data['frame'] < len(data['Payload'])-1:
            data['frame'] += 1
        else:
            data['frame'] = 0
    else:
        data['frame'] = 0
    set_my_pixels_id(data['Payload'][data['frame']])
    time.sleep(float(param))

def set_gif(payload):
    global payload_worker
    payload_worker = AsyncWorker(gif,payload)
    payload_worker.start()

def receive_file(data):
    try:
        if "Channel" in data:
            
            with open("channels/"+data["Channel"]+".json","w+") as f:
                json.dump(data,f)
            if data["Channel"] == pages[current_page-1][0]:
                if current_page != 0:
                    show_json(data)
        else:
            print "File has no Channel"
    except:
        print "Data Error"


#x;y;taille;r;g;b
def pixel(Payload):
    global pixels_list
    unicorn.set_pixel(Payload[0],Payload[1],Payload[3],Payload[4],Payload[5])
    unicorn.show()
    pixels_list.append([Payload[0],Payload[1],Payload[2],Payload[3],Payload[4],Payload[5],int(round(time.time() * 1000))])
    

def estompe_calc(delta, value,a):
    if delta <= 0 :
        return value
    result = ((a-delta)*value)/a
    if result < 0:
        result = 0
    return int(round(result))
    
def estompe(etime, param):
    global pixels_list
    if etime == "":
        etime = 5000
    millis = time.time() * 1000
    erase = []
    for i in range(len(pixels_list)):
        delta = millis-pixels_list[i][6]
        if len(pixels_list[i])>7 :
            etimepixel=pixels_list[i][7]
        else:
            etimepixel = etime
        if delta < etimepixel-1:
            unicorn.set_pixel(pixels_list[i][0],pixels_list[i][1],estompe_calc(delta,pixels_list[i][3],etimepixel),estompe_calc(delta,pixels_list[i][4],etimepixel),estompe_calc(delta,pixels_list[i][5],etimepixel))
        else:
            erase.append(pixels_list[i])
    for item in erase:
        pixels_list.remove(item)
    unicorn.show()

def radar(nil, nil2):
    global radar_json, frame
    if radar_json == 0:
        with open ("res/radar.json") as d:
            radar_json = json.load(d)
    frame += 1
    if frame == len(radar_json['Payload']):
        frame = 0
    radar_frame(radar_json['Payload'][frame])
    
    
    time.sleep(0.04)
    


def show_json(json):
    stop_payload_worker()
    global pixels
    try:
        type=json['Type']
        
        if type == 'StaticId':
            print 'StaticId'
            set_my_pixels_id(json['Payload'])
        elif type == 'Static':
            set_my_pixels(json["Payload"])
            #worker = AsyncWorker(static_effect,json)
            #worker.start()
            print 'Static'
        elif type == 'GIF':
            set_gif(json)
            print 'GIF'
        elif type == 'p':
            pixel(json['Payload'])
            print 'pixel'
        elif type == 'P':
            pixels = json['Payload']
            print "Pixels"
        else: 
            print 'none';
    except Exception as e:
        s = str(e)
        print "Format error ", s
    

def start_local(func_name):
    global current_local, command_module, pages, current_page
    current_local = func_name
    if func_name == 'Pixels_poster':
        unicorn.clear()
        start_effect_worker('radar','')
        start_effect_worker('estompe',700)
    try:
        command_module = __import__("local.%s" % func_name, fromlist=["local"])
        try:
            command_module.set_received(receive_file)
        except:
            print "No receive file callback"
        command_module.start(unicorn, pages[current_page-1][2])
        print 'started local ', func_name
    except ImportError:
        print "error"

def stop_local():
    global current_local, command_module
    if current_local != '':
        try:
            command_module.stop()
            print 'stopped local ', current_local
        except Exception as e:
            s = str(e)
            print "can't stop it!!!" , s
        

def start_effect_worker(effect_name, args):
    print 'starting ', effect_name
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(effect_name)
    if not method:
        #raise NotImplementedError("Method %s not implemented" % method_name)
        method = estompe
    temp_worker = AsyncWorker(method,args)
    effect_worker.append(temp_worker)
    print len(effect_worker), " workers"
    effect_worker[len(effect_worker)-1].start()
        
def page_changed():
    global current_page,current_channel, pages, total_pages
    current_channel = pages[current_page-1]
    stop_page_workers()
    stop_payload_worker()
    stop_local()
    print ""
    print "**********"
    print "page ",current_page,"/", total_pages
    
    if  'Local' == pages[current_page-1][1]:
        print "local, ",pages[current_page-1][0]
        start_local(pages[current_page-1][0])
    elif "p" == pages[current_page-1][1]:
        print "pixels mod, ",pages[current_page-1][2]
        unicorn.clear()
        start_effect_worker(pages[current_page-1][2],'')
        
    elif "Radar" == pages[current_page-1][1]:
        print "radar"
        unicorn.clear()
        global payload_worker, effect_worker
        start_effect_worker('radar','')
        start_effect_worker('estompe',700)
        
    else:
        try:
            with open("channels/"+pages[current_page-1][0]+".json") as d:
                print "normal mod, ",pages[current_page-1][0]
                data = json.load(d)
                show_json(data)
        except:
            with open("res/No-channels.json") as d:
                print "Unknown channel ",pages[current_page-1][0]
                data = json.load(d)
                show_json(data)
    

    
def get_current_page():
    global current_page
    return current_page

def get_current_channel():
    global current_channel
    return current_channel


def next_page():
    global current_page, total_pages
    if current_page < total_pages:
        current_page = current_page + 1
    else:
        current_page = 1
    #print str(current_page)+"/"+str(total_pages)
    page_changed()
    return current_page

def previous_page():
    global current_page, total_pages
    if current_page > 1:
        current_page = current_page - 1
    else:
        current_page = total_pages
    #print str(current_page)+"/"+str(total_pages)
    page_changed()
    return current_page
    

#init()
