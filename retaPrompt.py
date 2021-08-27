#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import reta
from prompt_toolkit import print_formatted_text, prompt
from prompt_toolkit.completion import (Completer, Completion, NestedCompleter,
                                       WordCompleter)
from prompt_toolkit.styles import Style


class MyCustomCompleter(Completer):
    def get_completions(self, document, complete_event):
        yield Completion("abcd", start_position=0)


retaProgram = reta.Program([sys.argv[0]])
# print(str(retaProgram.mainParaCmds))
# print(str(retaProgram.paraDict.keys()))
# print(str(reta.Program.kombiParaNdataMatrix.values()))
# print(str(reta.Program.kombiParaNdataMatrix2.values()))
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
        "exit": MyCustomCompleter(),
    }
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
