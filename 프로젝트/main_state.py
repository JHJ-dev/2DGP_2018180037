from pico2d import *
import game_framework
import game_world
import title_state

from background import Background
from ui_slot import Ui_slot
from peashooter_ui import Peashooter_ui
from sun import Sun
from peashooter import Peashooter
from bullet import Bullet
from normal_zombie import Normal_zombie

name = "MainState"

UI = []
Resource = []
Plant = []
Mob1 = []
Mob2 = []

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def enter():
    background = Background()
    game_world.add_object(background, 0)

    ui_slot = Ui_slot()
    game_world.add_object(ui_slot, 0)

    peashooter_ui = Peashooter_ui()
    game_world.add_object(peashooter_ui, 0)

    peashooter = Peashooter()
    game_world.add_object(peashooter, 1)

    global sun
    sun = Sun()
    normal_zombie = Normal_zombie()

def update():
    global Time
    Time = int(get_time())
    if (Time % 5 == 0):
        game_world.add_object(sun, 1)
    print(Time)
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def exit():
    game_world.clear()

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