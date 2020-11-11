from random import choice

darkercolors = ["#141616", "#18373c", "#35585e", "#be8579", "#bab9ce"]

class Particle(object):

    def __init__(self):
        self.x = random(width)
        self.y = random(height)
        self.tamanho = 30
        self.direcao = random(TAU)
        self.color = choice(darkercolors)
        self.alph = alpha(self.color)
        self.strok = 27

    def atualiza(self):
        self.direcao += random(-0.5, 0.5)
        self.x = self.x + cos(self.direcao) * random(0.1, 5)
        self.y = self.y + sin(self.direcao) * random(0.1, 5)

        self.tamanho -= 1
        self.alph -= 4
        self.strok += 10
        rotate(HALF_PI)
        
    def desenha(self):
        if self.tamanho < 0:
            return
        stroke(self.strok)
        fill(red(self.color), green(self.color), blue(self.color), self.alph)
        triangle(self.x, self.y, random(width), random(height), random(width), random(height))


particles = []
num_particles = 300

def setup():
    global particle
    background("#bab9ce")
    size(800, 820)
    for i in range(num_particles):
        particle = Particle()
        particles.append(particle)

def draw():
    for particle in particles:
        particle.atualiza()
        particle.desenha()
        
def keyPressed():
    if key == 's':
        saveFrame("###########.png")
