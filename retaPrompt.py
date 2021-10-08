#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import os
import platform
import pprint
import re
import subprocess
import sys
from copy import deepcopy
from itertools import zip_longest
from typing import Optional

from center import BereichToNumbers
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

try:
    if platform.system() != "Windows":
        ColumnsRowsAmount, shellRowsAmountStr = (
            os.popen("stty size", "r").read().split()
        )  # Wie viele Zeilen und Spalten hat die Shell ?
    else:
        ColumnsRowsAmount, shellRowsAmountStr = "80", "80"
except Exception:
    ColumnsRowsAmount, shellRowsAmountStr = "80", "80"

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


def externCommand(cmd: str, StrNummern: str):
    nummern: list[int] = list(BereichToNumbers(StrNummern))
    nummern.sort()
    nummernStr: list[str] = [str(nummer) for nummer in nummern]
    try:
        process = subprocess.Popen(
            [os.path.dirname(__file__) + os.sep + cmd, *nummernStr]
        )
        process.wait()
    except:
        pass


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
    stext: Optional[list] = text.split()
    bedinung: bool = len(stext) > 0 and stext[0] == "reta"
    if not bedinung:
        EineZahlenFolgeJa: dict = {}
        for g, a in enumerate(stext):
            for innerKomma in a.split(","):
                innerKommaList = innerKomma.split("-")
                for k, innerMinus in enumerate(innerKommaList):
                    if k == 0 and len(innerMinus) == 0:
                        pass
                    elif innerMinus.isdecimal():
                        c = a
                        try:
                            EineZahlenFolgeJa[g]
                        except KeyError:
                            EineZahlenFolgeJa[g] = True

                    else:
                        EineZahlenFolgeJa[g] = False

            # d = re.split(",|-", a)
            # if a.isnumeric() or [b.isnumeric() for b in d] == [True] * len(d):
            # b += 1
            # c = a

    if "abc" in stext or "abcd" in stext and len(stext) == 2:
        buchstabe: str
        if stext[0] == "abc" or stext[0] == "abcd":
            buchstaben = stext[1]
        else:
            buchstaben = stext[0]
        print(
            str(
                " ".join(
                    [
                        "".join(str(ord(buchstabe.lower()) - 96))
                        for buchstabe in buchstaben
                    ]
                )
            )
        )

    if "help" in stext or "hilfe" in stext:
        print(
            "Alle Befehle außer reta, abc und abcd können beliebig kombiniert werden."
        )
        print(
            "Bei den kombinierbaren muss exakt eine Zahleninformation vorliegen, die innerhalb Leerzeichen steht. Was ist eine Zahleninformation?"
        )
        print(
            "Eine Zahleninformation ist entweder eine natürliche Zahl z.B. 4, oder ein Zahlenbereich z.B. 3-6 oder eines oder beides dieser Zahleninformationen mehrmals mit Kommas getrennt z.B. 3,6-9,11. Hinter jedem Komma oder vor einer Zahl oder einem Zahlenbereich kann auch ein Minus stehen, was wieder Zahlen entfernt z.B. 1-10,-2,-5-9 entspricht 1,3,4,10."
        )

    if bedinung:
        import reta

        reta.Program(stext, int(shellRowsAmountStr) - 15)
        # process = subprocess.Popen(sos.path.dirname(__file__) + os.sep + text)
        # process.wait()
    elif list(EineZahlenFolgeJa.values()).count(True) == 1:
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
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )
        if len({"prim24", "primfaktorzerlegungModulo24"} & set(stext)) > 0:
            externCommand("prim24", c)

        if len({"prim", "primfaktorzerlegung"} & set(stext)) > 0:
            externCommand("prim", c)

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
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )

            externCommand("multis", c)
            externCommand("prim", c)

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
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )
        if len({"modulo"} & set(stext)) > 0:
            externCommand("modulo", c)

        if len({"alles"} & set(stext)) > 0:
            import reta

            kette = [
                "reta",
                "-zeilen",
                zeiln,
                "-spalten",
                "--alles",
                "--breite=" + str(int(shellRowsAmountStr) - 10),
                "-ausgabe",
            ]
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )

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
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )
