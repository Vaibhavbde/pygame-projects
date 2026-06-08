from pyray import *
from raylib import *
from os.path import join

init_window(1920,1080, 'Animations')

while not window_should_close():
    dt = get_frame_time()
    begin_drawing()
    clear_background(BLACK)
    end_drawing()

close_window()