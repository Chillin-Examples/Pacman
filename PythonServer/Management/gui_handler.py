from ks.models import World, Pacman, Ghost, Constants, ECell, EDirection

class GuiHandler ():

    _sides = []
    # _world = World()
    

    def __init__(self, sides, world, canvas):

        self._sides = sides
        self.world = world
        self._canvas = canvas

    
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
    