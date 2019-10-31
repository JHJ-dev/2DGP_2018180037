from pico2d import *
import random

class Zombie1:
    global z
    z = random.randint(0, 10)

    def __init__(self):
        self.walk1 = load_image('walk1.png')
        self.x = 1200
        self.y = -25 + (random.randint(1, 5) * 96)
        self.frame = random.randint(0, 7)

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x -= 1

    def draw(self):
        if (self.x > 336):
            self.walk1.clip_draw(self.frame * 110, 0, 110, 133, self.x, self.y)
        else:
            self.walk1.draw(336, self.y)