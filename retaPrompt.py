#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint
import sys
from copy import deepcopy

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
# print(str(retaProgram.paraDict.keys()))
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


notParameterValues = (
    ausgabeParas + zeilenParas + kombiMainParas + spalten + mainParas,
)


def setMainParas(startpunkt: dict, mainParas) -> dict:
    for mainPara1 in mainParas:
        startpunkt[mainPara1] = {}
    return startpunkt


# startpunkt = setMainParas(startpunkt, mainParas)


def nebenToMainPara(startpunkt: dict, zeilen, kombi, spalten, ausgabe, exPara) -> dict:
    if exPara == "-zeilen":
        for nebenPara in zeilen:
            startpunkt[nebenPara] = NestedCompleter(
                {},
            )
    elif exPara == "-spalten":
        for nebenPara in spalten:
            startpunkt[nebenPara] = {}
    elif exPara == "-kombination":
        for nebenPara in kombi:
            startpunkt[nebenPara] = {}
    elif exPara == "-ausgabe":
        for nebenPara in ausgabe:
            startpunkt[nebenPara] = {}

    return startpunkt


# startpunkt = nebenToMainPara(
#    startpunkt, zeilenParas, kombiMainParas, spalten, ausgabeParas
# )


def nebenUndMainParas(
    startpunkt, mainParas, zeilen, kombi, spalten, ausgabe, exPara
) -> dict:
    startpunkt = setMainParas(startpunkt, mainParas)
    startpunkt = nebenToMainPara(
        startpunkt, zeilenParas, kombiMainParas, spalten, ausgabeParas, exPara
    )
    return startpunkt


def nebenMainRekursiv(
    startpunkt, key, mainParas, zeilen, kombi, spalten, ausgabe, anzahl
) -> dict:
    if anzahl > 0:
        # pp(key)
        startpunkt = nebenUndMainParas(
            startpunkt, mainParas, zeilen, kombi, spalten, ausgabe, key
        )
        # pp((startpunkt).values())
        for key in deepcopy(tuple(startpunkt.keys())):
            nebenMainRekursiv(
                startpunkt[key],
                key,
                mainParas,
                zeilen,
                kombi,
                spalten,
                ausgabe,
                anzahl - 1,
            ),
    return startpunkt


startpunkt: dict = {"reta": {}}
startpunkt = nebenMainRekursiv(
    startpunkt,
    "reta",
    mainParas,
    zeilenParas,
    kombiMainParas,
    spalten,
    ausgabeParas,
    5,
)
# pp(startpunkt)

# print(str(ausgabeParas))
# Es gibt einen vi mode in dieser lib
# html_completer = WordCompleter(["<html>", "<body>", "<head>", "<title>"])
html_completer = NestedCompleter.from_nested_dict(
    {
        "show": {"version": None, "clock": None, "ip": {"interface": {"brief"}}},
        "bla": {"version": None, "ip": {"interface": {"brief"}}},
        "bla2": {"version": None, spalten[0]: None, "ip": {"interface": {"brief"}}},
    },
    notParameterValues=notParameterValues,
)
# pp(ausgabeParas + zeilenParas + kombiMainParas + spalten)


if True:
    text = prompt(
        # print_formatted_text("Enter HTML: ", sep="", end=""), completer=html_completer
        "Enter HTML: ",
        completer=NestedCompleter.from_nested_dict(
            startpunkt, notParameterValues=notParameterValues
        ),
        wrap_lines=False,
        complete_while_typing=True,
        vi_mode=True,
    )
    print("You said: %s" % text, end=" ")
