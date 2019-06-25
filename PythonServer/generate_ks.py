#! /usr/bin/env python
# -*- coding: utf-8 -*-

# python imports
import os
from shutil import copyfile

# chillin imports
from koala_serializer import generate


commands_reletive_dir = 'ks/commands.ks'
models_reletive_dir = 'ks/models.ks'
destinations = [
    '../PythonClient',
    '../PythonRandomClient',
    '../CppClient/Game'
]

for dest in destinations:
    copyfile('app/ks/commands.ks', os.path.join(dest, commands_reletive_dir))
    copyfile('app/ks/models.ks', os.path.join(dest, models_reletive_dir))

all_args = [
    ('python', 'app/ks', 'snake_case'),
    ('python', '../PythonClient/ks', 'snake_case'),
    ('python', '../PythonRandomClient/ks', 'snake_case'),
    ('cpp', '../CppClient/Game/ks', 'camelCase')
]

for args in all_args:
    generate('app/ks/commands.ks', *args)
    generate('app/ks/models.ks', *args)
