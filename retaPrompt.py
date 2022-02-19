#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import os
import platform
import pprint
import re
import subprocess
import sys
from copy import copy, deepcopy
from itertools import zip_longest
from typing import Optional

from center import cliout
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


def newSession(history=False):
    if history:
        return PromptSession(history=FileHistory(os.path.expanduser("~") + os.sep + ".ReTaPromptHistory"))
    else:
        return PromptSession()


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
        + " starten mit Parameter -vi für ViMode (Ansonsten gelten Emacs-Tastenkürzel.), beenden mit q, exit, quit"
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


warBefehl: bool
befehleBeenden = ("ende", "exit", "quit", "q", ":q")
loggingSwitch = False
while text not in befehleBeenden:
    warBefehl = False
    session = newSession(loggingSwitch)
    try:
        text = session.prompt(
            # print_formatted_text("Enter HTML: ", sep="", end=""), completer=html_completer
            # ">",
            [("class:bla", ">")],
            # completer=NestedCompleter.from_nested_dict(
            #    startpunkt, notParameterValues=notParameterValues
            # ),
            completer=startpunkt1,
            wrap_lines=True,
            complete_while_typing=True,
            vi_mode=True if "-vi" in sys.argv else False,
            style=Style.from_dict({"bla": "#0000ff bg:#ffff00"}) if loggingSwitch else Style.from_dict({"bla": "#0000ff bg:#ff0000"}),
        )
    except KeyboardInterrupt:
        sys.exit()
    # stext: Optional[list[str]] = str(text).split()
    # stext2: list[str] = str(text).split()
    if text is not None:
        stext: list = text.split()
    else:
        stext: list = []

    if len(stext) > 0:
        textDazu: list
        stext2: list = []
        s_2: list

        for s_ in tuple(deepcopy(stext)):
            textDazu = []
            n: Optional[int] = None
            for ii, s_3 in enumerate(s_):
                if s_3.isdecimal():
                    n = ii
                    break
            try:
                if s_[int(n) - 1] == "-":
                    n -= 1
            except:
                pass

            if n is not None:
                s_2 = s_[n:].split(",")
                s_4 = [s_5.split("-") for s_5 in s_2]
                if len(s_) > n and [
                    [strInt.isdecimal() or len(strInt) == 0 for strInt in strA]
                    for strA in s_4
                ] == [[True for strInt in strA] for strA in s_4]:
                    buchst = set(s_[:n]) & {"a", "t", "v", "u", "p", "r", "U"}
                    if n == len(buchst):
                        buchst2: list = [a if a != "U" else "mu" for a in buchst]
                        textDazu += buchst2 + [str(s_[n:])]

            if len(textDazu) > 0:
                stext2 += textDazu
            else:
                stext2 += [str(s_)]
        stext = stext2

    if stext is not None:
        nstextnum: list = []
        for astext in stext:
            if astext.isdecimal():
                nstextnum += [int(astext)]
        if len(nstextnum) > 0:
            maxNum = max(nstextnum)
        else:
            maxNum = 1024

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

    if "--art=bbcode" in stext and "reta" == stext[0]:
        if "--nocolor" in stext:
            print("[code]" + text + "[/code]")
        else:
            cliout("[code]" + text + "[/code]", True, "bbcode")

    if ("abc" in stext or "abcd" in stext) and len(stext) == 2:
        warBefehl = True
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

    if len({"befehle"} & set(stext)) > 0:
        warBefehl = True
        print("Befehle: " + str(befehle)[1:-1])

    if len({"help", "hilfe"} & set(stext)) > 0 or (
        "h" in stext and "abc" not in stext and "abcd" not in stext
    ):
        warBefehl = True

        print(
            "Alle Befehle außer reta, shell, math, abc und abcd können beliebig kombiniert werden."
        )
        print(
            "Bei den meisten Kombinierbaren muss exakt eine Zahleninformation vorliegen, die innerhalb Leerzeichen steht.  Jedoch funktioniert der Befehl shell und math anders. 'shell' ist dazu da, Shellbefehle auszuführen und 'math' um Mathe-Formeln auszurechnen in Python-Syntax. \nWas ist eine Zahleninformation?"
        )
        print(
            "Eine Zahleninformation ist entweder eine natürliche Zahl z.B. 4, oder ein Zahlenbereich z.B. 3-6 oder eines oder beides dieser Zahleninformationen mehrmals mit Kommas getrennt z.B. 3,6-9,11. Hinter jedem Komma oder vor einer Zahl oder einem Zahlenbereich kann auch ein Minus stehen, was wieder Zahlen entfernt z.B. 1-10,-2,-5-9 entspricht 1,3,4,10."
        )
        print("Der Befehl 'befehle' gibt die Liste der möglichen Befehle aus.")

    if bedinung:
        warBefehl = True
        import reta

        reta.Program(stext, int(shellRowsAmountStr) - 15)
        # process = subprocess.Popen(sos.path.dirname(__file__) + os.sep + text)
        # process.wait()
    elif list(EineZahlenFolgeJa.values()).count(True) == 1:
        if "einzeln" not in stext and (
            ("vielfache" in stext)
            or ("v" in stext and "abc" not in stext and "abcd" not in stext)
        ):
            zeiln1 = "--vielfachevonzahlen=" + str(c).strip()

            zeiln2 = ""
        else:
            zeiln1 = "--vorhervonausschnitt=" + str(c).strip()
            zeiln2 = "--oberesmaximum=" + str(maxNum)

        if len({"absicht", "absichten", "motiv", "motive"} & set(stext)) > 0 or (
            (("a" in stext) != ("mo" in stext))
            and "abc" not in stext
            and "abcd" not in stext
        ):
            warBefehl = True
            import reta

            kette = [
                "reta",
                "-zeilen",
                zeiln1,
                zeiln2,
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

        if (len({"thomas"} & set(stext)) > 0) or (
            "t" in stext and "abc" not in stext and "abcd" not in stext
        ):
            warBefehl = True
            import reta

            kette = [
                "reta",
                "-zeilen",
                zeiln1,
                zeiln2,
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
            warBefehl = True
            externCommand("prim24", c)

        if (len({"prim", "primfaktorzerlegung"} & set(stext)) > 0) or (
            "p" in stext and "abc" not in stext and "abcd" not in stext
        ):
            warBefehl = True
            externCommand("prim", c)

        if len({"multis"} & set(stext)) > 0 or (
            "mu" in stext and "abc" not in stext and "abcd" not in stext
        ):
            warBefehl = True
            import reta

            # kette = [
            # "reta",
            # "-zeilen",
            # zeiln,
            # "-spalten",
            # "--multiplikationen=motivstern",
            # "--breite=" + str(int(shellRowsAmountStr) - 10),
            # ]
            # reta.Program(
            # kette,
            # int(shellRowsAmountStr),
            # )

            # externCommand("multis", c)
            listeStrWerte = c.split(",")
            try:
                mult(listeStrWerte)
            except NameError:
                from multis import mult

                mult(listeStrWerte)

            externCommand("prim", c)

        if len({"procontra"} & set(stext)) > 0:
            warBefehl = True
            import reta

            kette = [
                "reta",
                "-zeilen",
                zeiln1,
                zeiln2,
                "-spalten",
                "--procontra=pro,contra,gegenteil,harmonie,helfen,hilfeerhalten,gegenposition,pronutzen,nervig,nichtauskommen,nichtdagegen,keingegenteil,nichtdafuer,hilfenichtgebrauchen,nichthelfenkoennen,nichtabgeneigt,unmotivierbar,gegenspieler,sinn,vorteile,veraendern,kontrollieren,einheit",
                "--breite=" + str(int(shellRowsAmountStr) - 10),
            ]
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )
        if len({"modulo"} & set(stext)) > 0:
            warBefehl = True
            externCommand("modulo", c)

        if len({"alles"} & set(stext)) > 0:
            warBefehl = True
            import reta

            kette = [
                "reta",
                "-zeilen",
                zeiln1,
                zeiln2,
                "-spalten",
                "--alles",
                "--breite=" + str(int(shellRowsAmountStr) - 10),
                "-ausgabe",
            ]
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )

        if len({"primzahlkreuz"} & set(stext)) > 0:
            warBefehl = True
            import reta

            kette = [
                "reta",
                "-zeilen",
                zeiln1,
                "--oberesmaximum=1028",
                "-spalten",
                "--bedeutung=primzahlkreuz",
                "--breite=" + str(int(shellRowsAmountStr) - 10),
            ]
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )

        if len({"universum"} & set(stext)) > 0 or (
            "u" in stext and "abc" not in stext and "abcd" not in stext
        ):
            warBefehl = True
            import reta

            kette = [
                "reta",
                "-zeilen",
                zeiln1,
                zeiln2,
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
        if (len({"richtung"} & set(stext)) > 0) or (
            "r" in stext and "abc" not in stext and "abcd" not in stext
        ):
            warBefehl = True
            import reta

            kette = [
                "reta",
                "-zeilen",
                zeiln1,
                zeiln2,
                "-spalten",
                "--primzahlwirkung=Galaxieabsicht",
                "--breite=" + str(int(shellRowsAmountStr) - 10),
            ]
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )

    if len(stext) > 0 and "shell" == stext[0]:
        warBefehl = True
        try:
            process = subprocess.Popen([*stext[1:]])
            process.wait()
        except:
            pass

    if len(stext) > 0 and "math" == stext[0]:
        warBefehl = True
        try:
            process = subprocess.Popen(
                ["python3", "-c", "print(" + " ".join(stext[1:]) + ")"]
            )
            process.wait()
        except:
            pass
    if "loggen" == stext[0]:
        warBefehl = True
        loggingSwitch = True
    elif "nichtloggen" == stext[0]:
        warBefehl = True
        loggingSwitch = False

    if not warBefehl and len(stext) > 0 and stext[0] not in befehleBeenden:
        if stext[0] in befehle:
            print(
                "Dies ('"
                + stext[0].strip()
                + "') ist tatsächlich ein Befehl (oder es sind mehrere), aber es gibt nichts auszugeben.",
            )
        else:
            print("Das ist kein Befehl!")
