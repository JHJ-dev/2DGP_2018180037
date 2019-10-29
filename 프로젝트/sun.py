from pico2d import *
import random

class Sun():
    global timer
    def __init__(self):
        global stop_y
        self.image = load_image('light.png')
        self.i = random.randint(0, 7)
        self.j = random.randint(1, 5)
        self.x = 336 + (self.i * 96)
        self.y = random.randint(672, 3000)
        self.stop_y = -48 + (self.j * 96)
        self.speed = 1

    def update(self):
        self.y -= self.speed

    def draw(self):
        if(self.y < self.stop_y):
             self.image.draw(self.x , self.stop_y)
        else:
            self.image.draw(self.x , self.y)
