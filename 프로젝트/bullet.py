from pico2d import *
import game_world

class Bullet:
    def __init__(self):
        self.image = load_image('image/bullet.png')

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        self.x += 3

    def draw(self):
        self.image.draw(self.x, self.y)