#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv

from lib4tables import multiples


def mult(liste: list):
    for arg in liste:
        if type(arg) is int or arg.isdecimal():
            print(str(multiples(int(arg))))


if __name__ == "__main__":
    mult(argv[1:])
