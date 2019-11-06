from pico2d import *
import game_framework
import start_state

width, height  = 1152, 672

open_canvas(width, height, sync = True)
game_framework.run(start_state)
pico2d.close_canvas()