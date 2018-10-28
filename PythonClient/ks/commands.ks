[EDirection]
_def = enum <byte>
    {
        Up,
        Right,
        Down,
        Left
    }


[ChangePacmanDirection]
_def = class 
direction = EDirection


[ChangeGhostDirection]
_def = class 
id = int
direction = EDirection
