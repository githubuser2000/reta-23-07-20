#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import difflib
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
    moreless = 0
    bla = ""
    for i, t1 in enumerate(text1):
        if i + moreless < len(text2) and t1 == text2[i + moreless]:
            more += 1
        elif i + 1 < len(text2) and t1 == text2[i + 1 + moreless]:
            moreless += 1
            more += 1
        elif i - 1 < len(text2) and t1 == text2[i - 1 + moreless]:
            moreless -= 1
            more += 1
        elif i + 2 < len(text2) and t1 == text2[i + 2 + moreless]:
            moreless += 2
            more += 1
        elif i - 2 < len(text2) and t1 == text2[i - 2 + moreless]:
            moreless -= 2
            more += 1
        else:
            bla += text2[i + moreless]
    alxp(bla)
    return more


textList2: dict = {}
multiples = set()
for i, line in enumerate(textList):
    textList2[i] = line
    if i > 0:
        diffi = differentLetters(textList2[i - 1], line)
        alxp(diffi)
    else:
        diffi = len(line)
    if diffi < 10:
        multiples |= {i}
# alxp(multiples)
