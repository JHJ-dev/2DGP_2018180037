from pico2d import *
import game_framework
#import game_world
import title_state
import random

import background
import ui_slot
import peashooter_ui
import sun
import peashooter
import bullet
import normal_zombie

name = "MainState"

UI = []
Resource = []
Normal_mob = []
Plant = []

sun_timer = 0.0
mob_timer = 0.0

def enter():
    UI.append(peashooter_ui.Peashooter_ui())
    Resource.append(sun.Sun())
    Normal_mob.append(normal_zombie.Normal_zombie())
    Plant.append(peashooter.Peashooter())

def exit():
    pass

def update():
    global sun_timer, mob_timer
    for i in UI:
        i.update()
    for i in Resource:
        i.update()
    for i in Plant:
        i.update()
    for i in Normal_mob:
        i.update()
    if(sun_timer > 1):
        Resource.append(sun.Sun())
        sun_timer = 0
    sun_timer += 0.01
    if(mob_timer > (random.randint(5, 10)) / 10):
        Normal_mob.append(normal_zombie.Normal_zombie())
        mob_timer = 0
    mob_timer += 0.01

def draw():
    clear_canvas()
    background.Background().draw()
    ui_slot.Ui_slot().draw()
    for i in UI:
        i.draw()
    for i in Resource:
        i.draw()
    for i in Plant:
        i.draw()
    for i in Normal_mob:
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