from pico2d import *
import game_framework
import title_state

from map import Map
from slot import Slot
from sun import Sun
from zombie1 import Zombie1

name = "MainState"

map = None
slot = None
sun = None
zombie1 = None

def enter():
    global map, slot, Resource, Monster1
    Resource = [Sun() for i in range(3)]
    Monster1 = [Zombie1() for i in range(3)]
    map = Map()
    slot = Slot()

def exit():
    global map, slot, sun, zombie1
    del map
    del slot
    del sun
    del zombie1

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

def update():
    for sun in Resource:
        sun.update()
    for zombie1 in Monster1:
        zombie1.update()

def draw():
    clear_canvas()
    map.draw()
    slot.draw()
    for sun in Resource:
        sun.draw()
    for zombie1 in Monster1:
        zombie1.draw()
    update_canvas()
    delay(0.05)