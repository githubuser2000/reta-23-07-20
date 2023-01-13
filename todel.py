#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import json
from copy import deepcopy
from pprint import pprint

from LibRetaPrompt import wahl15


def merge_dicts(dict1, dict2):
    for key in dict2:
        if (
            key in dict1
            and isinstance(dict1[key], dict)
            and isinstance(dict2[key], dict)
        ):
            merge_dicts(dict1[key], dict2[key])
        else:
            if key in dict1:
                if isinstance(dict2[key], dict) and not isinstance(dict1[key], dict):
                    dict1[key] = dict2[key]
            else:
                dict1[key] = dict2[key]
    return dict1


wahlNeu: dict[str, dict] = {}
liste: list[str]
for key, value in wahl15.items():
    liste = key.split("_")
    liste = list(filter(None, liste))
    if len(liste) > 0:
        thing: dict[str, dict] = {}
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

            if thing == {}:
                thing: dict[dict, str]
                thing = {el: {value: None}}
            else:
                thing = {el: thing}

        wahlNeu = merge_dicts(thing, wahlNeu)
        # pprint(wahlNeu)

    # wahlNeu[liste[0]] = value

# wahlNeu2: dict[str, dict] = {}
# wahlNeu2["15"] = wahlNeu

# pprint(json.dumps(wahlNeu2))
pprint(wahlNeu)
