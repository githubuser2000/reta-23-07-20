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

textList2 = {}
multiples = set()
for i, line in enumerate(textList):
    found = thing.findall(line)
    if found is not None and len(found) > 0:
        if found[0] in textList2.values():
            multiples |= {i}
        textList2[i] = found[0]

alxp(multiples)
