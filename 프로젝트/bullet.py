from pico2d import *
import game_world

class Bullet:
    def __init__(self, x, y):
        self.image = load_image('image/bullet.png')
        self.x = x
        self.y = y

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.x += 3

    def draw(self):
        self.image.draw(self.x, self.y)