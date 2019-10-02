from pico2d import *

open_canvas(1280, 720)
map = load_image('map.png')
character = load_image('peashooter.png')

map.draw_now(640, 360)
character.draw_now(300, 100)

