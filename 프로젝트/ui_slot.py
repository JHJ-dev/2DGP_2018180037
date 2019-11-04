from pico2d import *

class Ui_slot:
    def __init__(self):
        self.image = load_image('image/ui_slot.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(123, 629)
