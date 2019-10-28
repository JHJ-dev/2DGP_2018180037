from pico2d import *
import random

class Sun():
    def __init__(self):
        self.image = load_image('resource.png')
        self.x = random.randint(365, 1180)
        self.y = 720
        self.speed = 2

    def random(self):
        global random_Y
        random_Y = random.randint(0, 720)

    def update(self):
        self.y -= 5

    def draw(self):
        self.image.draw(self.x, self.y)
