#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

from center import (alxp, cliout, getTextWrapThings, infoLog, output,
                    primzahlvielfachesgalaxie, re, x)
from lib4tables import primMultiple


def multiples(a):
    menge = set()
    for b in range(2, math.floor(math.sqrt(a) + 1)):
        c = a / b * 1000
        c = round(c) / 1000
        if c == round(c):
            menge |= {(int(c), b)}
    return list(menge)


for i in range(1, 10):
    x(str(i), [multiples(i), primMultiple(i)])
