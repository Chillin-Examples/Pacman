from ks.models import World, Pacman, Ghost, Constants, ECell, EDirection
import math
from chillin_server.gui.canvas_elements import ScaleType

class GuiHandler ():


    def __init__(self, sides, world, canvas):

        self._sides = sides
        self._world = world
        self._canvas = canvas

    # Oo -____-
    def config(self, gameobj):
        # gameobj.scale_factor = (gameobj.canvas.width - gameobj.config['statuses_width']) / (gameobj.world.width * gameobj.config['cell_size'])
        # gameobj.scale_percent = math.ceil(gameobj.scale_factor * 100)
        # gameobj.cell_size = math.ceil(gameobj.config['cell_size'] * gameobj.scale_factor)
        # gameobj.font_size = gameobj.cell_size // 2
        print("gameconfig")


    def draw_board(self, height, width, board):
        for y in range(height):
            for x in range(width):
                cell = board[y][x]
                if cell == ECell.Wall and (y == height or y==0): 
                    # self._canvas.create_image('UDwall', 20,20)
                    self._canvas.create_image('Wall', x * 150, y * 150, scale_type=ScaleType.ScaleToWidth, scale_value=150)
                elif cell == ECell.Empty and (x==width or x==0): 
                    self._canvas.create_image('RLwall', 30,30)
                else:
                    self._convas.create_image

    
    def update(self, events):
        pass
    