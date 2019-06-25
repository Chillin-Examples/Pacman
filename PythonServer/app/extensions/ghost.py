# -*- coding: utf-8 -*-

# project imports
from ..ks.models import ECell, Position, EDirection, Ghost
from ..gui_events import GuiEvent, GuiEventType


def move(self, world):
    gui_events = []
    new_position = self.get_new_position()
    if self.can_move(world, new_position):
        self.position = new_position
        gui_events.append(GuiEvent(GuiEventType.MoveGhost, id=self.id, new_pos=self.position))
    return gui_events


def recover(self, world):
    super(Ghost, self).recover(world)
    return [
        GuiEvent(GuiEventType.ChangeGhostDirection, id=self.id, direction=self.direction),
        GuiEvent(GuiEventType.MoveGhost, id=self.id, new_pos=self.position)
    ]


def kill_pacman(self, world):
    world.scores['Ghost'] += world.constants.pacman_death_score
    world.pacman.health -= 1


def can_change_direction(self, world, new_direction):
    if super(Ghost, self).can_change_direction(world, new_direction) == False:
        return False

    forbidden_direction = new_direction.opponent()
    if self.direction != forbidden_direction:
        # Legal
        return True

    # Forbidden direction
    if self._check_dead_end(world, new_direction):
        return True

    # Forbidden but you have other choices
    return False


def _check_dead_end(self, world, direction):
    exception = self.position.dir_to_pos(direction)
    cells_around = [Position(-1, 0), Position(1, 0), Position(0, 1), Position(0, -1)]
    cells_around.remove(exception)
    # Check if there is a dead end
    for pos in cells_around:
        p = pos + self.position
        if world.board[p.y][p.x] != ECell.Wall:
            return False
    return True


Ghost.move = move
Ghost.recover = recover
Ghost.kill_pacman = kill_pacman
Ghost.can_change_direction = can_change_direction
Ghost._check_dead_end = _check_dead_end
