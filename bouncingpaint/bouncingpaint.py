# Author: jvfe
# Mostly adapted from The Nature of Code
# 'Gravity and wind' video
# https://www.youtube.com/watch?v=Uibl0UE4VH8

from pyp5js import *

class Mover:
    
    def __init__(self, x, y):
        
        self.pos = createVector(x, y)
        self.vel = createVector(0, 0)
        self.acc = createVector(0, 0)
        self.r = random(2, 16)
        
    def addforce(self, force):
        
        self.acc.add(force)
        
    def update(self):
        
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.set(0, 0)
        
    def edges(self):
        
        if self.pos.y >= height - self.r:
            self.pos.y = height - self.r
            self.vel.y = self.vel.y * -1
        if self.pos.x >= width - self.r:
            self.pos.x = width - self.r
            self.vel.x = self.vel.x * -1
        elif self.pos.x <= self.r:
            self.pos.x = self.r
            self.vel.x = self.vel.x * -1
        
    def show(self):
        
        stroke(255)
        strokeWeight(random(0, 3))
        fill(random(255), random(255), random(255))
        ellipse(self.pos.x, self.pos.y, self.r * 2)
        self.r = random(2, 16)
        
mover = []        
def setup():
    
      createCanvas(400, 400)
      background(0)
      mover.append(Mover(200, 0))

      
def draw():
    
      gravity = createVector(0, 0.2);
      mover[0].addforce(gravity)
      mover[0].edges()
      mover[0].update()
      mover[0].show()
      
      if mouseIsPressed:
          wind = createVector(0.1, 0)
          mover[0].addforce(wind) 
     