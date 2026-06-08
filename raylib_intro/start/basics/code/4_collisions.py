from pyray import *
from raylib import * 

init_window(1920, 1080, "Collisions")
player_pos = Vector2(0,0)
obstacle_pos = Vector2(500,400) 
player_radius = 50
obstacle_radius = 30

while not window_should_close():
    
    # input 
    player_pos = get_mouse_position()
    
    # drawing
    begin_drawing()
    clear_background(BLACK)
    draw_circle_v(player_pos, player_radius, WHITE)
    draw_circle_v(obstacle_pos, obstacle_radius, RED)    
    end_drawing()

close_window()