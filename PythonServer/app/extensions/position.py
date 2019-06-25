# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Position, EDirection

@staticmethod
def dir_to_pos(direction):
    dir_to_pos_map = {
        EDirection.Up: Position(0, -1),
        EDirection.Down: Position(0, +1),
        EDirection.Right: Position(+1, 0),
        EDirection.Left: Position(-1, 0)
    }
    return dir_to_pos_map[direction]


def __eq__(self, other):
    if isinstance(other, Position):
        return self.x == other.x and self.y == other.y
    return NotImplemented


def __ne__(self, other):
    r = self.__eq__(other)
    if r is not NotImplemented:
        return not r
    return NotImplemented


def __hash__(self):
    return hash(tuple(sorted(self.__dict__.items())))


def __add__(self, other):
    if isinstance(other, Position):
        return Position(self.x + other.x, self.y + other.y)
    return NotImplemented


def __iadd__(self, other):
    if isinstance(other, Position):
        self.x += other.x
        self.y += other.y
    return NotImplemented


def __sub__(self, other):
    if isinstance(other, Position):
        return Position(self.x - other.x, self.y - other.y)
    return NotImplemented


def __isub__(self, other):
    if isinstance(other, Position):
        self.x -= other.x
        self.y -= other.y
    return NotImplemented


def __repr__(self):
    return "<x: %s, y: %s>" % (self.x, self.y)


Position.dir_to_pos = dir_to_pos
Position.__eq__ = __eq__
Position.__ne__ = __ne__
Position.__hash__ = __hash__
Position.__add__ = __add__
Position.__iadd__ = __iadd__
Position.__sub__ = __sub__
Position.__isub__ = __isub__
Position.__repr__ = __repr__
