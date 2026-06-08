from pyray import *
from raylib import * 
from random import randint, choice

init_window(1920, 1080, "Camera")

# player
pos = Vector2()
radius = 50
direction = Vector2()
speed = 400

# circles
circles = [
    (
        Vector2(randint(-2000,2000),randint(-1000,1000)), # pos
        randint(50,200), # radius
        choice([RED, GREEN, BLUE, YELLOW, ORANGE]) # color
    ) 
    for i in range(100)
]

while not window_should_close():
    
    # input
    direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
    direction.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))
    direction = vector2_normalize(direction)

    # movement
    dt = get_frame_time()
    pos.x += direction.x * speed * dt
    pos.y += direction.y * speed * dt

    # drawing
    begin_drawing()
    clear_background(WHITE)
    for circle in circles:
        draw_circle_v(*circle)
    draw_circle_v(pos, radius, BLACK)
    end_drawing()

close_window()