n = 0
c = 3
angle_coef = 137.5
start = 0
alphag = 50

def setup():
    size(800, 800)
    frameRate(10)

def draw():
    
    global n, c, start, angle_coef, alphag
    background(27)
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
                if alphag < 100:
                    alphag += 1
                else:
                    alphag = 50
                fill(0, hu, random(127, 255), alphag)
                noStroke()
                # stroke(hu, random(0, 127), random(127, 255))
                ellipse(x + tamanho, y + tamanho, 4, 4)
            
            rotate(n * 0.3)
            popMatrix()

        n += 5
        start += 5

        
def keyPressed():
    if key == 's':
        saveFrame("###########.png")
