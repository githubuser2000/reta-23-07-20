#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint
import re
import sys

pp = pprint.PrettyPrinter(indent=4)


def x(a, text):
    a = str(a)
    if type(text) is str:
        print(a + ": " + text)
    else:
        print(a + ": ")
        pp.pprint(text)


def alxp(text):
    if type(text) is str:
        print(text)
    else:
        pp.pprint(text)


textList = []
for line in sys.stdin:
    textList += [line]

# thing = re.compile("[^>]+[^>]+>[\s\d]+<.*")
thing = re.compile("[^>]+>[^>]+>\s*\d+(.*)")


def differentLetters(text1, text2):
    more = 0
    for t1, t2 in zip(text1, text2):
        if t1 != t2:
            more += 1
    return more


textList2: dict = {}
multiples = set()
for i, line in enumerate(textList):
    # found = thing.findall(line)
    found = line
    if found is not None and len(found) > 0 and i > 0:
        # alxp(i)
        diffi = differentLetters(textList2[i - 1], found[0])
        if diffi != 0:
            multiples |= {i}
        textList2[i] = found[0]
    else:
        textList2[i] = ""
alxp(multiples)
