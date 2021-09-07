#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint
import sys

import reta
from nestedAlx import NestedCompleter
from prompt_toolkit import print_formatted_text, prompt
# from prompt_toolkit.completion import Completer, Completion, WordCompleter
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.styles import Style
from word_completerAlx import WordCompleter

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


def setMainParas(startpunkt: dict, mainParas) -> dict:
    for mainPara1 in mainParas:
        startpunkt[mainPara1] = {}
        for mainPara2 in mainParas:
            startpunkt[mainPara1][mainPara2] = None
    return startpunkt


# startpunkt = setMainParas(startpunkt, mainParas)

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


def nebenToMainPara(startpunkt: dict, zeilen, kombi, spalten, ausgabe) -> dict:
    for nebenPara in zeilen:
        startpunkt["-zeilen"][nebenPara] = None
    for nebenPara in spalten:
        startpunkt["-spalten"][nebenPara] = None
    for nebenPara in kombi:
        startpunkt["-kombination"][nebenPara] = None
    for nebenPara in ausgabe:
        startpunkt["-ausgabe"][nebenPara] = None

    return startpunkt


# startpunkt = nebenToMainPara(
#    startpunkt, zeilenParas, kombiMainParas, spalten, ausgabeParas
# )


def nebenUndMainParas(startpunkt, mainParas, zeilen, kombi, spalten, ausgabe) -> dict:
    startpunkt = setMainParas(startpunkt, mainParas)
    startpunkt = nebenToMainPara(
        startpunkt, zeilenParas, kombiMainParas, spalten, ausgabeParas
    )
    return startpunkt


def nebenMainRekursiv(
    startpunkt, mainParas, zeilen, kombi, spalten, ausgabe, anzahl
) -> dict:
    if anzahl > 0:
        startpunkt = nebenUndMainParas(
            startpunkt, mainParas, zeilen, kombi, spalten, ausgabe
        )
        anzahl -= 1
        for key, value in startpunkt.items():
            startpunkt[key] = nebenUndMainParas(
                nebenMainRekursiv(
                    {}, mainParas, zeilen, kombi, spalten, ausgabe, anzahl
                ),
                mainParas,
                zeilen,
                kombi,
                spalten,
                ausgabe,
            )
    return startpunkt


pp1 = pprint.PrettyPrinter(indent=2)
pp = pp1.pprint
startpunkt = nebenMainRekursiv(
    {"reta": None}, mainParas, zeilenParas, kombiMainParas, spalten, ausgabeParas, 5
)
pp(startpunkt)

# print(str(ausgabeParas))
# Es gibt einen vi mode in dieser lib
# html_completer = WordCompleter(["<html>", "<body>", "<head>", "<title>"])
html_completer = NestedCompleter.from_nested_dict(
    {
        "show": {"version": None, "clock": None, "ip": {"interface": {"brief"}}},
        "bla": {"version": None, "ip": {"interface": {"brief"}}},
        "bla2": {"version": None, spalten[0]: None, "ip": {"interface": {"brief"}}},
    },
    notParameterValues=ausgabeParas + zeilenParas + kombiMainParas + spalten,
)
# pp(ausgabeParas + zeilenParas + kombiMainParas + spalten)

text = prompt(
    # print_formatted_text("Enter HTML: ", sep="", end=""), completer=html_completer
    "Enter HTML: ",
    completer=NestedCompleter.from_nested_dict(
        startpunkt,
        notParameterValues=ausgabeParas + zeilenParas + kombiMainParas + spalten,
    ),
    wrap_lines=False,
    complete_while_typing=True,
    vi_mode=True,
)
print("You said: %s" % text, end=" ")
