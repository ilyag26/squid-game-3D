from ursina import *
from ursina.shaders import lit_with_shadows_shader 
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

models = {
    "staff" : "models/staff.obj",
    "doll" : "models/doll.obj",
    "tree" : "models/tree.obj",
}

textures = {
    "sky":"textures/sky.png",
    "sand":"textures/sand.png",
    "field" : "textures/field.png",
}

class Staff: 
    def __init__(self, rot_x, rot_y, rot_z, pos_x, pos_y, pos_z, scale):
        self.staff = Entity(model=models['staff'], rotation=(0, -180, 0), scale=scale)
        self.staff.position = Vec3(pos_x, pos_y, pos_z)

class Walls:
    def __init__(self, scale_x, scale_z, rot_x, rot_y, rot_z, pos_x, pos_y, pos_z):
        self.wall = Entity(model = 'plane',
                        scale_x = scale_x, scale_z = scale_z, 
                        rotation_y = rot_y, rotation_x = rot_x, rotation_z = rot_z,
                        collider='box', texture = textures['field'])
        self.wall.position = Vec3(pos_x, pos_y, pos_z)

ground = Entity(model='plane', collider='box', scale=150, texture=textures['sand'])

#rot_x, rot_y, rot_z, pos_x, pos_y, pos_z, scale
staff = Staff(0, -180, 0, 4, 0, -52, 1.5)
staff2 = Staff(0, -180, 0, -4, 0, -52, 1.5)

doll = Entity(model=models['doll'], rotation=(0, -180, 0), shader = lit_with_shadows_shader)
doll.position = Vec3(0,0,-52)

tree = Entity(model=models['tree'], rotation=(0, -90, 0), shader = lit_with_shadows_shader)
tree.position = Vec3(0,0,-55.5)

player = FirstPersonController(model='cube', z=-10, rotation=(0, -180, 0), color=color.gray, origin_y=-.5, speed=13, collider='box')
player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))
player.position = Vec3(0,0,45)

#scale_x, scale_z, rotation_x, rotation_y, rotation_z, pos_x, pos_y, pos_z
front_wall = Walls(100, 70, 90, 0, 0, 0, 0, -75)
left_wall = Walls(170, 70, 90, -90, 0, 50, 0, -30)
right_wall = Walls(170, 70, 90, 90, 0, -50, 0, -30)
back_wall = Walls(100, 70, 90, -180, 0, 0, 0, 50)

window.color = color.rgb(135,206,250)

sun = DirectionalLight()
sun.look_at(Vec3(2,-2,-2))

sun2 = DirectionalLight()
sun2.look_at(Vec3(-40,40,40))

pivot = Entity()

def input(key):
    if key == 'escape':
        quit()


Sky()
app.run()