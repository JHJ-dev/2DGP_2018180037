from pico2d import *
from bullet import Bullet
import random

class Normal_zombie:
    def __init__(self):
        self.x, self.y = 1200, -25 + (random.randint(1, 5) * 96)
        self.image = load_image('image/walk_normal_zombie.png')
        self.velocity = 1
        self.frame = 0

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x -= 1

    def draw(self):
        if (self.x < 336):
            self.velocity = 0
            self.frame = 0
        self.image.clip_draw(self.frame * 110, 0, 110, 133, self.x, self.y)
        draw_rectangle(*self.get_bb())