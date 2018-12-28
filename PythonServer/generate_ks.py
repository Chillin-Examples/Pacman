#! /usr/bin/env python
# -*- coding: utf-8 -*-

from koala_serializer import generate
from shutil import copyfile

commands_reletive_dir = '/ks/commmands.ks'
models_reletive_dir = '/ks/models.ks'
destination = ['../PythonClient',
               '../PythonRandomClient',
               '../CppClient/Game']
for dest in destination:
    copyfile('app/ks/commands.ks', dest + commands_reletive_dir)
    copyfile('app/ks/models.ks', dest + models_reletive_dir)

all_args = [('python', 'app/ks', 'snake_case'),
            ('python', '../PythonClient/ks', 'snake_case'),
            ('python', '../PythonRandomClient/ks', 'snake_case'),
            ('cpp', '../CppClient/Game/ks', 'camelCase')]

for args in all_args:
    generate('app/ks/commands.ks', *args)
    generate('app/ks/models.ks', *args)
