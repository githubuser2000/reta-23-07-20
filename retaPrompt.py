#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import reta
from nestedAlx import NestedCompleter
from prompt_toolkit import print_formatted_text, prompt
# from prompt_toolkit.completion import Completer, Completion, WordCompleter
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.styles import Style
from word_completerAlx import WordCompleter

retaProgram = reta.Program([sys.argv[0]])
# print(str(retaProgram.mainParaCmds))
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
print(str(ausgabeParas))
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
text = prompt(
    # print_formatted_text("Enter HTML: ", sep="", end=""), completer=html_completer
    "Enter HTML: ",
    completer=html_completer,
    wrap_lines=False,
    complete_while_typing=True,
    vi_mode=True,
)
print("You said: %s" % text, end=" ")
