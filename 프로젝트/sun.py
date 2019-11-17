from pico2d import *
import game_framework
import random

class Sun():
    def __init__(self):
        global stop_y
        self.image = load_image('image/sun.png')
        self.x, self.y = 336 + (random.randint(0, 7) * 96), 700
        self.stop_y = -48 + (random.randint(1, 5) * 96)
        self.fall_speed = 100

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

    def draw(self):
        if(self.y < self.stop_y):
             self.image.draw(self.x , self.stop_y)
        else:
            self.image.draw(self.x , self.y)