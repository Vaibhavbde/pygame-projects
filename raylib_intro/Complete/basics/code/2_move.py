from pyray import *
from raylib import * 
from os.path import join

init_window(1920, 1080, "Move")
# set_target_fps(100)

# imports
ship = load_texture(join('assets', 'spaceship.png'))
ship_pos = Vector2(0,0)
ship_direction = Vector2(1,1)
ship_speed = 800

while not window_should_close():
    
    # updates
    if ship_pos.y >= 1080 - 40:
        ship_direction.y = -1
    if ship_pos.x >= 1920 - 100:
        ship_direction.x = -1
    if ship_pos.y <= 0:
        ship_direction.y = 1
    if ship_pos.x <= 0:
        ship_direction.x = 1

    dt = get_frame_time()
    ship_pos.x += ship_direction.x * ship_speed * dt
    ship_pos.y += ship_direction.y * ship_speed * dt

    # drawing
    begin_drawing()
    clear_background(BLACK)
    draw_texture_v(ship, ship_pos, WHITE)
    draw_fps(0,0)
    end_drawing()
close_window()