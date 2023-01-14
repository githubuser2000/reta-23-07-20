#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from copy import deepcopy
from functools import cmp_to_key
from pprint import pprint

from LibRetaPrompt import wahl15


def cmp_before(value):
    value = value[0]
    isNumber: bool = True
    if "/" in value:
        a = value.split("/")[-1]
        if a.isdecimal():
            toSort = a
        else:
            isNumber = False
    elif value.isdecimal():
        toSort = value
    else:
        isNumber = False
    if not isNumber:
        toSort = value
    return isNumber, toSort


def cmpx(erster, zweiter):
    isNumber1, value1 = cmp_before(erster)
    isNumber2, value2 = cmp_before(zweiter)
    if isNumber1 and isNumber2:
        value1 = int(value1)
        value2 = int(value2)
        if value1 == value2:
            if "/" in erster[0]:
                return 1
            elif "/" in zweiter[0]:
                return -1
            else:
                return 0
        else:
            return value1 - value2
    elif isNumber1 and not isNumber2:
        return 1
    elif not isNumber1 and isNumber2:
        return -1
    else:
        return value1 > value2


def merge_dicts(dict1, dict2):
    for key in dict2:
        if (
            key in dict1
            and isinstance(dict1[key], OrderedDict)
            and isinstance(dict2[key], OrderedDict)
        ):
            merge_dicts(dict1[key], dict2[key])
        else:
            if key in dict1:
                if isinstance(dict2[key], OrderedDict) and not isinstance(
                    dict1[key], OrderedDict
                ):
                    dict1[key] = dict2[key]
            else:
                dict1[key] = dict2[key]
    return dict1


def traverseHierarchy(liste, thing, listenIndex):
    # print(listenIndex)
    # print(liste[listenIndex:])
    print(tuple(reversed(liste))[listenIndex:])
    for knoten in tuple(reversed(liste))[listenIndex:]:
        knoten = knoten.replace("pro", "/")
        # print(liste)
        # print(knoten)
        # print(thing.keys())
        if knoten not in thing or type(thing[knoten]) is not str:
            # print("SDASDFGGFGFSGSDFG")
            thing = {knoten: thing}
            thing = traverseHierarchy(liste, thing, listenIndex + 1)
        else:
            thing: dict[dict, list]
            newKeys = value.split(",")
            newValues = [None] * len(newKeys)
            thing = {knoten: OrderedDict(zip(newKeys, newValues))}
    return thing


wahlNeu: dict[str, dict] = OrderedDict(sorted({}.items(), key=cmp_to_key(cmpx)))

liste: list[str]
for key, value in wahl15.items():
    liste = key.split("_")
    liste = list(filter(None, liste))
    thing: dict[str, dict] = OrderedDict(sorted({}.items(), key=cmp_to_key(cmpx)))
    if len(liste) > 0:
        thing = traverseHierarchy(liste, thing, 0)
        wahlNeu = merge_dicts(thing, wahlNeu)


wahlNeu2: OrderedDict[str, dict] = OrderedDict()
wahlNeu2["15"] = OrderedDict(sorted(wahlNeu.items(), key=cmp_to_key(cmpx)))


# pprint(json.dumps(wahlNeu2))
pprint(wahlNeu2)


# print("<br>BLAAAAAAAAAAAAAAAAA<br>")


def myprint(d):
    for k, v in d.items():
        print(
            '<div  style="white-space: normal; border-left: 40px solid rgba(0, 0, 0, .0);">',
            end="",
        )
        print('<input type="checkbox">', end="")
        print("{0}".format(k), end="")
        if v is not None:
            myprint(v)
        print("</input>", end="")
        print("</div>", end="")


# myprint(wahlNeu2)
