from pico2d import *
import random

class Sun():
    def __init__(self):
        global stop_y
        self.image = load_image('light.png')
        i = random.randint(0, 7)
        j = random.randint(1, 5)
        self.x = 336 + (i * 96)
        self.y = 672
        stop_y = -48 + (j * 96)
        self.speed = 1

    def update(self):
        self.y -= self.speed

    def draw(self):
        global stop_y
        if(self.y < stop_y):
             self.image.draw(self.x , stop_y)
        else:
            self.image.draw(self.x , self.y)
