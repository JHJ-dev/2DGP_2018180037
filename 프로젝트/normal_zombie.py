import game_framework
from pico2d import *
import random

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Normal_zombie:
    def __init__(self):
        self.image = load_image('image/walk_normal_zombie.png')
        self.x = 1200
        self.y = -25 + (random.randint(1, 5) * 96)
        self.velocity = -RUN_SPEED_PPS
        self.frame = 0


    def get_bb(self):
        return self.x - 40, self.y - 65, self.x + 40, self.y + 55


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.velocity * game_framework.frame_time
        if (self.x < 336):
            self.frame = 0
            self.velocity = 0


    def draw(self):
        self.image.clip_draw(int(self.frame) * 110, 0, 110, 133, self.x, self.y)
        draw_rectangle(*self.get_bb())