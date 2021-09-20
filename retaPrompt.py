#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pprint
import subprocess
import sys
from copy import deepcopy
from itertools import zip_longest
from typing import Optional

# import reta
from nestedAlx import (ComplSitua, NestedCompleter, ausgabeParas,
                       hauptForNeben, kombiMainParas, mainParas,
                       notParameterValues, reta, retaProgram, spalten,
                       spaltenDict, zeilenParas)
from prompt_toolkit import PromptSession, print_formatted_text, prompt
# from prompt_toolkit.completion import Completer, Completion, WordCompleter
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style
from word_completerAlx import WordCompleter

ColumnsRowsAmount, shellRowsAmountStr = (
    os.popen("stty size", "r").read().split()
)  # Wie viele Zeilen und Spalten hat die Shell ?

session = PromptSession(
    history=FileHistory(os.path.expanduser("~") + os.sep + ".ReTaPromptHistory")
)

pp1 = pprint.PrettyPrinter(indent=2)
pp = pp1.pprint

schonDrin = {}
schonDrin2 = []


def setMainParas(
    startpunkt: NestedCompleter, mainParas, complSit: ComplSitua, exPara: str
) -> NestedCompleter:
    for mainPara1 in mainParas:
        merke = NestedCompleter({}, notParameterValues, {}, complSit, exPara, {})
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
            startpunkt.optionsTypes[mainPara1] = ComplSitua.hauptPara
            schonDrin[merke] = merke
    return startpunkt


# startpunkt = setMainParas(startpunkt, mainParas)


def nebenToMainPara(
    startpunkt: NestedCompleter,
    zeilen,
    kombi,
    spalten,
    ausgabe,
    exPara,
    complSit: ComplSitua,
) -> NestedCompleter:
    # pp(exPara)
    if exPara == "-zeilen":
        for nebenPara in zeilen:
            startpunkt.options[nebenPara] = NestedCompleter(
                {}, notParameterValues, {}, complSit, exPara, {}
            )
    elif exPara == "-spalten":
        # pp(startpunkt.options.keys())
        for nebenPara in spalten:
            startpunkt.options[nebenPara] = NestedCompleter(
                {}, notParameterValues, {}, complSit, exPara, {}
            )
    elif exPara == "-kombination":
        for nebenPara in kombi:
            startpunkt.options[nebenPara] = NestedCompleter(
                {}, notParameterValues, {}, complSit, exPara, {}
            )
    elif exPara == "-ausgabe":
        for nebenPara in ausgabe:
            startpunkt.options[nebenPara] = NestedCompleter(
                {}, notParameterValues, {}, complSit, exPara, {}
            )

    return startpunkt


def valueToNebenPara(
    startpunkt: NestedCompleter,
    zeilen,
    kombi,
    spalten,
    ausgabe,
    newerKey,
    exPara,
    complSit: ComplSitua = ComplSitua.unbekannt,
) -> NestedCompleter:
    global spaltenDict, schonDrin2
    if exPara == "-spalten" and newerKey in spalten:
        # pp(spaltenDict)
        # pp(newerKey)
        # for nebenPara in spalten:
        for nebenPara in ("--planet", "--Planet"):
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
            startpunkt.options2[nebenPara] = NestedCompleter(
                {
                    key: value
                    for (key, value) in zip_longest(paraVals, (), fillvalue=None)
                },
                notParameterValues=notParameterValues,
                optionsStandard={},
            )
            # merke = startpunkt.options2[nebenPara]
            # schonDrin[merke] = merke
            schonDrin[startpunkt] = startpunkt
            schonDrin2 += [startpunkt]
        # startpunkt.options2["blub"] = NestedCompleter(
        #    {}, notParameterValues=notParameterValues, optionsStandard={}
        # )
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
    startpunkt,
    mainParas,
    zeilen,
    kombi,
    spalten,
    ausgabe,
    exPara,
    newerKey,
    complSit: ComplSitua = ComplSitua.unbekannt,
) -> dict:
    startpunkt = setMainParas(startpunkt, mainParas, complSit, exPara)
    startpunkt = nebenToMainPara(
        startpunkt, zeilenParas, kombiMainParas, spalten, ausgabeParas, exPara, complSit
    )
    startpunkt = valueToNebenPara(
        startpunkt,
        zeilenParas,
        kombiMainParas,
        spalten,
        ausgabeParas,
        newerKey,
        exPara,
        complSit,
    )
    return startpunkt


def nebenMainRekursiv(
    startpunkt,
    key,
    mainParas,
    zeilen,
    kombi,
    spalten,
    ausgabe,
    anzahl,
    lastKey=None,
    complSit: ComplSitua = ComplSitua.unbekannt,
) -> dict:
    global schonDrin2
    if anzahl > 0:
        # pp(key)
        schonDrin2 += [startpunkt]
        if startpunkt.options[key] is None:
            startpunkt.options[key] = NestedCompleter(
                {}, notParameterValues, {}, complSit, key, {}
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
            startpunkt,
            mainParas,
            zeilen,
            kombi,
            spalten,
            ausgabe,
            key,
            newerKey,
            complSit,
        )
        # pp((startpunkt).values())
        for key2, key3 in zip(
            deepcopy(tuple(startpunkt.options.keys())),
            deepcopy(tuple(startpunkt.optionsTypes.keys())),
        ):
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
                key3,
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

            try:
                maxkey = max(maxis, key=maxis.get)
                startpunkt.options = gleiche[k].options
            except ValueError:
                pass
            #
            # for gleich2 in gleiche:

        for key in startpunkt.options.keys():
            startpunkt2 = startpunkt.options[key]
            nochMalTraverse(startpunkt2, anzahl - 1)
    return startpunkt


anzahl = 3
startpunkt1 = NestedCompleter(
    {"reta": None},
    notParameterValues,
    {},
    ComplSitua.retaAnfang,
    "",
    {"reta": ComplSitua.retaAnfang},
    None,
)

# startpunkt = nebenMainRekursiv(
# startpunkt1,
# "reta",
# mainParas,
# zeilenParas,
# kombiMainParas,
# spalten,
# ausgabeParas,
# anzahl,
# ComplSitua.retaAnfang,
# )
# startpunkt = nochMalTraverse(startpunkt, anzahl)
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
text = None
print(
    sys.argv[0].split(os.sep)[-1]
    + " starten mit Parameter -vi für ViMode, beenden mit q, exit, quit"
)
print("Tippe reta ein!")
while text not in ("ende", "exit", "quit", "q", ""):
    text = session.prompt(
        # print_formatted_text("Enter HTML: ", sep="", end=""), completer=html_completer
        ">",
        # completer=NestedCompleter.from_nested_dict(
        #    startpunkt, notParameterValues=notParameterValues
        # ),
        completer=startpunkt1,
        wrap_lines=False,
        complete_while_typing=True,
        vi_mode=True if "-vi" in sys.argv else False,
    )
    # print("Du meintest: %s" % text, end=" ")
    stext = text.split()
    if len(stext) > 0 and stext[0] == "reta":
        import reta

        reta.Program(stext, ColumnsRowsAmount)

        # process = subprocess.Popen(stext)
        # process.wait()
