from pico2d import *
import game_world
from bullet import *
import random

class Peashooter:
    def __init__(self):
        self.image = load_image('image/peashooter.png')
        self.x = 400
        self.y = -25 + (random.randint(1, 5) * 96)
        self.timer = 0.0

    def shoot_bullet(self):
        bullet = Bullet(self.x, self.y)
        game_world.add_object(bullet, 1)

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
