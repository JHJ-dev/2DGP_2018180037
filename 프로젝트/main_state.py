from pico2d import *
import game_framework
#import game_world
import title_state
import random

import map
import slot
import peashooter_ui
import sun
import zombie1

name = "MainState"

Resource = []
Mob1 = []

sun_timer = 0.0
mob_timer = 0.0

def enter():
    global peashooter_ui
    Resource.append(sun.Sun())
    Mob1.append(zombie1.Zombie1())
    peashooter_ui = peashooter_ui.pea_ui()

def exit():
    pass

def update():
    global Resource, sun_timer, mob_timer
    for i in Resource:
        i.update()
    for i in Mob1:
        i.update()
    peashooter_ui.update()
    if(sun_timer > 1):
        Resource.append(sun.Sun())
        sun_timer = 0
    sun_timer += 0.01
    if(mob_timer > (random.randint(5, 10)) / 10):
        Mob1.append(zombie1.Zombie1())
        mob_timer = 0
    mob_timer += 0.01

def draw():
    clear_canvas()
    map.Map().draw()
    slot.Slot().draw()
    peashooter_ui().draw()
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