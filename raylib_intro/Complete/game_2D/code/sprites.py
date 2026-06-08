from settings import * 

class Sprite:
    def __init__(self, texture, pos, speed, direction):
        self.texture = texture
        self.pos = pos
        self.speed = speed
        self.direction = direction
        self.size = Vector2(texture.width, texture.height)
        self.discard = False
        self.collision_radius = self.size.y / 2
    
    def move(self, dt):
        self.pos.x += self.direction.x * self.speed * dt
        self.pos.y += self.direction.y * self.speed * dt

    def check_discard(self):
        self.discard = not -300 < self.pos.y < WINDOW_HEIGHT + 300

    def get_center(self):
        return Vector2(
            self.pos.x + self.size.x / 2,
            self.pos.y + self.size.y / 2,
        )

    def update(self, dt):
        self.move(dt)
        self.check_discard()

    def draw(self):
        draw_texture_v(self.texture, self.pos, WHITE)

class Player(Sprite):
    def __init__(self, texture, pos, shoot_laser):
        super().__init__(texture, pos, PLAYER_SPEED, Vector2())
        self.shoot_laser = shoot_laser

    def input(self):
        self.direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
        self.direction.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))
        self.direction = Vector2Normalize(self.direction)

        if is_key_pressed(KEY_SPACE):
            self.shoot_laser(Vector2(self.pos.x + self.size.x / 2, self.pos.y - 60))

    def constraint(self):
        self.pos.x = max(0, min(self.pos.x, WINDOW_WIDTH - self.size.x))
        self.pos.y = max(0, min(self.pos.y, WINDOW_HEIGHT - self.size.y))

    def update(self, dt):
        self.input()
        self.move(dt)
        self.constraint()

class Laser(Sprite):
    def __init__(self, texture, pos):
        super().__init__(texture, pos, LASER_SPEED, Vector2(0,-1))
    
    def get_rect(self):
        return Rectangle(self.pos.x, self.pos.y, self.size.x, self.size.y)

class Meteor(Sprite):
    def __init__(self, texture):
        pos = Vector2(randint(0, WINDOW_WIDTH), randint(-150,-50))
        speed = randint(*METEOR_SPEED_RANGE)
        direction = Vector2(uniform(-0.5, 0.5),1)
        super().__init__(texture, pos, speed, direction)
        self.rotation = 0
        self.rect = Rectangle(0, 0, self.size.x, self.size.y)
    
    def update(self, dt):
        super().update(dt)
        self.rotation += 50 * dt
    
    def get_center(self):
        return self.pos

    def draw(self):
        target_rect = Rectangle(self.pos.x, self.pos.y, self.size.x, self.size.y)
        draw_texture_pro(self.texture,self.rect,target_rect,Vector2(self.size.x / 2, self.size.y / 2),self.rotation, WHITE)

class ExplosionAnimation:
    def __init__(self, pos, textures):
        self.textures = textures
        self.size = Vector2(textures[0].width, textures[0].height)
        self.pos = Vector2(pos.x - self.size.x / 2, pos.y - self.size.y / 2)
        self.index = 0
        self.discard = False

    def update(self, dt):
        if self.index < len(self.textures) - 1:
            self.index += 20 * dt
        else:
            self.discard = True
        

    def draw(self):
        draw_texture_v(self.textures[int(self.index)], self.pos, WHITE)