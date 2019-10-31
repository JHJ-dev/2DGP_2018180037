from pico2d import *
import game_framework
import title_state
import map
import sun
import zombie

name = "MainState"

Map = []
Resource =[]

def enter():
    global map
    pass

def exit():
    global map, sun, zombie
    del (map)
    del (sun)
    del (zombie)
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
    pass

def update():
    for sun in Resource:
        sun.update()
    for zombie in Monster:
        zombie.update()

def draw():
    clear_canvas()
    map.draw()
    for sun in Resource:
        sun.draw()
    for zombie in Monster:
        zombie.draw()
    update_canvas()
    delay(0.01)