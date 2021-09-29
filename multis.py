#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv

from lib4tables import multiples

for arg in argv[1:]:
    if arg.isdecimal():
        zahl = int(arg)
