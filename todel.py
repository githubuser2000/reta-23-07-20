#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import json
from pprint import pprint

from LibRetaPrompt import wahl15

wahlNeu: dict[str, dict] = {}
liste: list[str]
for key, value in wahl15.items():
    liste = key.split("_")
    liste = list(filter(None, liste))
    if len(liste) > 0:
        thing: dict[str, dict] = {}
        wahl: dict[str, dict] = wahlNeu
        for el in reversed(liste):
            el = el.replace("pro", "/")
            if thing == {}:
                thing: dict[dict, str]
                thing = {el: value}
            if thing != {}:
                try:
                    if type(wahl) is dict and wahl[el] == value:
                        thing = {el: thing}
                        thing |= {el: value}
                        wahl = wahl[el]
                    else:
                        thing = {el: thing}
                        if type(wahl) is dict:
                            wahl = wahl[el]
                except:
                    thing = {el: thing}
        wahlNeu |= thing

    # wahlNeu[liste[0]] = value

wahlNeu2: dict[str, dict] = {}
wahlNeu2["15"] = wahlNeu

# pprint(json.dumps(wahlNeu2))
pprint(wahlNeu2)
