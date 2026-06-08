from pyray import *
from raylib import * 
from os.path import join

init_window(1920, 1080, "Input")
ship_texture = load_texture(join('assets', 'spaceship.png'))
ship_pos = Vector2(0,0)
ship_direction = Vector2(0,0)
ship_speed = 800

while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    draw_texture_v(ship_texture, ship_pos, WHITE)
    end_drawing()
close_window()