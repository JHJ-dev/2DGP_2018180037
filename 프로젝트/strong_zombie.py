from pico2d import *
import random

class Strong_zombie:
    def __init__(self):
        self.image = load_image('image/strong_zombie.png')
        self.x = random.randint (1152, 2000)
        self.y = -25 + (random.randint(1, 5) * 96)
        self.frame = random.randint(0, 7)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x -= 0.5

    def draw(self):
        if (self.x > 336):
            self.image.clip_draw(self.frame * 100, 0, 120, 133, self.x, self.y)
        else:
            self.image.draw(336, self.y)