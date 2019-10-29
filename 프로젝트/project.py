from pico2d import *
from sun import Sun

width, height = 1152, 672

open_canvas(width, height)
map = load_image('map.png')

Resource = [Sun() for i in range(10)]

running = True

while running:
    for sun in Resource:
        sun.update()
        
    clear_canvas()
    map.draw(width//2, height//2)
    for sun in Resource:
        sun.draw()
    update_canvas()
    delay(0.05)
    
close_canvas()
