from pyray import *
from raylib import *
from random import choice

class Timer:
    def __init__(self, duration: int, repeat = False, autostart = False, func = None):
        self.duration = duration
        self.start_time = 0
        self.active = False
        self.repeat = repeat
        self.func = func
		
        if autostart:
            self.activate()

    def activate(self):
        self.active = True
        self.start_time = get_time()

    def deactivate(self):
        self.active = False
        self.start_time = 0
        if self.repeat:
            self.activate()

    def update(self):
        if self.active:
            if get_time() - self.start_time >= self.duration:
                if self.func and self.start_time: self.func()
                self.deactivate()

class Sprite:
    def __init__(self, pos, size):
        self.rec = Rectangle(pos[0], pos[1], size[0], size[1])
        self.color = WHITE

    def randomize_color(self):
        self.color = choice([RED, YELLOW, GREEN, ORANGE, MAGENTA, BLUE, GRAY, MAROON])

    def draw(self):
        draw_rectangle_rec(self.rec, self.color) 

init_window(1920,1080, 'Timer')

while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    end_drawing()

close_window()