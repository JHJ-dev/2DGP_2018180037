from pico2d import *
import random

mapx_array = [370, 468, 565, 665, 763, 865, 963, 1060, 1170]
mapy_array = [265, 273, 395, 515, 630]

class Sun():
    def __init__(self):
        self.image = load_image('resource.png')
        self.x = random.randint(315, 1230)
        self.y = random.randint(100, 690)
        self.speed = 2
        self.stop = self.random_sunY()

    def update(self):
        if self.image_rect.centery < self.stop:
            self.image_rect.centery += self.speed
