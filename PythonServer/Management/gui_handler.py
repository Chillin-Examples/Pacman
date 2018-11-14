from ks.models import World, Pacman, Ghost, Constants, ECell, EDirection
import math

class GuiHandler ():


    def __init__(self, sides, world, canvas):

        self._sides = sides
        self._world = world
        self._canvas = canvas
    # Oo
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
                if cell == ECell.Wall: 
                    self._canvas.create_image('Wall', 20,20)
                    # self.canvas.create_image('Wall', x * self.cell_size, y * self.cell_size, scale_type=ScaleType.ScaleToWidth, scale_value=self.cell_size)
                elif cell == ECell.Empty: 
                    self._canvas.create_image('Empty', 30,30)

    
    def update(self, events):
        pass
    