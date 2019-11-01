from pico2d import *
import random

class Sun():
    def __init__(self):
        global stop_y
        self.image = load_image('sun.png')
        self.x = 336 + (random.randint(0, 7) * 96)
        self.y = 700
        self.stop_y = -48 + (random.randint(1, 5) * 96)

    def update(self):
        self.y -= 5

    def draw(self):
        if(self.y < self.stop_y):
             self.image.draw(self.x , self.stop_y)
        else:
            self.image.draw(self.x , self.y)