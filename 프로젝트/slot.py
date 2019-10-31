from pico2d import *

class Slot:
    def __init__(self):
        self.image = load_image('slot.png')

    def draw(self):
        self.image.draw(123, 629)
