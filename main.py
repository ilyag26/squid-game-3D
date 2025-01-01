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
}

env = Entity()
ground = Entity(model='plane', collider='box', scale=150, texture=textures['sand'])

staff = Entity(model=models['staff'], rotation=(0, -180, 0), scale=1.5)
staff.position = Vec3(4,0,-52)

staff2 = Entity(model=models['staff'], rotation=(0, -180, 0), scale=1.5)
staff2.position = Vec3(-4,0,-52)

doll = Entity(model=models['doll'], rotation=(0, -180, 0), shader = lit_with_shadows_shader)
doll.position = Vec3(0,0,-52)

tree = Entity(model=models['tree'], rotation=(0, -90, 0), shader = lit_with_shadows_shader)
tree.position = Vec3(0,0,-55.5)

player = FirstPersonController(model='cube', z=-10, rotation=(0, -180, 0), color=color.gray, origin_y=-.5, speed=13, collider='box')
player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))
player.position = Vec3(0,0,45)

wall1 = Entity(model='plane', scale_x=100, scale_z=70, rotation_x = 90, collider='box', color = color.blue)
wall1.position = Vec3(0,0,-75)

wall2 = Entity(model='plane', scale_x=170, scale_z=70, rotation_x = 90, rotation_y = -90, collider='box', color = color.blue)
wall2.position = Vec3(50,0,-30)

wall3 = Entity(model='plane', scale_x=170, scale_z=70, rotation_x = 90, rotation_y = 90, collider='box', color = color.blue)
wall3.position = Vec3(-50,0,-30)

wall3 = Entity(model='plane', scale_x=100, scale_z=70, rotation_x = 90, rotation_y = -180, collider='box', color = color.blue)
wall3.position = Vec3(0,0,50)

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
print(player.position)