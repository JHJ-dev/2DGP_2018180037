from pico2d import *
import random

class Zombie:
    def __init__(self):
        self.image = load_image('zombie1.png')
        j = random.randint(1, 5)
        self.x = 1152
        self.y = -38 + (j * 96)
        self.frame = random.randint(0, 7)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x -= 0.5

    def draw(self):
        if (self.x > 336):
            self.image.draw(self.x, self.y)
        else:
            self.image.draw(336, self.y)