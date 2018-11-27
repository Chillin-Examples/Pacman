# -*- coding: utf-8 -*-

# project imports
from ks.commands import ECommandDirection
from ks.models import World, Position


def apply_command(self, side_name, command):
    print(command)
    print(side_name)
    self.move_dirs = {
            ECommandDirection.Up.name: Position(x=0, y=-1),
            ECommandDirection.Right.name: Position(x=1, y=0),
            ECommandDirection.Down.name: Position(x=0, y=1),
            ECommandDirection.Left.name: Position(x=-1, y=0)
        }
    
    # if self.world.pacman.health == 0:
    #     return False

    if command.name() == ChangePacmanDirection.name():
        # if it cannot move return false
        world.pacman.direction = command.direction

        new_position = Pos(position=pacman.position) + self.move_dirs[command.direction.name]

        if self.can_move():
            return GuiEvent(GuiEventType.MovePacman, pacman.position, new_position)

        else:
            return GuiEvent(GuiEventType.ChangePacmanDirection, pacman.position, pacman.position)


def can_move(self):

    if self.world.board[new_position.y][new_position.x] == ECell.Wall:
        return False
    # if ghost      
    else:
        return True


World.apply_command = apply_command
