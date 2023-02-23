#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import os
import platform
import pprint
import re
import subprocess
import sys
from collections import defaultdict
from copy import copy, deepcopy
from enum import Enum
from itertools import zip_longest
from typing import Optional

from prompt_toolkit import PromptSession, print_formatted_text, prompt
# from prompt_toolkit.completion import Completer, Completion, WordCompleter
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style

from center import BereichToNumbers2, cliout, retaPromptHilfe
from lib4tables import multiples
from LibRetaPrompt import wahl15
# import reta
from nestedAlx import (ComplSitua, NestedCompleter, ausgabeParas, befehle,
                       befehle2, hauptForNeben, kombiMainParas, mainParas,
                       notParameterValues, reta, retaProgram, spalten,
                       spaltenDict, zeilenParas)
from word_completerAlx import WordCompleter


def isZeilenAngabe(g):
    return (
        True
        if bool(re.match(r"^[\+1234567890,-]+$", g))  # len(g) > 0 and
        and g[0].isdecimal()
        and g[-1] not in ["-", "+"]
        and "--" not in g
        and "++" not in g
        and "+-" not in g
        and "-+" not in g
        and ",+" not in g
        and "+," not in g
        and "-," not in g
        else False
    )


class PromptModus(Enum):
    normal = 0
    speichern = 1
    loeschenStart = 2
    speicherungAusgaben = 3
    loeschenSelect = 4
    speicherungAusgabenMitZusatz = 5
    AusgabeSelektiv = 6


class CharType(Enum):
    decimal = 0
    alpha = 1
    neithernor = 2
    begin = 3


def teiler(zahlenBereichsAngabe):
    ZahlenBereichMenge = BereichToNumbers2(zahlenBereichsAngabe, False, 0)
    ZahlenWbereichMenge = set()
    for each1 in ZahlenBereichMenge:
        for each2 in set(multiples(int(each1))):
            ZahlenWbereichMenge |= set(each2)
    ZahlenWbereichMenge -= {1}
    zahlenWBereichStringListe = [str(each2) for each2 in ZahlenWbereichMenge]
    return zahlenWBereichStringListe, ZahlenWbereichMenge


# def nummernStringzuNummern(text: str, isV: bool = False, until: int = 1028) -> str:
#    # print(BereichToNumbers2(text, isV, until))
#    # print(",".join([str(a) for a in BereichToNumbers2(text, isV, until)]))
#    return ",".join([str(a) for a in BereichToNumbers2(text, isV, until)])


#    def toNummernSet(text: list) -> set:
#        menge = set()
#        for t1 in text:
#            for t2 in t1:
#                menge |= {int(t2)}
#        return menge
#
#    listen = [kommatiert.split("-") for kommatiert in text.split(",")]
#    results = []
#    abzug = []
#    for insideKomma in listen:
#        if len(insideKomma) == 1 and insideKomma[0].isdecimal():
#            results += [[int(insideKomma[0])]]
#        elif len(insideKomma) == 2:
#            if insideKomma[0].isdecimal() and insideKomma[1].isdecimal():
#                raeinsch = range(int(insideKomma[0]), int(insideKomma[1]) + 1)
#                if len(raeinsch) > 0:
#                    results += [range(int(insideKomma[0]), int(insideKomma[1]) + 1)]
#            if insideKomma[0] == "" and insideKomma[1].isdecimal():
#                abzug += [[insideKomma[1]]]
#        elif len(insideKomma) == 3:
#            if (
#                insideKomma[0] == ""
#                and insideKomma[1].isdecimal()
#                and insideKomma[2].isdecimal()
#            ):
#                abzug += [range(int(insideKomma[1]), int(insideKomma[2]) + 1)]
#        else:
#            return text
#
#    return ",".join(map(str, toNummernSet(results) - toNummernSet(abzug)))


def newSession(history=False):
    if history:
        return PromptSession(
            history=FileHistory(os.path.expanduser("~") + os.sep + ".ReTaPromptHistory")
        )
    else:
        return PromptSession()


def returnOnlyParasAsList(textList: str):
    liste = []
    for t in textList:
        if len(t) > 0 and t[0] == "-":
            liste += [t]
    return liste


def externCommand(cmd: str, StrNummern: str):
    nummern: list[int] = list(BereichToNumbers2(StrNummern, False, 0))
    nummern.sort()
    nummernStr: list[str] = [str(nummer) for nummer in nummern]
    try:
        process = subprocess.Popen(
            [os.path.dirname(__file__) + os.sep + cmd, *nummernStr]
        )
        process.wait()
    except:
        pass


def speichern(ketten, platzhalter, text):
    global promptMode2, textDazu0
    bedingung1 = len(platzhalter) > 0
    bedingung2 = len(ketten) > 0
    if bedingung1 or bedingung2:
        if bedingung1:
            ifJoinReTaBefehle = True
            rpBefehlE = ""
            for rpBefehl in (text, platzhalter):
                rpBefehlSplitted = str(rpBefehl).split()
                if len(rpBefehlSplitted) > 0 and rpBefehlSplitted[0] == "reta":
                    rpBefehlE += " ".join(rpBefehlSplitted[1:]) + " "
                else:
                    ifJoinReTaBefehle = False
            if ifJoinReTaBefehle:
                platzhalter = "reta " + rpBefehlE
            else:
                # nochmal für nicht Kurzbefehle befehle, also ohne "reta" am Anfang
                textUndPlatzHalterNeu = []
                langKurzBefehle = []
                for rpBefehl in text.split() + platzhalter.split():
                    if rpBefehl in befehle and len(rpBefehl) > 1:
                        langKurzBefehle += [rpBefehl]
                    else:
                        textUndPlatzHalterNeu += [rpBefehl]
                ifJoinReTaBefehle = True
                rpBefehlE = ""
                for rpBefehl in textUndPlatzHalterNeu:
                    rpBefehlSplitted = str(rpBefehl).split()
                    if len(rpBefehlSplitted) > 0 and rpBefehlSplitted[0] != "reta":
                        rpBefehlE += " ".join(rpBefehlSplitted) + " "
                    else:
                        ifJoinReTaBefehle = False
                if ifJoinReTaBefehle:
                    rpBefehle2 = ""
                    charTuep = CharType.begin
                    stilbruch = False
                    zeichenKette = []
                    zahlenBereich = " "
                    alt_i = -1
                    for i, rpBefehl in enumerate(textUndPlatzHalterNeu):
                        for zeichen in rpBefehl:
                            charTuepDavor = charTuep
                            if zeichen.isalpha():
                                charTuep = CharType.alpha
                            elif zeichen.isdecimal():
                                charTuep = CharType.decimal
                            else:
                                charTuep = CharType.neithernor
                            if (
                                charTuep != charTuepDavor
                                and charTuepDavor != CharType.begin
                            ):
                                stilbruch = True
                            if not zeichen.isspace():
                                if zeichen in [",", "-"] or zeichen.isdecimal():
                                    if i == alt_i:
                                        zahlenBereich += " " + zeichen + " "
                                    else:
                                        zahlenBereich += zeichen
                                else:
                                    zeichenKette += [zeichen]
                        alt_i = i
                    if stilbruch:
                        rpBefehle2 = " ".join(zeichenKette) + zahlenBereich
                    platzhalter = rpBefehle2 + " " + (" ".join(langKurzBefehle))

        # vielleicht programmier ich hier noch weiter
        if bedingung2 and False:
            ifJoinReTaBefehle = True
            rpBefehlE = ""
            for rpBefehl in ketten:
                rpBefehlSplitted = rpBefehl
                if len(rpBefehl) > 0 and rpBefehl[0] == "reta":
                    rpBefehlE += " ".join(rpBefehl[1:]) + " "
                else:
                    ifJoinReTaBefehle = False
            if ifJoinReTaBefehle:
                platzhalter = "reta " + rpBefehlE

    else:
        platzhalter = "" if text is None else str(text)
    text = ""
    if platzhalter != "":
        promptMode2 = PromptModus.AusgabeSelektiv
    else:
        promptMode2 = PromptModus.normal
    textDazu0 = platzhalter.split()
    return ketten, platzhalter, text


def PromptScope():
    global promptMode2, textDazu0
    (
        befehleBeenden,
        ketten,
        loggingSwitch,
        nochAusageben,
        platzhalter,
        promptDavorDict,
        promptMode,
        shellRowsAmountStr,
        startpunkt1,
        text,
    ) = PromptAllesVorGroesserSchleife()
    while text not in befehleBeenden:
        warBefehl = False
        promptModeLast = promptMode

        if promptMode not in (
            PromptModus.speicherungAusgaben,
            PromptModus.speicherungAusgabenMitZusatz,
        ):
            befehlDavor, text = promptInput(
                loggingSwitch,
                platzhalter,
                promptDavorDict,
                promptMode,
                startpunkt1,
                text,
            )
            ketten, platzhalter, text = promptSpeicherungA(
                ketten, platzhalter, promptMode, text
            )

        else:
            text = promptSpeicherungB(nochAusageben, platzhalter, promptMode, text)

        if promptMode == PromptModus.loeschenSelect:
            platzhalter, promptMode, text = PromptLoescheVorSpeicherungBefehle(
                platzhalter, promptMode, text
            )
            continue

        promptMode = PromptModus.normal

        if text is not None:
            stext: list = text.split()
        else:
            stext: list = []

        # stext: Optional[list[str]] = str(text).split()
        # stext2: list[str] = str(text).split()
        if text == "S" or text == "BefehlSpeichernDanach":
            promptMode = PromptModus.speichern
            continue
        if text == "s" or text == "BefehlSpeichernDavor":
            ketten, platzhalter, text = speichern(ketten, platzhalter, befehlDavor)
            promptMode = PromptModus.normal
            continue

        elif text == "o" or text == "BefehlSpeicherungAusgeben":
            promptMode = PromptModus.speicherungAusgaben
            continue
        elif ("o" in stext or "BefehlSpeicherungAusgeben" in stext) and len(stext) > 1:
            nochAusageben = " ".join(
                tuple(set(stext) - {"o"} - {"BefehlSpeicherungAusgeben"})
            )
            promptMode = PromptModus.speicherungAusgabenMitZusatz
            continue
        elif text in ("l", "BefehlSpeicherungLöschen"):
            print(str([{i + 1, a} for i, a in enumerate(platzhalter.split())]))
            print("promptmode vorher: {} , {}".format(promptMode, promptMode2))
            promptMode = PromptModus.loeschenSelect
            continue

        (
            EineZahlenFolgeJa,
            bedingung,
            brueche,
            c,
            ketten,
            maxNum,
            stext,
        ) = promptVorbereitungGrosseAusgabe(
            ketten,
            platzhalter,
            promptMode,
            promptMode2,
            promptModeLast,
            text,
            textDazu0,
        )
        loggingSwitch = PromptGrosseAusgabe(
            EineZahlenFolgeJa,
            bedingung,
            befehleBeenden,
            brueche,
            c,
            ketten,
            loggingSwitch,
            maxNum,
            shellRowsAmountStr,
            stext,
            text,
            warBefehl,
        )


def PromptGrosseAusgabe(
    EineZahlenFolgeJa,
    bedingung,
    befehleBeenden,
    brueche,
    c,
    ketten,
    loggingSwitch,
    maxNum,
    shellRowsAmountStr,
    stext,
    text,
    warBefehl,
):
    if not bedingung:
        for g, a in enumerate(stext):
            EineZahlenFolgeJa[g] = isZeilenAngabe(g)

            # innerKomma3 = []
            # innerKomma4 = a.split(",")
            # for innerKomma2 in innerKomma4:
            #    if innerKomma2.isdecimal():
            #        innerKomma3 += [innerKomma2]
            # innerKomma6 = innerKomma3

            # if "w" in stext or "teiler" in stext:
            #    innerKomma3, innerKomma5 = teiler(innerKomma3)

            # print(innerKomma3)
            # for innerKomma in innerKomma3:
            #    innerKommaList = innerKomma.split("-")
            #    for k, innerMinus in enumerate(innerKommaList):
            #        if k == 0 and len(innerMinus) == 0:
            #            pass
            #        elif innerMinus.isdecimal():
            #            c = ",".join(innerKomma3)
            #            c2 = ",".join(innerKomma6)
            #            try:
            #                EineZahlenFolgeJa[g]
            #            except KeyError:
            #                EineZahlenFolgeJa[g] = True
            #
            #        else:
            #            EineZahlenFolgeJa[g] = False
            c2 = BereichToNumbers2(g, False, 0)
            c = teiler(g)

            for innerKomma in innerKomma4:
                bruch = [bruch for bruch in innerKomma.split("/")]
                if [bruch1.isdecimal() for bruch1 in bruch] == [True, True]:
                    brueche += [bruch]
            if "b" in stext:
                brueche += [[bruch[1], bruch[0]] for bruch in brueche]
    if "mulpri" in stext or "p" in stext:
        stext += ["multis", "prim"]
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
        retaPromptHilfe()
    bedingungZahl, bedingungBrueche = (
        list(EineZahlenFolgeJa.values()).count(True) == 1,
        len(brueche) > 0,
    )
    if bedingung:
        warBefehl = True
        import reta

        reta.Program(stext, int(shellRowsAmountStr) - 2)
        # process = subprocess.Popen(sos.path.dirname(__file__) + os.sep + text)
        # process.wait()

    if bedingungZahl:
        if "einzeln" not in stext and (
            ("vielfache" in stext)
            or ("v" in stext and "abc" not in stext and "abcd" not in stext)
        ):
            zeiln1 = "--vielfachevonzahlen=" + str(c).strip()
            # zeiln1 = "--vorhervonausschnitt=" + str(c).strip()

            zeiln2 = ""
        else:
            zeiln1 = "--vorhervonausschnitt=" + str(c).strip()
            zeiln2 = "--oberesmaximum=" + str(maxNum + 1)

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
                "--breite=" + str(int(shellRowsAmountStr) - 2),
                "-ausgabe",
                "--spaltenreihenfolgeundnurdiese=2",
                *["--keineleereninhalte" if "e" in stext else ""],
            ] + returnOnlyParasAsList(stext)
            kette += [ketten]
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )

    if bedingungZahl or bedingungBrueche:
        if len({"absicht", "absichten", "motiv", "motive"} & set(stext)) > 0 or (
            (("a" in stext) != ("mo" in stext))
            and "abc" not in stext
            and "abcd" not in stext
        ):
            warBefehl = True

            import reta

            if len(c) > 0:
                kette = [
                    "reta",
                    "-zeilen",
                    zeiln1,
                    zeiln2,
                    "-spalten",
                    "--menschliches=motivation",
                    "--breite=" + str(int(shellRowsAmountStr) - 2),
                    "-ausgabe",
                    "--spaltenreihenfolgeundnurdiese=1",
                    *["--keineleereninhalte" if "e" in stext else ""],
                ] + returnOnlyParasAsList(stext)
                kette += [ketten]
                reta.Program(
                    kette,
                    int(shellRowsAmountStr),
                )
            for bruch in brueche:
                import reta

                kette = [
                    "reta",
                    "-zeilen",
                    "--vorhervonausschnitt=" + bruch[0],
                    "-spalten",
                    "--gebrochengalaxie=" + bruch[1],
                    "--breite=" + str(int(shellRowsAmountStr) - 2),
                    "-kombination",
                    "-ausgabe",
                    "--spaltenreihenfolgeundnurdiese=1",
                    *["--keineleereninhalte" if "e" in stext else ""],
                ] + returnOnlyParasAsList(stext)
                kette += [ketten]
                reta.Program(
                    kette,
                    int(shellRowsAmountStr),
                )

        if len({"universum"} & set(stext)) > 0 or (
            "u" in stext and "abc" not in stext and "abcd" not in stext
        ):
            warBefehl = True
            if len(c) > 0:
                import reta

                kette = [
                    "reta",
                    "-zeilen",
                    zeiln1,
                    zeiln2,
                    "-spalten",
                    "--universum=transzendentalien,komplexitaet,ontologie",
                    "--breite=" + str(int(shellRowsAmountStr) - 2),
                    "-ausgabe",
                    "--spaltenreihenfolgeundnurdiese=1,3,4",
                    *["--keineleereninhalte" if "e" in stext else ""],
                ] + returnOnlyParasAsList(stext)
                kette += [ketten]
                reta.Program(
                    kette,
                    int(shellRowsAmountStr),
                )

            for bruch in brueche:
                import reta

                kette = [
                    "reta",
                    "-zeilen",
                    "--vorhervonausschnitt=" + bruch[0],
                    "-spalten",
                    "--gebrochenuniversum=" + bruch[1],
                    "--breite=" + str(int(shellRowsAmountStr) - 2),
                    "-kombination",
                    "-ausgabe",
                    "--spaltenreihenfolgeundnurdiese=1",
                    *["--keineleereninhalte" if "e" in stext else ""],
                ] + returnOnlyParasAsList(stext)
                kette += [ketten]
                reta.Program(
                    kette,
                    int(shellRowsAmountStr),
                )
    if bedingungZahl:

        if len({"prim24", "primfaktorzerlegungModulo24"} & set(stext)) > 0:
            warBefehl = True
            externCommand("prim24", c2)

        if len({"prim", "primfaktorzerlegung"} & set(stext)) > 0:
            warBefehl = True
            externCommand("prim", c2)

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
            # "--breite=" + str(int(shellRowsAmountStr) - 2),
            # ]
            # reta.Program(
            # kette,
            # int(shellRowsAmountStr),
            # )
            # externCommand("multis", c)
            listeStrWerte = c2.split(",")
            try:
                mult(listeStrWerte)
            except NameError:
                from multis import mult

                mult(listeStrWerte)

            # externCommand("prim", c)

        if len({"mond"} & set(stext)) > 0:
            warBefehl = True
            import reta

            kette = [
                "reta",
                "-zeilen",
                zeiln1,
                zeiln2,
                "-spalten",
                "--bedeutung=gestirn",
                "-ausgabe",
                "--spaltenreihenfolgeundnurdiese=3,4,5,6",
                "--breite=" + str(int(shellRowsAmountStr) - 2),
                *["--keineleereninhalte" if "e" in stext else ""],
            ] + returnOnlyParasAsList(stext)
            kette += [ketten]
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )

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
                "--breite=" + str(int(shellRowsAmountStr) - 2),
                "-ausgabe",
                *["--keineleereninhalte" if "e" in stext else ""],
            ] + returnOnlyParasAsList(stext)
            kette += [ketten]
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
                "--breite=" + str(int(shellRowsAmountStr) - 2),
                "-ausgabe",
                *["--keineleereninhalte" if "e" in stext else ""],
            ] + returnOnlyParasAsList(stext)
            kette += [ketten]
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
                "--breite=" + str(int(shellRowsAmountStr) - 2),
                "-ausgabe",
                *["--keineleereninhalte" if "e" in stext else ""],
            ] + returnOnlyParasAsList(stext)
            kette += [ketten]
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
                "--breite=" + str(int(shellRowsAmountStr) - 2),
                "-ausgabe",
                *["--keineleereninhalte" if "e" in stext else ""],
            ] + returnOnlyParasAsList(stext)
            kette += [ketten]
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )

        if (
            len(stext) > 0
            and any([token[:3] == "15_" for token in stext])
            and "abc" not in stext
            and "abcd" not in stext
        ):
            warBefehl = True
            import reta

            try:
                befehle15 = []
                for token in stext:
                    if token[:3] == "15_":
                        befehle15 += [wahl15[token[2:]]]
                grundstruk = ",".join(befehle15)
                kette = [
                    "reta",
                    "-zeilen",
                    zeiln1,
                    zeiln2,
                    "-spalten",
                    "--grundstrukturen=" + grundstruk,
                    "--breite=" + str(int(shellRowsAmountStr) - 2),
                    "-ausgabe",
                    *["--keineleereninhalte" if "e" in stext else ""],
                ] + returnOnlyParasAsList(stext)
                kette += [ketten]
                reta.Program(
                    kette,
                    int(shellRowsAmountStr),
                )
            except:
                pass
    loggingSwitch, warBefehl = PromptVonGrosserAusgabeSonderBefehlAusgaben(
        loggingSwitch, stext, text, warBefehl
    )
    if not warBefehl and len(stext) > 0 and stext[0] not in befehleBeenden:
        if stext[0] in befehle:
            print(
                "Dies ('"
                + stext[0].strip()
                + "') ist tatsächlich ein Befehl (oder es sind mehrere), aber es gibt nichts auszugeben.",
            )
        else:
            print("Das ist kein Befehl! -> " + str(stext))
    return loggingSwitch


def PromptVonGrosserAusgabeSonderBefehlAusgaben(loggingSwitch, stext, text, warBefehl):
    if len(stext) > 0 and stext[0] in ("shell"):
        warBefehl = True
        try:
            process = subprocess.Popen([*stext[1:]])
            process.wait()
        except:
            pass
    if len(stext) > 0 and "python" == stext[0]:
        warBefehl = True
        try:
            process = subprocess.Popen(["python3", "-c", " ".join(stext[1:])])
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
    if "loggen" == text:
        warBefehl = True
        loggingSwitch = True
    elif "nichtloggen" == text:
        warBefehl = True
        loggingSwitch = False
    return loggingSwitch, warBefehl


def promptVorbereitungGrosseAusgabe(
    ketten, platzhalter, promptMode, promptMode2, promptModeLast, text, textDazu0
):
    if text is not None:
        stext: list = text.split()
    else:
        stext: list = []
    ketten = []
    AusgabeSelektiv = 5
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
                    buchst = set(s_[:n]) & {
                        "a",
                        "t",
                        "v",
                        "u",
                        "p",
                        "r",
                        "w",
                        "s",
                        "o",
                        "S",
                        "e",
                    }
                    if n == len(buchst):
                        buchst2: list = [a if a != "p" else "mulpri" for a in buchst]
                        textDazu += buchst2 + [str(s_[n:])]
                    if (
                        len(stext) == 1
                        and len(buchst) == 0
                        and promptMode2 != PromptModus.AusgabeSelektiv
                    ):
                        textDazu += ["mulpri", "a", "t", "w"]

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
    stextb = []
    zahlenBereichMatch = [bool(isZeilenAngabe(swort)) for swort in stext]
    # zahlenBereichNeu = {i: a for i, a in zip(zahlenBereichMatch, stext)}
    # for s in stext:
    #    if (
    #        len(s) > 0
    #        and s[0].isdecimal()
    #        and ("," in s or "-" in s or "+" in s)
    #        and s == zahlenBereichNeu[True]
    #    ):
    #        stextb += [nummernStringzuNummern(s, "v" in stext)]
    #    else:
    #        stextb += [s]
    # stext = stextb
    if (
        promptMode2 == PromptModus.AusgabeSelektiv
        and promptModeLast == PromptModus.normal
    ):
        stext += textDazu0
    if (
        promptMode == PromptModus.normal
        and len(platzhalter) > 1
        and platzhalter[:4] == "reta"
        # and not any([("--vorhervonausschnitt" in a or "--vielfachevonzahlen" in a) for a in stext])
        and any(zahlenBereichMatch)
        and zahlenBereichMatch.count(True) == 1
    ):
        zeilenn = False
        woerterToDel = []
        for i, wort in enumerate(stext):
            if len(wort) > 1 and wort[0] == "-" and wort[1] != "-":
                zeilenn = False
            if zeilenn is True or wort == zahlenBereichNeu[True]:
                woerterToDel += [i]
            if wort == "-zeilen":
                zeilenn = True
                woerterToDel += [i]
        stextDict = {i: swort for i, swort in enumerate(stext)}
        for todel in woerterToDel:
            del stextDict[todel]
        stext = list(stextDict.values())

        if len({"w", "teiler"} & set(stext)) > 0:
            BereichMenge = BereichToNumbers2(zahlenBereichNeu[True], False, 0)
            BereichMengeNeu = teiler(BereichMenge)[1]
            zahlenBereichNeu[True] = ""
            for a in BereichMengeNeu:
                zahlenBereichNeu[True] += str(a) + ","
            zahlenBereichNeu[True] = zahlenBereichNeu[True][:-1]

            try:
                stext.remove("w")
            except:
                pass
            try:
                stext.remove("teiler")
            except:
                pass

        if len({"v", "vielfache"} & set(stext)) == 0:
            stext += ["-zeilen", "--vorhervonausschnitt=" + zahlenBereichNeu[True]]

        else:
            # stext += ["-zeilen", "--vorhervonausschnitt=" + zahlenBereichNeu[True]]
            stext += [
                "-zeilen",
                "--vielfachevonzahlen=" + zahlenBereichNeu[True],
            ]
            try:
                stext.remove("v")
            except:
                pass
            try:
                stext.remove("vielfache")
            except:
                pass
    bedingung: bool = len(stext) > 0 and stext[0] == "reta"
    brueche = []
    c = ""
    EineZahlenFolgeJa: dict = {}
    return EineZahlenFolgeJa, bedingung, brueche, c, ketten, maxNum, stext


def PromptAllesVorGroesserSchleife():
    global promptMode2, textDazu0
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
        retaPromptHilfe()
    if "-log" in sys.argv:
        loggingSwitch = True
    else:
        loggingSwitch = False
    if platform.system() != "Windows":
        try:
            ColumnsRowsAmount, shellRowsAmountStr = (
                os.popen("stty size", "r").read().split()
            )  # Wie viele Zeilen und Spalten hat die Shell ?
        except Exception:
            ColumnsRowsAmount, shellRowsAmountStr = "80", "80"
    else:
        SiZe = os.get_terminal_size()
        ColumnsRowsAmount, shellRowsAmountStr = SiZe.columns, SiZe.lines
    promptMode = PromptModus.normal
    promptMode2 = PromptModus.normal
    warBefehl: bool
    befehleBeenden = ("ende", "exit", "quit", "q", ":q")
    platzhalter = ""
    ketten = []
    text = ""
    promptDavorDict = defaultdict(lambda: ">")
    promptDavorDict[PromptModus.speichern] = "was speichern>"
    promptDavorDict[PromptModus.loeschenSelect] = "was löschen>"
    nochAusageben = ""
    textDazu0 = []
    return (
        befehleBeenden,
        ketten,
        loggingSwitch,
        nochAusageben,
        platzhalter,
        promptDavorDict,
        promptMode,
        shellRowsAmountStr,
        startpunkt1,
        text,
    )


def PromptLoescheVorSpeicherungBefehle(platzhalter, promptMode, text):
    global promptMode2, textDazu0
    text = str(text)
    if bool(isZeilenAngabe(text)):
        zuloeschen = text
        loeschbares = {i + 1: a for i, a in enumerate(platzhalter.split())}
        for todel in zuloeschen:
            try:
                del loeschbares[todel]
            except:
                pass
        platzhalter = " ".join(loeschbares.values())
    else:
        loeschbares = {a: i + 1 for i, a in enumerate(platzhalter.split())}
        for wort in text.split():
            try:
                del loeschbares[wort]
            except:
                pass
        platzhalter = " ".join(loeschbares.keys())
    promptMode = PromptModus.normal
    if len(platzhalter.strip()) == 0:
        promptMode2 = PromptModus.normal
        textDazu0 = []
    return platzhalter, promptMode, text


def promptSpeicherungB(nochAusageben, platzhalter, promptMode, text):
    # stext = text.split()
    # if promptMode in (
    #    PromptModus.speicherungAusgaben,
    #    PromptModus.speicherungAusgabenMitZusatz,
    # ):
    if promptMode == PromptModus.speicherungAusgaben:
        text = platzhalter
    elif promptMode == PromptModus.speicherungAusgabenMitZusatz:
        text = platzhalter + " " + nochAusageben
    return text


def promptSpeicherungA(ketten, platzhalter, promptMode, text):
    if promptMode == PromptModus.speichern:
        ketten, platzhalter, text = speichern(ketten, platzhalter, text)
    return ketten, platzhalter, text


def promptInput(
    loggingSwitch, platzhalter, promptDavorDict, promptMode, startpunkt1, text
):
    session = newSession(loggingSwitch)
    try:
        befehlDavor = text
        text = session.prompt(
            # print_formatted_text("Enter HTML: ", sep="", end=""), completer=html_completer
            # ">",
            [("class:bla", promptDavorDict[promptMode])],
            # completer=NestedCompleter.from_nested_dict(
            #    startpunkt, notParameterValues=notParameterValues
            # ),
            completer=startpunkt1
            if not promptMode == PromptModus.loeschenSelect
            else None,
            wrap_lines=True,
            complete_while_typing=True,
            vi_mode=True if "-vi" in sys.argv else False,
            style=Style.from_dict({"bla": "#0000ff bg:#ffff00"})
            if loggingSwitch
            else Style.from_dict({"bla": "#0000ff bg:#ff0000"}),
            # placeholder="reta",
            placeholder=platzhalter,
        )
        text: str = str(text)
        text.replace(" 15_ ", " 15_15 ")
        if text[:4] == "15_ ":
            text = "15_15 " + text[4:]
        if text[-4:] == " 15_":
            text = text[:-4] + " 15_15"
    except KeyboardInterrupt:
        sys.exit()
    return befehlDavor, text


PromptScope()
