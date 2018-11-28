# -*- coding: utf-8 -*-

# project imports
from ks.commands import ECommandDirection, ChangePacmanDirection, ChangeGhostDirection
from ks.models import World, ECell
from gui_events import GuiEvent, GuiEventType

def apply_command(self, side_name, command):

    
    print(command)
    if command.name() == ChangePacmanDirection.name():
        self.pacman.direction = command.direction
        
        x = self.pacman.x
        y = self.pacman.y
        pacman_position = (x,y)
        new_position = self._calculate_new_pos(command, pacman_position)

        if self._can_move(new_position):
            print("can_move")
            return GuiEvent(GuiEventType.MovePacman, pacman_position, new_position)

        else:
            print("Cannot move")
            return GuiEvent(GuiEventType.ChangePacmanDirection, pacman_position, pacman_position)

    if command.name() == ChangeGhostDirection.name():
        self.ghosts[command.id].direction = command.direction

def _calculate_new_pos(self, command, pacman_position):
    
    if command.direction.name == ECommandDirection.Right.name:
        return (pacman_position[0]+150, pacman_position[1])

    elif command.direction == ECommandDirection.Left:
        return (pacman_position[0]-150, pacman_position[1])

    elif command.direction == ECommandDirection.Up:
        return (pacman_position[0], pacman_position[1]+150)

    elif command.direction == ECommandDirection.Down:
        return (pacman_position[0], pacman_position[1]-150)

def _can_move(self, new_position):
    
    if self.board[(new_position[1]/150)][(new_position[0]/150)] == ECell.Wall:
        return False
      
    else:
        return True


World.apply_command = apply_command
World._can_move = _can_move
World._calculate_new_pos = _calculate_new_pos