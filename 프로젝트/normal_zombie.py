import game_framework
from pico2d import *
from bullet import Bullet
import random

import game_world

# Zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Normal_zombie:
    def __init__(self):
        self.image = load_image('image/walk_normal_zombie.png')
        self.x = 1200
        self.y = -25 + (random.randint(1, 5) * 96)
        self.font = load_font('ENCR10B.TTF', 16)
        self.velocity = 0
        self.frame = 0

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.velocity -= RUN_SPEED_PPS
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
        self.x += self.velocity * game_framework.frame_time

    def draw(self):
        if (self.x > 336):
            self.image.clip_draw(self.frame * 110, 0, 110, 133, self.x, self.y)
        else:
            self.image.draw(336, self.y)


