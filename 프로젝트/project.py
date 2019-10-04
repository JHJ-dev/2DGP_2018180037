from pico2d import *

width, height = 1280, 720

open_canvas(width, height)
map = load_image('map.png')
character = load_image('peashooter.png')

running = True
frame = 0

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

while running:
    clear_canvas()
    map.draw(width//2, height//2)
    character.draw(300, 100)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    
close_canvas()
