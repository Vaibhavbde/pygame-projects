from pyray import *
from raylib import *
from os.path import join

class AnimatedSprite:
    def __init__(self):
        self.animation_frames = [load_texture(join('assets', 'animation', f'{i}.png')) for i in range(8)]
        self.animation_index, self.animation_speed = 0, 5
    
    def update(self, dt):
        self.animation_index += self.animation_speed * dt

    def draw(self):
        draw_texture(self.animation_frames[int(self.animation_index) % len(self.animation_frames)],0,0,WHITE)

init_window(1920,1080, 'Animations')
# animation_frames = [load_texture(join('assets', 'animation', f'{i}.png')) for i in range(8)]
# animation_index = 0
# animation_speed = 5
animated_sprite = AnimatedSprite()

while not window_should_close():
    dt = get_frame_time()
    # animation_index += animation_speed * dt
    animated_sprite.update(dt)
    begin_drawing()
    clear_background(BLACK)
    animated_sprite.draw()
    # draw_texture(animation_frames[int(animation_index) % len(animation_frames)],0,0,WHITE)
    end_drawing()

close_window()