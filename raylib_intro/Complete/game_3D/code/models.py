from settings import *
from math import sin

class Model:
    def __init__(self, model, pos, speed, direction = Vector3()):
        self.model = model
        self.pos = pos
        self.speed = speed
        self.direction = direction
        self.discard = False
    
    def move(self, dt):
        self.pos.x += self.direction.x * self.speed * dt
        self.pos.y += self.direction.y * self.speed * dt
        self.pos.z += self.direction.z * self.speed * dt

    def update(self, dt):
        self.move(dt)

    def draw(self):
        draw_model(self.model, self.pos, 1, WHITE)

class Floor(Model):
    def __init__(self, texture):
        model = load_model_from_mesh(gen_mesh_cube(32,1,32))
        set_material_texture(model.materials[0], MATERIAL_MAP_ALBEDO, texture)
        super().__init__(model, Vector3(6.5,-2,-8), 0)

class Player(Model):
    def __init__(self, model, shoot_laser):
        super().__init__(model, Vector3(), PLAYER_SPEED)
        self.shoot_laser = shoot_laser
        self.angle = 0
    
    def input(self):
        self.direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
        if is_key_pressed(KEY_SPACE):
            self.shoot_laser(Vector3Add(self.pos, Vector3(0,0,-1)))

    def update(self, dt):
        self.input()
        super().update(dt)
        self.angle -= self.direction.x * 10 * dt
        self.pos.y += sin(get_time() * 5) * dt * 0.1

        # constraints
        self.pos.x = max(-6, min(self.pos.x,7))
        self.angle = max(-15, min(self.angle, 15))
    
    def draw(self):
        draw_model_ex(self.model, self.pos, Vector3(0,0,1), self.angle, Vector3(1,1,1),WHITE)

class Laser(Model):
    def __init__(self, model, pos, texture):
        super().__init__(model, pos, LASER_SPEED,Vector3(0,0,-1))
        set_material_texture(self.model.materials[0], MATERIAL_MAP_ALBEDO, texture)

class Meteor(Model):
    def __init__(self, texture):
        # setup
        pos = Vector3(uniform(-6,7),0,-20)
        self.radius = uniform(0.6, 1.5)
        model = load_model_from_mesh(gen_mesh_sphere(self.radius, 8,8))
        set_material_texture(model.materials[0], MATERIAL_MAP_ALBEDO, texture)
        super().__init__(model, pos, uniform(*METEOR_SPEED_RANGE), Vector3(0,0,uniform(0.75,1.25)))

        # rotation 
        self.rotation = Vector3(uniform(-5,5),uniform(-5,5),uniform(-5,5))
        self.rotation_speed = Vector3(uniform(-1,1),uniform(-1,1),uniform(-1,1))

        # discard logic
        self.hit = False
        self.death_timer = Timer(0.25, False, False, self.activate_discard)
    
        # shader
        self.shader = load_shader(ffi.NULL, join('shaders', 'flash.fs'))
        model.materials[0].shader = self.shader
        self.flash_loc = get_shader_location(self.shader, 'flash')
        self.flash_amount = ffi.new('struct Vector2 *', [1,0])

    def flash(self):
        set_shader_value(self.shader, self.flash_loc, self.flash_amount, SHADER_UNIFORM_VEC2)

    def activate_discard(self):
        self.discard = True

    def update(self, dt):
        self.death_timer.update()
        if not self.hit:
            super().update(dt)
            self.rotation.x += self.rotation_speed.x * dt
            self.rotation.y += self.rotation_speed.y * dt
            self.rotation.z += self.rotation_speed.z * dt
            self.model.transform = matrix_rotate_xyz(self.rotation)