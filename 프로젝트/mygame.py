import game_framework
import pico2d

width, height  = 1152, 672

import start_state

pico2d.open_canvas(width, height)
game_framework.run(start_state)
pico2d.close_canvas()