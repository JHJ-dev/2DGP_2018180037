from pico2d import *
import game_framework
import title_state

import map
import slot
import sun
import zombie1

name = "MainState"

Resource = []
Mob1 = []

sun_maker = 0
sun_remover = 0

def enter():
    global map, slot, sun, zombie1
    map = map.Map()
    slot = slot.Slot()
    sun = sun.Sun()
    zombie1 = zombie1.Zombie1

def exit():
    global map, slot, sun, zombie1
    del (map)
    del (slot)
    del (sun)
    del (zombie1)

def update():
    global Resource, sun_maker, sun_remover
    if(sun_maker > 3):
        Resource.append(sun)
        sun_maker = 0
    delay(0.01)
    sun_maker += 1
    pass

def draw():
    clear_canvas()
    map.draw()
    slot.draw()
    for i in Resource:
        i.draw()
    update_canvas()
    delay(0.05)

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