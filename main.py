from ursina import *
from ursina.shaders import lit_with_shadows_shader 
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

red = False

models = {
    "staff" : "models/staff.obj",
    "doll" : "models/doll.obj",
    "tree" : "models/tree.obj",
}

textures = {
    "sky":"textures/sky.png",
    "sand":"textures/sand.png",
    "field" : "textures/field.png",
    "hand" : "textures/hand.png"
}

class UI(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='sphere',
            position=Vec2(0.5, -0.4),
            scale=(0.3, 0.3, 0.6),
            texture = textures['hand'],
            rotation=(130, -50, -40)
)

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

text = Text(text="Green", scale=3, x=-.83, y=.45, color = color.green) 

def update_text_red():
    red = True
    text.text = "Red"
    text.color = color.red
    invoke(update_text_green, delay=3)

def update_text_green():
    red = False
    text.text = "Green"
    text.color = color.green
    invoke(update_text_red, delay=3)

def light():
    invoke(update_text_green, delay=3)

ground = Entity(model='plane', collider='box', scale=150, texture=textures['sand'])
line = Entity(model='wireframe_cube', scale_x = 3, scale_y = 3, collider = "box", color = color.red)
line.position = Vec3(0, 0.1, -40)
linew = Entity(model='wireframe_cube', scale_x = 1, scale_y = 1, collider = "box", color = color.green)
linew.position = Vec3(0, 0.1, -40)
# line.position = Vec3(0, 0.08, -40)

#scale_x, scale_z, rotation_x, rotation_y, rotation_z, pos_x, pos_y, pos_z
front_wall = Walls(100, 70, 90, 0, 0, 0, 0, -75)
left_wall = Walls(170, 70, 90, -90, 0, 50, 0, -30)
right_wall = Walls(170, 70, 90, 90, 0, -50, 0, -30)
back_wall = Walls(100, 70, 90, -180, 0, 0, 0, 50)

#rot_x, rot_y, rot_z, pos_x, pos_y, pos_z, scale
staff = Staff(0, -180, 0, 4, 0, -52, 1.5)
staff2 = Staff(0, -180, 0, -4, 0, -52, 1.5)

doll = Entity(model=models['doll'], rotation=(0, -180, 0), shader = lit_with_shadows_shader)
doll.position = Vec3(0, 0, -52)

tree = Entity(model=models['tree'], rotation=(0, -90, 0), shader = lit_with_shadows_shader)
tree.position = Vec3(0, 0, -55.5)

player = FirstPersonController(model='cube', z=-10, rotation=(0, -180, 0), color=color.gray, origin_y=-.5, speed=13)
player.position = Vec3(0, 0, 45)
text1 = Text(text="000", scale=3, x=-.83, y=.45) 

def update():
    if player.intersects(linew).hit:
        text1.text = "4783"
        print("fjkdsvnvkjnfdskvn")

window.color = color.rgb(135, 206, 250)

sun = DirectionalLight()
sun.look_at(Vec3(2, -2, -2))

sun2 = DirectionalLight()
sun2.look_at(Vec3(-40, 40, 40))

pivot = Entity()

def input(key):
    if key == 'escape':
        quit()

light()

UI()
Sky()
app.run()