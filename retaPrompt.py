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
        # yield Completion("abcd", start_position=0)
        a = (a for a in [0, 1])
        b = (b for b in [2, 3, 4])
        # UNSINN DAS MIT GENERATOR ZU MACHEN, DA ES DURCH DIE LIB AM ENDE ZU EINER LISTE WIRD UND DAS LAHMEN WIRD AUCH MIT NUMPY
        # DAS HEIßT SOGAR INSGESAMT FUNKTIONIERT DAS NICHT SO WIE ICH WILL
        wortliste = ""
        for davor in ["-", ""]:
            for zahl1 in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                for zahl2 in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ""]:
                    for zahl3 in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ""]:
                        for zahl4 in [
                            "0",
                            "1",
                            "2",
                            "3",
                            "4",
                            "5",
                            "6",
                            "7",
                            "8",
                            "9",
                            "",
                        ]:
                            wortliste += davor + zahl1 + zahl2 + zahl3 + zahl4

        completer = WordCompleter([a for a in ["abcdef", "hijkl"]])
        for c in completer.get_completions(document, complete_event):
            yield c


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
