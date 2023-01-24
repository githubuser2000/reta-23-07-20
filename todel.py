#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import pprint

from lib4tables import primMultiple

a = {a: {a / 2, a / 5, a / 3} for a in range(61)}

c = {}
for i, d in a.items():
    flag = False
    for b in d:
        if b == round(b):
            flag = True
    if flag:
        c[i] = b
pp = pprint.PrettyPrinter(indent=4).pprint
a1 = 0
f = []
for a in c.keys():
    f += [a - a1]
    a1 = a

f3 = f.count(1)
f4 = f.count(2)

pp(str(f))
pp(str(f3))
pp(str(f4))
t = set(c.keys()) ^ set(range(61))
pp(str(t))
pp(str(len(t)))


a = {a: {a / 2, a / 5, a / 3} for a in range(61)}
k = {a: primMultiple(a) for a in range(61)}
pp(k)
