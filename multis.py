#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv

from center import multiples


def mult(liste: list):
    for arg in liste:
        if type(arg) is int or arg.isdecimal():
            print(str(arg) + ": " + str(multiples(int(arg))))


if __name__ == "__main__":
    mult(argv[1:])
