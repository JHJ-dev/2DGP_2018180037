from pico2d import *
import game_framework
#import game_world
import title_state
import random

import map
import slot
import sun
import zombie1

name = "MainState"

Resource = []
Mob1 = []

sun_timer = 0
mob_timer = 0

def enter():
    Resource.append(sun.Sun())
    Mob1.append(zombie1.Zombie1())
    pass

def exit():
    pass

def update():
    global Resource, sun_maker
    for i in Resource:
        i.update()
    for i in Mob1:
        i.update()
    if(sun_maker > 1):
        Resource.append(sun.Sun())
        sun_maker = 0
    sun_maker += 0.01
    pass

def draw():
    clear_canvas()
    map.Map().draw()
    slot.Slot().draw()
    for i in Resource:
        i.draw()
    for i in Mob1:
        i.draw()
    update_canvas()

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