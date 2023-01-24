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
j = {}

for i, a in k.items():
    if i not in t:
        j[i] = a[1:]

l = set()
for a in j.values():
    for b in a:
        l |= {*b}


pp(l - t)
pp(
    'ungefähr Nicht-Primzahlen innerhalb 1 bis 30 ohne "Primzahlen zwischen 1 bis 30 aber mit 2,3,5"'
)

pp("das sind " + str(len(l - t)) + " Stück")
pp(
    "Diese setzen sich aus einem Polynom zusammen f(x1,x2,x3) = a + b*2^x1 + c*3^x2 + d*5^x3"
)
pp(
    "Die Potenzen könnte man noch raus-bekommen, zur Vereinfachung, indem man sie ausrechnet, sodas man keinen Exponenten mehr braucht. So sparrt man 3 Zahlen bei so einer Schreibweise."
)
u = {}
for a in l:
    u[a] = primMultiple(a)[1:]

pp(u)
pp(
    "Das wurde oben gemacht und deshalb sind diese 22 Zeichen so: f(x1,x2,x3) = a + b*2+c*2 + d*3 + e*5"
)
pp(
    "Das sind also 5 Zahlen, um eine Zahl darzustellen, um nur 22 Zeichen zu benötigen, wenn man eine Basis 60 haben möchte, statt 10, wie es bei unseren alltäglichen Dezimalzahlen wäre."
)
