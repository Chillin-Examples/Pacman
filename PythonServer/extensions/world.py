# -*- coding: utf-8 -*-

# project imports
from ks.commands import ECommandDirection, ChangePacmanDirection
from ks.models import World
from gui_events import GuiEvent, GuiEventType

def apply_command(self, side_name, command):

    # if self.world.pacman.health == 0:
    #     return False

    if command.name() == ChangePacmanDirection.name():
        self.pacman.direction = command.direction
        
        x = self.pacman.x
        y = self.pacman.y
        
        pacman_position = (x,y)
        print(pacman_position)
        new_position = pacman_position + self._calculate_new_pos(command, x, y)
       
        if self._can_move(new_position):
            return GuiEvent(GuiEventType.MovePacman, pacman_position, new_position)

        else:
            return GuiEvent(GuiEventType.ChangePacmanDirection, pacman_position, pacman_position)

def _calculate_new_pos(self, command, x, y):
    print(x)
    if command.direction == ECommandDirection.Right:
        return (150,0)
    elif command.direction == ECommandDirection.Left:
            return (x-150, y)
    elif command.direction == ECommandDirection.Up:
            return (x, y+150)
    elif command.direction == ECommandDirection.Down:
            return (x, y-150)

def _can_move(self, new_position):
    
    if self.board[new_position.y][new_position.x] == ECell.Wall:
        return False
    # if ghost      
    else:
        return True


World.apply_command = apply_command
World._can_move = _can_move
World._calculate_new_pos = _calculate_new_pos