from pico2d import *
from bullet import Bullet
import random

class Normal_zombie:
    def __init__(self):
        self.image = load_image('image/walk_normal_zombie.png')
        self.x = 1200
        self.y = -25 + (random.randint(1, 5) * 96)
        self.velocity = 3
        self.frame = 0

    def get_bb(self):
        return self.x - 40, self.y - 65, self.x + 40, self.y + 55

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x -= self.velocity
        if (self.x == 336):
            self.frame = 0
            self.velocity = 0

    def draw(self):
        self.image.clip_draw(self.frame * 110, 0, 110, 133, self.x, self.y)
        draw_rectangle(*self.get_bb())