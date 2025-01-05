from ursina import *
from ursina.shaders import lit_with_shadows_shader 
from ursina.prefabs.first_person_controller import FirstPersonController 

app = Ursina()

red = False
game = True
win = False
printing = False

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

class Game_over(Entity):
    def __init__(self, width=5, height=8, **kwargs):
        super().__init__(
            parent = camera.ui,
            model = Quad(radius=.015),
            scale = (width*.1, height*.1),
            origin = (-.5,.5),
            position = (-.3,.4),
            color = color.hsv(0,181,225),
            )

        self.width = width
        self.height = height

class Game_win(Entity):
    def __init__(self, width=5, height=8, **kwargs):
        super().__init__(
            parent = camera.ui,
            model = Quad(radius=.015),
            scale = (width*.1, height*.1),
            origin = (-.5,.5),
            position = (-.3,.4),
            color = color.hsv(140,255,200),
            )

        self.width = width
        self.height = height

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

ground = Entity(model='plane', collider='box', scale=150, texture=textures['sand'])
line = Entity(model='cube', scale_x = 100, scale_y = 2, collider = "box", color = color.red)
line.position = Vec3(0, -0.92, -40)
# line.position = Vec3(0, 0.08, -40)

#scale_x, scale_z, rotation_x, rotation_y, rotation_z, pos_x, pos_y, pos_z
front_wall = Walls(100, 70, 90, 0, 0, 0, 0, -75)
left_wall = Walls(170, 70, 90, -90, 0, 50, 0, -30)
right_wall = Walls(170, 70, 90, 90, 0, -50, 0, -30)
back_wall = Walls(100, 70, 90, -180, 0, 0, 0, 50)

#rot_x, rot_y, rot_z, pos_x, pos_y, pos_z, scale
staff = Staff(0, -180, 0, 4, 0, -52, 1.5)
staff2 = Staff(0, -180, 0, -4, 0, -52, 1.5)

doll = Entity(model=models['doll'], rotation=(0, 0, 0), shader = lit_with_shadows_shader)
doll.position = Vec3(0, 0, -52)

tree = Entity(model=models['tree'], rotation=(0, -90, 0), shader = lit_with_shadows_shader)
tree.position = Vec3(0, 0, -55.5)

player = FirstPersonController(rotation=(0, -180, 0), speed=13)
player.position = Vec3(0, -0.4, 45)

cube_player = Entity(scale = 1, color = color.orange, collider="box")
cube_player.position = Vec3(0, -0.4, 45)

def game_over2():
    global game_over
    game_over = Game_over()
    global game
    game = False
    destroy(text)
    global text2
    text2 = Text(text="GAME OVER", scale=2, x=-.30, y=.30, color = color.yellow) 
    text2 = Text(text="Pulsa teclo R para \nreiniciar el juego", scale=2, x=-.30, y=.20, color = color.yellow) 


def game_win2():
    global game_win1
    game_win1 = Game_win()
    destroy(text)
    global text4
    text4 = Text(text="GAME WIN", scale=2, x=-.30, y=.30, color = color.yellow) 
    text4 = Text(text="Pulsa teclo G para \nreiniciar el juego", scale=2, x=-.30, y=.20, color = color.yellow) 

def update_text_red():
    global red
    red = True
    if game:
        text.text = "Red"
        text.color = color.red
        doll.rotation = (0, 180, 0)
        invoke(update_text_green, delay=3)

def update_text_green():
    global red
    red = False
    if game:
        text.text = "Green"
        text.color = color.green
        doll.rotation = (0, 0, 0)
        invoke(update_text_red, delay=3)

def update():
    cube_player.position = player.position
    if line.intersects(cube_player).hit:
        global game
        global win
        game = False
        win = True
        global printing
        if printing == False:
            printing = True
            print("heu")
            game_win2()

def destroy_all_ui_elements():
    print(win)
    if win: 
        destroy(game_win1)
        destroy(text4)
    if not win:
        destroy(game_over)
        destroy(text2)
    
    global printed 
    printed = False
    for entity in scene.entities:
        if isinstance(entity, Button) or isinstance(entity, Text) or isinstance(entity, Game_win) or isinstance(entity, Game_over):
            destroy(entity)
    for entity in scene.entities:
        if isinstance(entity, Text):
            destroy(entity)

def text_initialize():
    global text
    text = Text(text="Green", scale=3, x=-.83, y=.45, color = color.green) 

def restart():
    player.speed = 13
    global game
    game = True
    global red
    red = False
    cube_player.position = Vec3(0, -0.4, 45)
    player.position = Vec3(0, -0.4, 45)
    doll.rotation = (0, 0, 0)
    destroy_all_ui_elements()
    text_initialize()
    update_text_green()
    global win 
    win= False

window.color = color.rgb(135, 206, 250)

sun = DirectionalLight()
sun.look_at(Vec3(2, -2, -2))

sun2 = DirectionalLight()
sun2.look_at(Vec3(-40, 40, 40))

pivot = Entity()

def input(key):
    if key == 'escape':
        quit()

    global red
    if key == 'w' or key == 's' or key == 'a' or key == 'd':
        if red == True:
            game_over2()

    global win
    if key == "g" and win == True:
            restart()
    
    global game
    if key == "r" and game == False and not win:
            restart()

    if game == False:
        if key == 'w' or key == 's' or key == 'a' or key == 'd':
            player.speed = 0


text_initialize()
update_text_green()
UI()
Sky()
app.run()