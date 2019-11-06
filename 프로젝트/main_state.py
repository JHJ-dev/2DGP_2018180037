from pico2d import *
import game_framework
import game_world
import title_state
import random

from background import *
from ui_slot import *
from peashooter_ui import *
from sun import *
from peashooter import *
from bullet import *
from normal_zombie import *

name = "MainState"

UI = []
Resource = []
Plant = []
Monster = []

sun_timer = 0.0
mob_timer = 0.0

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def enter():
    global sun_timer, mob_timer
    background = Background()
    ui_slot = Ui_slot()
    peashooter_ui = Peashooter_ui()
    sun = Sun()
    peashooter = Peashooter()
    normal_zombie = Normal_zombie()
    game_world.add_object(background, 0)
    game_world.add_object(ui_slot, 0)
    game_world.add_object(peashooter_ui, 0)
    if(sun_timer > 1):
        game_world.add_object(sun, 1)
        sun_timer = 0
    game_world.add_object(peashooter, 1)
    if (mob_timer > (random.randint(5, 10)) / 10):
        game_world.add_object(normal_zombie, 1)
        mob_timer = 0


def exit():
    game_world.clear()

def update():
    global sun_timer, mob_timer
    sun_timer += 0.01
    mob_timer += 0.01
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
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