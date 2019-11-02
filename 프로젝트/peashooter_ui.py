from pico2d import *

class pea_ui:
    def __init__(self):
        self.image = load_image('peashooter_ui.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 10
        delay(0.01)
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 70, 200, 629)