add_library('oscP5')   # imports oscP5 lib
from collections import deque

oscP5 = None    # OSC server's global variable 
bass_freq = None
n = 0
c = 3
angle_coef = 137.5
start = 0
alphag = 50

synth_data = None

class MyOscListener(OscEventListener):
    
    @staticmethod
    def oscEvent(m):
        global synth_data    
        args = m.arguments()
        name = args[0]
        is_synth_message = all([
            m.addrPattern() == u'/s_new',
            name != u'startSound',
            name != u'makeSound',
            not str(name).startswith(u'play'),
        ])
        if not is_synth_message:
            return    
    
        synth_data = {
            u"name": args[0],
            u"id": args[1],
            u"add_action": args[2],
            u"target_id": args[3],            
        }
        
        offset = 4
        for i, value in enumerate(args[offset:]):
            if isinstance(value, unicode):
                synth_data[value] = args[offset + i + 1]
        
            
        # print(u"Processing: " + synth_data['name'] + u' - Frequency: ' + str(synth_data.get('freq', 0)))
        # synths_deque.appendleft(synth_data)
    
def stop():
    global oscP5
    oscP5.dispose()

def setup():
    global oscP5
    
    size(800, 800)
    # frameRate(10)
    
    oscP5 = OscP5(this, 12000) # create a new server runnint at 127.0.0.1 at port 12000
    
    oscP5.addListener(MyOscListener()) 
    loc = NetAddress('127.0.0.1', 12000)
    
def draw():
    
    global n, c, start, angle_coef, alphag, synth_data
    
    background(240)
    tamanho = 100
    
    for current_w in range(0, width , tamanho * 2):
        for current_h in range(0, height, tamanho * 2):
            pushMatrix()
            translate(current_w, current_h)
            for i in range(n):
                a = i * angle_coef
                r = c * sqrt(i)
                x = r * cos(a) 
                y = r * sin(a)
                hu = sin(start + i * 0.5)
                hu = map(hu, -1, 1, 0, 360)
                if alphag > 100:
                    alphag = 50
                elif synth_data is not None:
                    alphag = map(synth_data.get('freq', 0), 0, 400, 50, 255)
                fill(0, hu, random(127, 255), alphag)
                noStroke()
                # stroke(hu, random(0, 127), random(127, 255))
                ellipse(x + tamanho, y + tamanho, 4, 4)

            
            if synth_data is not None:    
                rotate(n * map(synth_data.get('amp',0), 0, 1, 0.1, 0.5))
            else:
                rotate(n * random(0.1, 0.5))
            popMatrix()

        n += 5
        start += 5

        
def keyPressed():
    if key == 's':
        saveFrame("###########.png")
