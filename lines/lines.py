from pyp5js import *

colorarray = ['#ff00ff', '#ffff66', '#e50000', '#40e0d0', '#ffae19']

def setup():
    createCanvas(1080, 1920)
    
def draw():
    global colorarray
    background('#F5F5DC')
    
    tamanho = 20
    for x in range(0, width, tamanho):
        for y in range(0, height, tamanho):
            
            if random(1) > 0.5:
                x1, y1 = 0, 0
                x2, y2 = tamanho, tamanho
            else:
                x1, y1 = 0, tamanho
                x2, y2 = tamanho, 0
                
            line(x + x1, y + y1, x + x2, y + y2)
            stroke(random(colorarray))
            strokeWeight(random(5))
            
    noLoop()
    
    
