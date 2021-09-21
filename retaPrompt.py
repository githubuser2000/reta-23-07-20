#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pprint
import re
import subprocess
import sys
from copy import deepcopy
from itertools import zip_longest
from typing import Optional

# import reta
from nestedAlx import (ComplSitua, NestedCompleter, ausgabeParas, befehle,
                       befehle2, hauptForNeben, kombiMainParas, mainParas,
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


startpunkt1 = NestedCompleter(
    {a: None for a in befehle},
    notParameterValues,
    {},
    ComplSitua.retaAnfang,
    "",
    {
        **{"reta": ComplSitua.retaAnfang},
        **{a: ComplSitua.befehleNichtReta for a in befehle2},
    },
)

text: Optional[str] = None
if "-vi" not in sys.argv:
    print(
        sys.argv[0].split(os.sep)[-1]
        + " starten mit Parameter -vi für ViMode, beenden mit q, exit, quit"
    )
    print("Tippe reta ein!")

while text not in ("ende", "exit", "quit", "q", ""):
    try:
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
    except KeyboardInterrupt:
        sys.exit()
    # print("Du meintest: %s" % text, end=" ")
    stext = text.split()
    bedinung = len(stext) > 0 and stext[0] == "reta"
    if not bedinung:
        b = 0
        for a in stext:
            d = re.split(",|-", a)
            if a.isnumeric() or [b.isnumeric() for b in d] == [True] * len(d):
                b += 1
                c = a

    if bedinung:
        import reta

        reta.Program(stext, int(shellRowsAmountStr) - 15)
        # process = subprocess.Popen(sos.path.dirname(__file__) + os.sep + text)
        # process.wait()
    elif b == 1:
        if "vielfache" in stext and "einzeln" not in stext:
            zeiln = "--vielfachevonzahlen=" + str(c).strip()
        else:
            zeiln = "--vorhervonausschnitt=" + str(c).strip()

        if len({"absicht", "absichten", "motiv", "motive"} & set(stext)) > 0:
            import reta

            kette = [
                "reta",
                "-zeilen",
                zeiln,
                "-spalten",
                "--menschliches=motivation",
                "--breite=" + str(int(shellRowsAmountStr) - 10),
                "-ausgabe",
                "--spaltenreihenfolgeundnurdiese=1",
            ]
            # print(str(kette))
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )
        if len({"thomas"} & set(stext)) > 0:
            import reta

            kette = [
                "reta",
                "-zeilen",
                zeiln,
                "-spalten",
                "--galaxie=thomas",
                "--breite=" + str(int(shellRowsAmountStr) - 10),
                "-ausgabe",
                "--spaltenreihenfolgeundnurdiese=2",
            ]
            # print(str(kette))
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )
        if len({"prim24", "primfaktorzerlegungModulo24"} & set(stext)) > 0:
            try:
                process = subprocess.Popen(
                    [os.path.dirname(__file__) + os.sep + "prim24", c]
                )
                process.wait()
            except:
                pass
        if len({"prim", "primfaktorzerlegung"} & set(stext)) > 0:
            try:
                process = subprocess.Popen(
                    [os.path.dirname(__file__) + os.sep + "prim", c]
                )
                process.wait()
            except:
                pass
        if len({"multis"} & set(stext)) > 0:
            import reta

            kette = [
                "reta",
                "-zeilen",
                zeiln,
                "-spalten",
                "--multiplikationen=motivstern",
                "--breite=" + str(int(shellRowsAmountStr) - 10),
            ]
            # print(str(kette))
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )
            try:
                process = subprocess.Popen(
                    [os.path.dirname(__file__) + os.sep + "multis", c]
                )
                process.wait()
            except:
                pass
            try:
                process = subprocess.Popen(
                    [os.path.dirname(__file__) + os.sep + "prim", c]
                )
                process.wait()
            except:
                pass
        if len({"procontra"} & set(stext)) > 0:
            import reta

            kette = [
                "reta",
                "-zeilen",
                zeiln,
                "-spalten",
                "--procontra=pro,contra,gegenteil,harmonie,helfen,hilfeerhalten,gegenposition,pronutzen,nervig,nichtauskommen,nichtdagegen,keingegenteil,nichtdafuer,hilfenichtgebrauchen,nichthelfenkoennen,nichtabgeneigt,unmotivierbar,gegenspieler,sinn,vorteile,veraendern,kontrollieren,einheit",
                "--breite=" + str(int(shellRowsAmountStr) - 10),
            ]
            # print(str(kette))
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )
        if len({"modulo"} & set(stext)) > 0:
            try:
                process = subprocess.Popen(
                    [os.path.dirname(__file__) + os.sep + "modulo", c]
                )
                process.wait()
            except:
                pass
        if len({"universum"} & set(stext)) > 0:
            import reta

            kette = [
                "reta",
                "-zeilen",
                zeiln,
                "-spalten",
                "--universum=transzendentalien,komplexitaet,ontologie",
                "--breite=" + str(int(shellRowsAmountStr) - 10),
                "-ausgabe",
                "--spaltenreihenfolgeundnurdiese=1,3,4",
            ]
            # print(str(kette))
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )
        if len({"modulo"} & set(stext)) > 0:
            try:
                process = subprocess.Popen(
                    [os.path.dirname(__file__) + os.sep + "modulo", c]
                )
                process.wait()
            except:
                pass
