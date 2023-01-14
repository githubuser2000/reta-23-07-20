#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from copy import deepcopy
from functools import cmp_to_key
from pprint import pprint

from LibRetaPrompt import wahl15


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


wahlNeu: dict[str, dict] = OrderedDict()
liste: list[str]
for key, value in wahl15.items():
    liste = key.split("_")
    liste = list(filter(None, liste))
    if len(liste) > 0:
        thing: dict[str, dict] = OrderedDict()

        # wahl: dict[str, dict] = wahlNeu
        # adresse1 = []
        # adresse2 = []
        for el in reversed(liste):
            el = el.replace("pro", "/")
            # adresse1 += [el]

            # vorherSchonDrin = deepcopy(wahlNeu)
            ## pprint(vorherSchonDrin)
            # for adresse in reversed(adresse1):
            #    if vorherSchonDrin is not None and type(vorherSchonDrin) is not str:
            #        # print(adresse)
            #        # print(adresse1)
            #        # print(vorherSchonDrin.keys())
            #        adresse2 += [adresse]
            #        try:
            #            vorherSchonDrin = vorherSchonDrin[adresse]
            #        except KeyError:
            #            # print("ERR" + str(adresse))
            #            vorherSchonDrin = None
            # if type(vorherSchonDrin) is str:
            #    vorherSchonDrin = None
            # print(adresse1)
            # print(adresse2)
            # if vorherSchonDrin is not None:
            # print(vorherSchonDrin.items())

            if thing == OrderedDict():
                thing: dict[dict, str]
                thing = {el: OrderedDict({value: None})}
            else:
                thing = {el: thing}

        wahlNeu = merge_dicts(thing, wahlNeu)
        # pprint(wahlNeu)

    # wahlNeu[liste[0]] = value


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
        return int(value1) - int(value2)
    elif isNumber1 and not isNumber2:
        return 1
    elif not isNumber1 and isNumber2:
        return -1
    else:
        return value1 > value2


wahlNeu2: OrderedDict[str, dict] = OrderedDict()
wahlNeu2["15"] = OrderedDict(sorted(wahlNeu.items(), key=cmp_to_key(cmpx)))


# pprint(json.dumps(wahlNeu2))
pprint(wahlNeu2)
