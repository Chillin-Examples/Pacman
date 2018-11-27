[ECommandDirection]
_def = enum <byte>
    {
        Up,
        Right,
        Down,
        Left
    }


[ChangePacmanDirection]
_def = class
id = int
direction = ECommandDirection


[ChangeGhostDirection]
_def = class 
id = int
direction = ECommandDirection
