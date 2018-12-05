[ECell]
_def = enum <byte>
    {
        Empty,
        Food,
        SuperFood,
        Wall
    }


[EDirection]
_def = enum <byte>
    {
        Up,
        Right,
        Down,
        Left
    }


[Constants]
_def = class
food_score = int
super_food_score = int
ghost_death_score = int 
pacman_death_score = int
pacman_giant_form_duration = int
max_cycles = int


[Pacman]
_def = class
x = int
y = int
direction = EDirection
health = int
giant_form_remaining_time = int
init_x = int
init_y = int
init_direction = EDirection


[Ghost]
_def = class
x = int
y = int
id = int
direction = EDirection
init_x = int
init_y = int
init_direction = EDirection


[World]
_def = class
width = int
height = int
board = list<list<ECell>>
scores = map<string, int>
pacman = Pacman
ghosts = list<Ghost>
constants = Constants
