# -*- coding: utf-8 -*-

# project imports
from ks.commands import ECommandDirection, ChangePacmanDirection, ChangeGhostDirection
from ks.models import World, ECell
from gui_events import GuiEvent, GuiEventType

def apply_command(self, side_name, command):

    if command.name() == ChangePacmanDirection.name():
        self.pacman.direction = command.direction
        
        x = self.pacman.x
        y = self.pacman.y
        pacman_position = (x,y)
        new_position = self._calculate_new_pos(command, pacman_position)

        # Check move conditions
        if self._can_move(new_position):
            print("can move")
            return GuiEvent(GuiEventType.MovePacman, pacman_position, new_position)

        else:
            print("cannot move")
            return GuiEvent(GuiEventType.ChangePacmanDirection, pacman_position, pacman_position)
    # ghost 
    # if command.name() == ChangeGhostDirection.name():
    #     self.ghosts[command.id].direction = command.direction

    #     x = self.ghosts[command.id].x
    #     y = self.pacman[command.id].y
    #     ghost_position = (x,y)
    #     new_position = self._calculate_new_pos(command, ghost_position)

        # if self._check_ghost_move_conditions(new_position):
        #     print("can move")
        #     return GuiEvent(GuiEventType.MoveGhost, ghost_position, new_position)

        # else:
        #     print("cannot move")
        #     return GuiEvent(GuiEventType.ChangeGhostDirection, ghost_position, ghost_position)


def _calculate_new_pos(self, command, pre_pos):
    
    if command.direction.name == ECommandDirection.Right.name:
        return (pre_pos[0]+150, pre_pos[1])

    elif command.direction == ECommandDirection.Left:
        return (pre_pos[0]-150, pre_pos[1])

    elif command.direction == ECommandDirection.Up:
        return (pre_pos[0], pre_pos[1]+150)

    elif command.direction == ECommandDirection.Down:
        return (pre_pos[0], pre_pos[1]-150)


def _can_move(self, new_position):
    
    if self.board[(new_position[1]/150)][(new_position[0]/150)] == ECell.Wall:
        return False
      
    else:
        return True


World.apply_command = apply_command
World._can_move = _can_move
World._calculate_new_pos = _calculate_new_pos