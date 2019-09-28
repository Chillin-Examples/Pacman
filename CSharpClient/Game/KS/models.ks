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


[Position]
_def = class
x = int
y = int


[Agent]
_def = class
position = Position
direction = EDirection


[Pacman]
_def = class(Agent)
health = int
giant_form_remaining_time = int


[Ghost]
_def = class(Agent)
id = int


[World]
_def = class
width = int
height = int
board = list<list<ECell>>
scores = map<string, int>
pacman = Pacman
ghosts = list<Ghost>
constants = Constants
