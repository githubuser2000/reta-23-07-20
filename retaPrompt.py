#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint
import sys
from copy import deepcopy
from itertools import zip_longest
from typing import Optional

import reta
from nestedAlx import NestedCompleter
from prompt_toolkit import print_formatted_text, prompt
# from prompt_toolkit.completion import Completer, Completion, WordCompleter
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.styles import Style
from word_completerAlx import WordCompleter

pp1 = pprint.PrettyPrinter(indent=2)
pp = pp1.pprint

retaProgram = reta.Program([sys.argv[0]])
mainParas = ["-" + a for a in retaProgram.mainParaCmds]
# print(str(mainParas))
# print(str(retaProgram.paraDict))
spalten = ["--" + a[0] for a in retaProgram.paraDict.keys()]
# print(str(list(spalten)))
# print(str(reta.Program.kombiParaNdataMatrix.values()))
# print(str(reta.Program.kombiParaNdataMatrix2.values()))
#
#
# DAS SOLLTE ICH BESSER ALLES ORDENTLICH IN RETA.PY PACKEN, STATT ES HIER AUSZUSCHREIBEN, WEIL SONST DOPPELT!
# D.H. spezielle DatenTypen dafür in Reta.py anlegen!
# DAS GEHT SCHNELL, FLEIßARBEIT, WEIL KAUM BUGGEFAHR
#
# startpunkt: dict = {}
spaltenDict = {}
for tupel in retaProgram.paraNdataMatrix:
    for haupt in tupel[0]:
        spaltenDict[haupt] = tupel[1]
# pp(spaltenDict)

ausgabeParas = [
    "--nocolor",
    "--art",
    "--onetable",
    "--spaltenreihenfolgeundnurdiese",
]
kombiMainParas = ["--galaxie", "--universum"]
zeilenParas = [
    "--zeit",
    "--zaehlung",
    "--vorhervonausschnitt",
    "--primzahlvielfache",
    "--nachtraeglichdavon",
    "--alles",
    "--potenzenvonzahlen",
    "--typ",
]
hauptForNeben = ("-zeilen", "-spalten", "-kombination", "-ausgabe")

schonDrin = {}
schonDrin2 = []

notParameterValues = (
    ausgabeParas + zeilenParas + kombiMainParas + spalten + mainParas,
)


def setMainParas(startpunkt: dict, mainParas) -> dict:
    for mainPara1 in mainParas:
        merke = NestedCompleter(
            {}, notParameterValues=notParameterValues, optionsStandard={}
        )
        if merke in schonDrin and False:
            # op1 = set()
            # op2 = set()
            # for key, val in schonDrin[merke].options.items():
            #    op1 |= val.options
            # for key, val in merke.options.items():
            #    op2 |= val.options

            # if op1 == op2:
            # if schonDrin[merke].options == merke.options:
            #    startpunkt.options[mainPara1] = schonDrin[merke]
            # else:
            startpunkt.options[mainPara1] = schonDrin[merke]
            # schonDrin2[merke] = merke, op2
        else:
            # startpunkt.options[mainPara1] = merke
            startpunkt.options[mainPara1] = merke
            schonDrin[merke] = merke
    return startpunkt


# startpunkt = setMainParas(startpunkt, mainParas)


def nebenToMainPara(startpunkt: dict, zeilen, kombi, spalten, ausgabe, exPara) -> dict:
    # pp(exPara)
    if exPara == "-zeilen":
        for nebenPara in zeilen:
            startpunkt.options[nebenPara] = NestedCompleter(
                {}, notParameterValues=notParameterValues, optionsStandard={}
            )
    elif exPara == "-spalten":
        # pp(startpunkt.options.keys())
        for nebenPara in spalten:
            startpunkt.options[nebenPara] = NestedCompleter(
                {}, notParameterValues=notParameterValues, optionsStandard={}
            )
    elif exPara == "-kombination":
        for nebenPara in kombi:
            startpunkt.options[nebenPara] = NestedCompleter(
                {}, notParameterValues=notParameterValues, optionsStandard={}
            )
    elif exPara == "-ausgabe":
        for nebenPara in ausgabe:
            startpunkt.options[nebenPara] = NestedCompleter(
                {}, notParameterValues=notParameterValues, optionsStandard={}
            )

    return startpunkt


def valueToNebenPara(
    startpunkt, zeilen, kombi, spalten, ausgabe, newerKey, exPara
) -> dict:
    global spaltenDict, schonDrin2
    if exPara == "-spalten" and newerKey in spalten:
        # pp(spaltenDict)
        # pp(newerKey)
        for nebenPara in ():
            try:
                paraVals = spaltenDict[nebenPara[2:]]
            except KeyError:
                paraVals = ()
            if paraVals is None:
                paraVals = ()
            # pp(nebenPara + " | " + str(paraVals))
            pp(
                {
                    key: value
                    for (key, value) in zip_longest(paraVals, (), fillvalue=None)
                }
            )
            startpunkt.options[nebenPara] = NestedCompleter(
                {
                    key: value
                    for (key, value) in zip_longest(paraVals, (), fillvalue=None)
                },
                notParameterValues=notParameterValues,
                optionsStandard={},
            )
        startpunkt.options2["blub"] = NestedCompleter(
            {}, notParameterValues=notParameterValues, optionsStandard={}
        )
        merke = startpunkt.options2["blub"]
        schonDrin[merke] = merke
        schonDrin[startpunkt] = startpunkt
        schonDrin2 += [startpunkt]
    # elif exPara == "-kombination":
    #    for nebenPara in kombi:
    #        startpunkt.options[nebenPara] = NestedCompleter(
    #            {}, notParameterValues=notParameterValues
    #        )

    return startpunkt


# startpunkt = nebenToMainPara(
#    startpunkt, zeilenParas, kombiMainParas, spalten, ausgabeParas
# )


def nebenUndMainParas(
    startpunkt, mainParas, zeilen, kombi, spalten, ausgabe, exPara, newerKey
) -> dict:
    startpunkt = setMainParas(startpunkt, mainParas)
    startpunkt = nebenToMainPara(
        startpunkt, zeilenParas, kombiMainParas, spalten, ausgabeParas, exPara
    )
    startpunkt = valueToNebenPara(
        startpunkt, zeilenParas, kombiMainParas, spalten, ausgabeParas, newerKey, exPara
    )
    return startpunkt


def nebenMainRekursiv(
    startpunkt, key, mainParas, zeilen, kombi, spalten, ausgabe, anzahl, lastKey=None
) -> dict:
    global schonDrin2
    if anzahl > 0:
        # pp(key)
        schonDrin2 += [startpunkt]
        if startpunkt.options[key] is None:
            startpunkt.options[key] = NestedCompleter(
                {}, notParameterValues, optionsStandard={}
            )
        startpunkt = startpunkt.options[key]
        # pp(startpunkt.options.keys())
        # pp(key)
        newerKey = key
        if lastKey in hauptForNeben and key not in hauptForNeben:
            key = lastKey
        if key in hauptForNeben:
            lastKey = key
        startpunkt = nebenUndMainParas(
            startpunkt, mainParas, zeilen, kombi, spalten, ausgabe, key, newerKey
        )
        # pp((startpunkt).values())
        for key2 in deepcopy(tuple(startpunkt.options.keys())):
            nebenMainRekursiv(
                startpunkt,
                key2,
                mainParas,
                zeilen,
                kombi,
                spalten,
                ausgabe,
                anzahl - 1,
                lastKey,
            ),
    return startpunkt


def nochMalTraverse(startpunkt, anzahl):
    if anzahl > 0:
        if True:
            gleiche = []
            for sd2 in schonDrin2:
                if (
                    sd2.options.keys() == startpunkt.options.keys()
                    and sd2.options2.keys() == startpunkt.options2.keys()
                ):
                    gleiche += [sd2]
            maxis = {}
            for k, gleich1 in enumerate(gleiche):
                amount1 = 0
                maxamount = 0
                maxkey = None
                for v1 in gleich1.options.values():
                    if type(v1) == Optional[Completer]:
                        amount1 += 1
                for v1 in gleich1.options2.values():
                    if type(v1) == Optional[Completer]:
                        amount1 += 1
                if maxamount < amount1:
                    maxamount = amount1
                    maxkey = k
                maxis[maxkey] = maxamount
            if maxis == {}:
                pp(startpunkt.options)
            maxkey = max(maxis, key=maxis.get)
            startpunkt.options = gleiche[k].options

            # for gleich2 in gleiche:

        for key in startpunkt.options.keys():
            startpunkt2 = startpunkt.options[key]
            nochMalTraverse(startpunkt2, anzahl - 1)
    return startpunkt


anzahl = 3
startpunkt1 = NestedCompleter({"reta": None}, notParameterValues, optionsStandard={})
startpunkt = nebenMainRekursiv(
    startpunkt1,
    "reta",
    mainParas,
    zeilenParas,
    kombiMainParas,
    spalten,
    ausgabeParas,
    anzahl,
)
startpunkt = nochMalTraverse(startpunkt, anzahl)
# pp(startpunkt)

# print(str(ausgabeParas))
# html_completer = WordCompleter(["<html>", "<body>", "<head>", "<title>"])
# html_completer = NestedCompleter.from_nested_dict(
#    {
#        "show": {"version": None, "clock": None, "ip": {"interface": {"brief"}}},
#        "bla": {"version": None, "ip": {"interface": {"brief"}}},
#        "bla2": {"version": None, spalten[0]: None, "ip": {"interface": {"brief"}}},
#    },
#    notParameterValues=notParameterValues,
# )
# pp(ausgabeParas + zeilenParas + kombiMainParas + spalten)

# pp(len(schonDrin))
if True:
    text = prompt(
        # print_formatted_text("Enter HTML: ", sep="", end=""), completer=html_completer
        "Enter HTML: ",
        # completer=NestedCompleter.from_nested_dict(
        #    startpunkt, notParameterValues=notParameterValues
        # ),
        completer=startpunkt1,
        wrap_lines=False,
        complete_while_typing=True,
        vi_mode=True,
    )
    print("You said: %s" % text, end=" ")
