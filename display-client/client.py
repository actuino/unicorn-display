#!/usr/bin/env python

# Unicorn Jauge Display Client

import json
import os
import sys, getopt

# pip install socketIO-client  
# https://github.com/invisibleroads/socketIO-client
from socketIO_client import SocketIO, LoggingNamespace

current_page = 0;



# The socker server Hostname
DISPLAY_SERVER_HOST = 'localhost'
if 'DISPLAY_SERVER_HOST' in os.environ:
    DISPLAY_SERVER_HOST = os.environ['DISPLAY_SERVER_HOST']
    
# The socker server Port
DISPLAY_SERVER_PORT = 80
if 'DISPLAY_SERVER_PORT' in os.environ:
    DISPLAY_SERVER_PORT = os.environ['DISPLAY_SERVER_PORT']

# The Physical display name
DISPLAY_NAME = 'Astra' # Default unicorn name http://www.myangelcardreadings.com/unicornnames.html
# TODO : random unicorn name according to serial.
if 'DISPLAY_NAME' in os.environ:
    DISPLAY_NAME = os.environ['DISPLAY_NAME']

CONFIG_FILE_NAME = 'res/config.json'
if 'CONFIG_FILE_NAME' in os.environ:
    CONFIG_FILE_NAME = os.environ['CONFIG_FILE_NAME']
   
   
import unicorndisplay
    
def main(argv):
    global CONFIG_FILE_NAME
    try:
        opts, args = getopt.getopt(argv,"hc:",["help","config="])
    except getopt.GetoptError:
        print 'client.py -c <configfile> '
        sys.exit(2)
    for opt, arg in opts:
          if opt in ("-h", "--help"):
             print 'client.py -c <configfile> '
             sys.exit()
          elif opt in ("-c", "--config"):
             CONFIG_FILE_NAME = arg
    print 'Config file is "', CONFIG_FILE_NAME

    unicorndisplay.init(CONFIG_FILE_NAME)
    
    
if __name__ == "__main__":
   main(sys.argv[1:])

# From http://raspberrypi.stackexchange.com/questions/2086/how-do-i-get-the-serial-number
def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
  return cpuserial

def on_connect():
    print "Connected"
    socketIO.emit('name','{"Serial":"'+getserial()+'", "Name":"'+DISPLAY_NAME+'"}')    

def on_file(*args):
    unicorndisplay.receive_file(args[0])
    
def send_current_page():
    page = {'Page':current_page,'Serial':getserial(),'Name':DISPLAY_NAME,'Channel':unicorndisplay.get_current_channel()}
    socketIO.emit('page',json.dumps(page)) 
    
def on_command(*args):
    global current_page
    try:
        # ? message for us ?
        print "receive command: ",args[0]["Command"]
        if DISPLAY_NAME != args[0]["Name"]:
            print "Ignored Command"
            return
        command = args[0]["Command"]
        if command == "NextPage" or command == 'LeftGesture':
            current_page = unicorndisplay.next_page()
            send_current_page()
            #socketIO.emit('page','{"Page":"'+str(current_page)+'","Serial":"'+getserial()+'", "Name":"'+DISPLAY_NAME+'"}')  
        elif command == "PreviousPage" or command == 'RightGesture':
            current_page = unicorndisplay.previous_page()
            send_current_page()
            #socketIO.emit('page','{"Page":"'+str(current_page)+'","Serial":"'+getserial()+'", "Name":"'+DISPLAY_NAME+'"}')  
        else:
            print 'Unknown Command'
        
        
    except  Exception as e:
        s = str(e)
        print "Bad message"  ,s   
    

print DISPLAY_NAME,getserial(),"Connecting to",DISPLAY_SERVER_HOST, DISPLAY_SERVER_PORT
socketIO = SocketIO(DISPLAY_SERVER_HOST, DISPLAY_SERVER_PORT)

socketIO.on('connect', on_connect)
socketIO.on('file', on_file)
socketIO.on('command', on_command)

send_current_page()

# TODO : Manage exceptions and reconnect
while 1:
    socketIO.wait(60)
    socketIO.emit('ping')

