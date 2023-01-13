#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import json
from copy import deepcopy
from pprint import pprint

from LibRetaPrompt import wahl15

wahlNeu: dict[str, dict] = {}
liste: list[str]
for key, value in wahl15.items():
    liste = key.split("_")
    liste = list(filter(None, liste))
    if len(liste) > 0:
        thing: dict[str, dict] = {}
        # wahl: dict[str, dict] = wahlNeu
        adresse1 = []
        for el in reversed(liste):
            adresse1 += [el]
            el = el.replace("pro", "/")

            vorherSchonDrin = deepcopy(thing)
            # print(adresse1)
            flag = False
            for adresse in adresse1[:-1]:
                if vorherSchonDrin is not None and type(vorherSchonDrin) is not str:
                    try:
                        vorherSchonDrin = vorherSchonDrin[adresse]
                    except KeyError:
                        if flag:
                            vorherSchonDrin = None
                flag = True
            if type(vorherSchonDrin) is str:
                vorherSchonDrin = None
            if vorherSchonDrin is not None:
                print(vorherSchonDrin.items())

            if thing == {}:
                thing: dict[dict, str]
                thing = {el: value}
            else:
                thing = {el: thing}

        wahlNeu |= thing

    # wahlNeu[liste[0]] = value

wahlNeu2: dict[str, dict] = {}
wahlNeu2["15"] = wahlNeu

# pprint(json.dumps(wahlNeu2))
# pprint(wahlNeu2)
