from random import choice

colors = ["#141616", "#18373c", "#35585e", "#be8579", "#bab9ce"]


class Particle(object):

    def __init__(self):
        self.x = random(width)
        self.y = random(height)
        self.tamanho = 30
        self.direcao = random(TAU)
        self.color = choice(colors)

    def atualiza(self):
        self.direcao += random(-0.5, 0.5)
        self.x = self.x + cos(self.direcao) * random(0.1, 5)
        self.y = self.y + sin(self.direcao) * random(0.1, 5)

        self.tamanho -= 1
        
    def desenha(self):
        if self.tamanho < 0:
            return
        stroke(choice(colors))
        fill(red(self.color), green(self.color), blue(self.color))
        ellipse(self.x, self.y, self.tamanho, self.tamanho)

particles = []
num_particles = 3200

def setup():
    global particle
    background(27)
    size(1800, 1920)
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
