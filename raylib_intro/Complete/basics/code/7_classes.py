from pyray import *
from raylib import *
from os.path import join

class Sprite:
    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed
    
    def move(self, dt):
        self.pos.x += self.direction.x * self.speed * dt
        self.pos.y += self.direction.y * self.speed * dt

class Player(Sprite):
    def __init__(self, pos):
        super().__init__(pos, 400)
        self.texture = load_texture(join('assets','spaceship.png'))
        self.direction = Vector2()
    
    def update(self, dt):
        self.direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
        self.direction.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))
        self.direction = Vector2Normalize(self.direction)
        
        # update 
        self.move(dt)

    def draw(self):
        draw_texture_v(self.texture, self.pos, WHITE)

class Block(Sprite):
    def __init__(self, pos, speed):
        super().__init__(pos, speed)
        self.direction = Vector2(1,0)
        self.size = Vector2(100,200)

    def update(self, dt):
        self.move(dt)

    def draw(self):
        draw_rectangle_v(self.pos,self.size, RED)

init_window(1920,1080, 'OOP')
sprites = [Player(Vector2(500,200)), Block(Vector2(700,0), 200)]

while not window_should_close():
    
    dt = get_frame_time()
    for sprite in sprites:
        sprite.update(dt)
    
    begin_drawing()
    clear_background(BLACK)
    for sprite in sprites:
        sprite.draw()
    end_drawing()

close_window()