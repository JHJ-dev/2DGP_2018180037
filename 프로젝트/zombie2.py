from pico2d import *
import random

class Zombie:
    def __init__(self):
        self.walk2 = load_image('walk2.png')
        self.x = random.randint (1152, 2000)
        self.y = -25 + (random.randint(1, 5) * 96)
        self.frame = random.randint(0, 7)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x -= 0.5

    def draw(self):
        if (self.x > 336):
            self.walk2.clip_draw(self.frame * 100, 0, 120, 133, self.x, self.y)
        else:
            self.walk2.draw(336, self.y)