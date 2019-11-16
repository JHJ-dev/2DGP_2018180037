from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('image/background.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1152//2, 672//2)
