import pico2d
import game_framework
import start_state

width, height  = 1152, 672

pico2d.open_canvas(width, height)
game_framework.run(start_state)
pico2d.close_canvas()