#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
# import numpy as np
import html
import json
import platform
import re
from collections import OrderedDict, namedtuple
from itertools import zip_longest
from typing import Optional, Union

try:
    from orderedset import OrderedSet
except:
    OrderedSet = set

import pprint

from center import Primzahlkreuz_pro_contra_strs, retaHilfe

a = {a: {a / 2, a / 5, a / 3} for a in range(61)}

c = {}
for i, d in a.items():
    flag = False
    for b in d:
        if b == round(b):
            flag = True
    if flag:
        c[i] = b
pp = pprint.PrettyPrinter(indent=4)
pp(str(c))
