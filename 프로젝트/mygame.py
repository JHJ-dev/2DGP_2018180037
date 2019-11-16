from pico2d import *
import game_framework
import title_state

open_canvas(1152, 672)
game_framework.run(title_state)
pico2d.close_canvas()