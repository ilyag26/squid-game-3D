from ursina import *
from ursina.shaders import lit_with_shadows_shader 
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

textures = {
    "sky":{
         "sky":"texturas/sky.png"
    },
}

env = Entity()
ground = Entity(model='plane', collider='box', scale=150, texture='texturas/ws.png')
staff = Entity(model='models/staff.obj', scale=2)
staff.position = Vec3(4,0,52)
staff2 = Entity(model='models/staff.obj', scale=2)
staff2.position = Vec3(-4,0,52)
doll = Entity(model='models/doll.obj', shader = lit_with_shadows_shader)
doll.position = Vec3(0,0,52)
tree = Entity(model='models/tree.obj', rotation=(0, 90, 0), shader = lit_with_shadows_shader)
tree.position = Vec3(0,0,55.5)
player = FirstPersonController(model='cube', z=-10, color=color.gray, origin_y=-.5, speed=13, collider='box')
player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))
player.position = Vec3(0,0,-55)
wall1 = Entity(model='plane', scale_x=100, scale_z=70, rotation=(90, 0, 0), collider='box')
wall1.position = Vec3(0,0,-75)

window.color = color.rgb(135,206,250)
DirectionalLight(parent=env, y=0, z=0, shadows=True, rotation=(45, -45, 45))
pivot = Entity()
# EditorCamera()

def input(key):
    if key == 'escape':
        quit()

Sky()
app.run()
print(player.position)