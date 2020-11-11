add_library('oscP5')   # imports oscP5 lib

oscP5 = None    # OSC server's global variable 
bass_freq = None

def setup():
    size(900, 900)
    global oscP5
    
    oscP5 = OscP5(this, 12000) # create a new server runnint at 127.0.0.1 at port 12000
    
    oscP5.addListener(MyOscListener()) 
    loc = NetAddress('127.0.0.1', 12000)

def stop():
    global oscP5
    oscP5.dispose()

def draw():
  pass

class MyOscListener(OscEventListener):
    
    @staticmethod
    def oscEvent(m):   
        args = m.arguments()
        print(args)
        if str(args[0]) == 'bass':
            bass_freq = int(args[7])
            # print(bass_freq)
