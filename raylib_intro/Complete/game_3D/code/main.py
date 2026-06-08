from settings import * 
from models import Floor, Player, Laser, Meteor

class Game:
    def __init__(self):
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Space shooter")
        init_audio_device()
        self.import_assets()

         # camera
        self.camera = Camera3D()
        self.camera.position = Vector3(-4.0, 8.0, 6.0) 
        self.camera.target = Vector3(0.0, 0.0, -1.0) 
        self.camera.up = Vector3(0.0, 1.0, 0.0) 
        self.camera.fovy = 45.0 
        self.camera.projection = CAMERA_PERSPECTIVE 

        # setup
        self.floor = Floor(self.dark_texture)
        self.player = Player(self.models['player'], self.shoot_laser)
        self.lasers, self.meteors = [], []
        self.meteor_timer = Timer(METEOR_TIMER_DURATION, True, True, self.create_meteor)
        play_music_stream(self.audio['music'])

    def create_meteor(self):
        self.meteors.append(Meteor(choice(self.textures)))

    def shoot_laser(self, pos):
        self.lasers.append(Laser(self.models['laser'], pos, self.light_texture))
        play_sound(self.audio['laser'])

    def import_assets(self):
        self.models = {
            'player': load_model(join('models','ship.glb')),
            'laser': load_model(join('models','laser.glb')),
        }

        self.audio = {
            'laser': load_sound(join('audio','laser.wav')),
            'explosion': load_sound(join('audio','explosion.wav')),
            'music': load_music_stream(join('audio','music.wav')),
        }

        self.textures = [load_texture(join('textures', f'{color}.png')) for color in ('red', 'green', 'orange', 'purple')]
        self.dark_texture = load_texture(join('textures', 'dark.png'))
        self.light_texture = load_texture(join('textures', 'light.png'))

        self.font = load_font_ex('Stormfaze.otf', FONT_SIZE, ffi.NULL,0)
 
    def check_discard(self):
        self.lasers = [laser for laser in self.lasers if not laser.discard]
        self.meteors = [meteor for meteor in self.meteors if not meteor.discard]

    def check_collisions(self):
        # player -> meteor
        for meteor in self.meteors:
            if check_collision_spheres(self.player.pos, 0.8, meteor.pos, meteor.radius):
                close_window()

        # laser -> meteor
        for laser in self.lasers:
            for meteor in self.meteors:
                laser_bbox = get_mesh_bounding_box(laser.model.meshes[0])
                col_bbox = BoundingBox(
                    Vector3Add(laser_bbox.min, laser.pos), # min
                    Vector3Add(laser_bbox.max, laser.pos), # max
                )
                if check_collision_box_sphere(col_bbox, meteor.pos, meteor.radius):
                    meteor.hit = True
                    laser.discard = True
                    meteor.death_timer.activate()
                    meteor.flash()
                    play_sound(self.audio['explosion'])
    
    def update(self):
        dt = get_frame_time()
        self.check_collisions()
        self.check_discard()
        self.meteor_timer.update()
        self.player.update(dt)
        for model in self.lasers + self.meteors:
            model.update(dt)
        update_music_stream(self.audio['music'])

    def draw_shadows(self):
        player_radius = 0.5 + self.player.pos.y
        draw_cylinder(Vector3(self.player.pos.x, -1.5, self.player.pos.z), player_radius,player_radius,0.1,20,(0,0,0,50))

        for meteor in self.meteors:
            draw_cylinder(Vector3(meteor.pos.x, -1.5, meteor.pos.z), meteor.radius * 0.8, meteor.radius * 0.8, 0.1,20, (0,0,0,50))

    def draw_score(self):
        score = str(int(get_time()))
        draw_text_ex(self.font, score, Vector2(WINDOW_WIDTH - FONT_PADDING, WINDOW_HEIGHT - FONT_PADDING), FONT_SIZE,2, WHITE)

    def draw(self):
        clear_background(BG_COLOR)
        begin_drawing()
        begin_mode_3d(self.camera)
        self.floor.draw()
        self.draw_shadows()
        self.player.draw()
        for model in self.lasers + self.meteors:
            model.draw()
        end_mode_3d()
        self.draw_score()
        end_drawing()

    def run(self):
        while not window_should_close():
            self.update()
            self.draw() 
        unload_music_stream(self.audio['music'])
        close_audio_device()
        close_window()

if __name__ == '__main__':
    game = Game()
    game.run()