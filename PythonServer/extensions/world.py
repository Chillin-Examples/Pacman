# -*- coding: utf-8 -*-

# project imports
from ks.commands import ECommandDirection, ChangePacmanDirection
from ks.models import World
from gui_events import GuiEvent, GuiEventType

def apply_command(self, side_name, command):
    print(command)
    print(side_name)
    # self.move_dirs = {
    #         ECommandDirection.Up.name: Position(x=0, y=-1),
    #         ECommandDirection.Right.name: Position(x=1, y=0),
    #         ECommandDirection.Down.name: Position(x=0, y=1),
    #         ECommandDirection.Left.name: Position(x=-1, y=0)
    #     }
    
    # if self.world.pacman.health == 0:
    #     return False

    if command.name() == ChangePacmanDirection.name():
        # if it cannot move return false
        print("aaaa")
        print(ChangePacmanDirection.name())
        self.pacman.direction = command.direction
        x = self.pacman.x
        y = self.pacman.y
        # new_position = self.pacman.position
        # if command.direction == ECommandDirection.Right:
        #     new_position = Position(x=x+1, y=y)
        # new_position = self.pacman.position + self.move_dirs[command.direction.name]
        # new_position = Position(x=self.pacman.position.x, y=self.pacman.position.y) + self.move_dirs[command.direction.name]

        # if self.can_move():
        if True:
            return GuiEvent(GuiEventType.MovePacman, (self.pacman.x, self.pacman.y),(self.pacman.x +1, self.pacman.y) )

        else:
            return GuiEvent(GuiEventType.ChangePacmanDirection, (self.pacman.x, self.pacman.y), (self.pacman.x, self.pacman.y))


# def can_move(self, new_position):
#     return True
    # if self.board[new_position.y][new_position.x] == ECell.Wall:
    #     return False
    # # if ghost      
    # else:
    #     return True


World.apply_command = apply_command
# World.can_move = can_move