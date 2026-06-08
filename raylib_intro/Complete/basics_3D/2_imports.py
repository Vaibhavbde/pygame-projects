from pyray import *
from raylib import *
from os.path import join

init_window(1920, 1080, "3D imports")
camera = Camera3D()
camera.position = Vector3(0.0, 3.0, 5.0) 
camera.target = Vector3(0.0, 0.0, 0.0) 
camera.up = Vector3(0.0, 1.0, 0.0) 
camera.fovy = 45.0 
camera.projection = CAMERA_PERSPECTIVE 

# imports 
ship = load_model(join('models','ship.glb'))
rupee = load_model(join('models','rupee.gltf')) # texture and bin file must be there
ship_fail = load_model(join('models','ship_fail.glb')) # far from origin point
rotation = 0

while not window_should_close():
    # ship.transform = matrix_scale(10,10,10)
    dt = get_frame_time()
    rotation += 20 * dt
    begin_drawing()    
    clear_background(WHITE)
    begin_mode_3d(camera)
    draw_grid(10,1.0)
    draw_model_ex(ship, Vector3(),Vector3(0,1,0),rotation,Vector3(1.4,1.4,1.4),WHITE)
    end_mode_3d()
    end_drawing()

close_window()