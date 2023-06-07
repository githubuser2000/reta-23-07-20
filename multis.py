#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from sys import argv

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "libs"))
from center import multiples


def mult(liste: list):
    for arg in liste:
        if type(arg) is int or arg.isdecimal():
            print(str(arg) + ": " + str(multiples(int(arg))))


if __name__ == "__main__":
    mult(argv[1:])
