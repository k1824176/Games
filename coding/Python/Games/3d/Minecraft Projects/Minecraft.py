from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import base64
import json
import pyperclip  # You need to install this package using `pip install pyperclip`

blocks = ['cherry_trapdoor.png', 'stone.jpeg', 'quartz.png', 'cherry_leaves.png', 'cherry_planks.png', 'crimson_planks.png', 'cherry.jpg', 'dark_oak.jpg', 'cherry_wood.png', 'polished_deepslate.png']
block = 0
voxels = {}

def save_game():
    game_state = [{'position': pos, 'texture': v.texture.name} for pos, v in voxels.items()]
    game_code = base64.b64encode(json.dumps(game_state).encode()).decode()
    game_code_text.text = f"Game code: {game_code}"

def load_game(game_code):
    try:
        game_state = json.loads(base64.b64decode(game_code.encode()).decode())
        for voxel_data in game_state:
            Voxel(position=tuple(voxel_data['position']), texture=voxel_data['texture'])
    except (json.JSONDecodeError, base64.binascii.Error) as e:
        print("Invalid game code")
        error_text.text = "Invalid game code"

def copy_game_code():
    pyperclip.copy(game_code_text.text.split(": ")[1])

class Voxel(Button):
    def __init__(self, position, texture):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            highlight=color.gray,
            color=color.white
        )
        voxels[tuple(position)] = self

    def input(self, key):
        global block
        if key in '0123456789':
            block = int(key) - 1
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal, texture=blocks[block])
            elif key == 'right mouse down':
                pos = tuple(self.position)
                if pos in voxels:
                    del voxels[pos]
                    destroy(self)
            elif key == 'escape':
                exit()
            elif key == 'e':
                mouse.locked = False
            elif key == 'f':
                mouse.locked = True

def setup_world():
    for z in range(30):  # Reduced the number of voxels created
        for x in range(30):
            for y in range(2):
                Voxel(position=(x, y, z), texture='Minecraft_grass.png')

def input(key):
    if key == 't':
        save_game()
    if key == 'l':
        game_code = input_field.text
        if game_code:
            load_game(game_code)

app = Ursina()
window.fullscreen = True

setup_world()
player = FirstPersonController()
Sky(texture='sky.jpg')

game_code_text = Text(text='', position=(-0.5, 0.4), origin=(0, 0), background=True)
input_field = InputField(position=(-0.5, 0.3), origin=(0, 0), background=True)
Button("Copy Game Code", position=(-0.5, 0.2), origin=(0, 0), scale=(0.2, 0.1), on_click=copy_game_code)
Button("Load Game", position=(-0.5, 0.1), origin=(0, 0), scale=(0.2, 0.1), on_click=lambda: load_game(input_field.text))
error_text = Text(text='', position=(-0.5, 0.0), origin=(0, 0), background=True, color=color.red)

app.run()