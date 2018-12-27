#! /usr/bin/env python
# -*- coding: utf-8 -*-

from koala_serializer import generate
import sys
from shutil import copyfile

common_url = '/ks/commmands.ks'
destination = ['../PythonClient'+common_url, '../PythonRandomClient'+common_url, '../CppClient/Game'+common_url]
for dest in destination:
    copyfile('app/ks/commands.ks', dest)

all_args = [('python', 'app/ks', 'snake_case'),
            ('python', '../PythonClient/ks', 'snake_case'),
            ('python', '../PythonRandomClient/ks', 'snake_case'),
            ('cpp', '../CppClient/Game/ks', 'camelCase')]

for args in all_args:
    generate('app/ks/commands.ks', *args)
    generate('app/ks/models.ks', *args)
