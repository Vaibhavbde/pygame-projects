from pyray import *
from raylib import * 
from os.path import join

init_window(1920, 1080, "Move")

ship = load_texture(join('assets', 'spaceship.png'))
pos_x = 0
pos_y = 0

while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    draw_texture(ship, pos_x, pos_y, WHITE)
    end_drawing()
close_window()