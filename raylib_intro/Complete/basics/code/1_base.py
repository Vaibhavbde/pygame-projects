from pyray import *
from raylib import *
from os.path import join

init_window(1920,1080, 'Base')

# import images/textures
spaceship_texture = load_texture(join('assets', 'spaceship.png'))
spaceship_image = load_image(join('assets', 'spaceship.png'))
image_color_grayscale(spaceship_image)
new_texture = load_texture_from_image(spaceship_image)

cowboy_image = load_image(join('assets','animation', '0.png'))
image_color_invert(cowboy_image)
cowboy_texture = load_texture_from_image(cowboy_image)

# import font
font = load_font(join('assets', 'Zero Hour.otf'))

while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    
    # custom shape drawing
    draw_pixel(100, 200, RED)
    draw_pixel_v(Vector2(200,200),WHITE)
    draw_circle_v(Vector2(1000,600), 200, YELLOW)
    draw_circle(1000, 600, 100, GREEN)
    draw_line_ex(Vector2(0,0), Vector2(500,200), 10, (50,0,0,255))
    
    # display images
    draw_texture(spaceship_texture, 0, 0, WHITE)
    draw_texture_v(new_texture,Vector2(100,0),WHITE)
    draw_texture(cowboy_texture, 1800, 900, WHITE)

    # displaying text
    draw_text('Some text',0, 400, 100, WHITE)
    draw_text_ex(font, 'Some more text', Vector2(0,600), 20, 0, BLUE)

    end_drawing()

close_window()