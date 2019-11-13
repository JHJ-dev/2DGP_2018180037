from pico2d import *
from bullet import Bullet
import random

#

import game_world

class Normal_zombie:
    def __init__(self):
        self.image = load_image('image/walk_normal_zombie.png')
        self.x = 1200
        self.y = -25 + (random.randint(1, 5) * 96)
        self.velocity = 0
        self.frame = 0

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x -= 3
        delay(0.06)

    def draw(self):
        if (self.x > 336):
            self.image.clip_draw(self.frame * 110, 0, 110, 133, self.x, self.y)
        else:
            self.image.draw(336, self.y)


