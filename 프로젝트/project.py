from pico2d import *
import random

width, height = 1280, 720

class Sunlight:
    def __init__(self):
        self.x, self.y = random.randint (365, 1180), 720
        self.frame = random.randint (0, 7)
        self.image = load_image ('resource.png')
        
    def update(self):
        self.y -= 5
        
    def draw(self):
        self.image.draw(self.x , self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass
    
open_canvas(width, height)
map = load_image('map.png')
resource = [Sunlight() for i in range(10)]

running = True

while running:
    handle_events()
    for sunlight in resource:
        sunlight.update()
    clear_canvas()
    map.draw(width//2, height//2)
    for sunlight in resource:
        sunlight.draw()
    update_canvas()
    delay(0.05)
    
close_canvas()
