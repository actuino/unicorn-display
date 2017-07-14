

__version__ = '0.0.1'




def init():
    print "init"
    
def set_my_pixels_id(payload):
    print payload
    
def show_json(json):
    type=json['Type']
    if type == 'StaticId':
        print 'StaticId'
    elif type == 'Static' :
        print 'Static'
    else: 
        print 'none';
    
init()