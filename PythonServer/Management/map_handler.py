from ks.models import World, Pacman, Ghost, Constants, ECell, EDirection
import json

class MapHandler ():
    _sides = []

    def __init__(self, sides):
        self._sides = sides

    def load_map(self, config):

        map_config = json.loads(open((config['map']), "r").read())
        board = map_config['board']

        global BOARD_WIDTH, BOARD_HEIGHT
        BOARD_WIDTH = len(board[0])
        BOARD_HEIGHT = len(board)

        world = World()
        world.width = BOARD_WIDTH
        world.height = BOARD_HEIGHT
        # self.world.scores = {side: 0 for side in self.sides}
      
        
    # world is an instance of World 
        return world, board
