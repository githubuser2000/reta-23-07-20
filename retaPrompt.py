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

schonDrin = {}
schonDrin2 = {}

notParameterValues = (
    ausgabeParas + zeilenParas + kombiMainParas + spalten + mainParas,
)


def setMainParas(startpunkt: dict, mainParas) -> dict:
    for mainPara1 in mainParas:
        merke = NestedCompleter({}, notParameterValues=notParameterValues)
        if merke in schonDrin:
            # op1 = set()
            # op2 = set()
            # for key, val in schonDrin[merke].options.items():
            #    op1 |= val.options
            # for key, val in merke.options.items():
            #    op2 |= val.options

            # if op1 == op2:
            if schonDrin[merke].options == merke.options:
                startpunkt.options[mainPara1] = schonDrin[merke]
            else:
                startpunkt.options[mainPara1] = schonDrin[merke]
                # schonDrin2[merke] = merke, op2
        else:
            startpunkt.options[mainPara1] = merke
            schonDrin[merke] = merke
    return startpunkt


# startpunkt = setMainParas(startpunkt, mainParas)


def nebenToMainPara(startpunkt: dict, zeilen, kombi, spalten, ausgabe, exPara) -> dict:
    if exPara == "-zeilen":
        for nebenPara in zeilen:
            startpunkt.options[nebenPara] = NestedCompleter(
                {}, notParameterValues=notParameterValues
            )
    elif exPara == "-spalten":
        for nebenPara in spalten:
            startpunkt.options[nebenPara] = NestedCompleter(
                {}, notParameterValues=notParameterValues
            )
    elif exPara == "-kombination":
        for nebenPara in kombi:
            startpunkt.options[nebenPara] = NestedCompleter(
                {}, notParameterValues=notParameterValues
            )
    elif exPara == "-ausgabe":
        for nebenPara in ausgabe:
            startpunkt.options[nebenPara] = NestedCompleter(
                {}, notParameterValues=notParameterValues
            )

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
        if startpunkt.options[key] is None:
            startpunkt.options[key] = NestedCompleter({}, notParameterValues)
        startpunkt = startpunkt.options[key]
        # pp(startpunkt.options.keys())
        startpunkt = nebenUndMainParas(
            startpunkt, mainParas, zeilen, kombi, spalten, ausgabe, key
        )
        # pp((startpunkt).values())
        for key in deepcopy(tuple(startpunkt.options.keys())):
            nebenMainRekursiv(
                startpunkt,
                key,
                mainParas,
                zeilen,
                kombi,
                spalten,
                ausgabe,
                anzahl - 1,
            ),
    return startpunkt


def nochMalTraverse(startpunkt, anzahl):
    if anzahl > 0:
        for key in startpunkt.options.keys():
            startpunkt2 = startpunkt.options[key]
            nochMalTraverse(startpunkt2, anzahl - 1)
    return startpunkt


anzahl = 3
startpunkt1 = NestedCompleter({"reta": None}, notParameterValues)
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

pp(len(schonDrin))
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
