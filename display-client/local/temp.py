#read in
#/sys/class/thermal/thermal_zone0/temp

import json

def red_temp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    data = file.read().rstrip() # remove trailing '\n' newline character.
    file.close()
    payload = json.dumps({ "temp": data })
    return payload