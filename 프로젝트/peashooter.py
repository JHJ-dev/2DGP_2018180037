from pico2d import *
import game_world
import bullet
import random

class Peashooter:
    def __init__(self):
        self.image = load_image('image/peashooter.png')
        self.x = 400
        self.y = -25 + (random.randint(1, 5) * 96)
        self.timer = 0.0

    def shoot(self):
        Shoot = bullet.Bullet(self.x, self.y)
        game_world.add_object(Shoot, 1)
        print('SHOOT BALL')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
