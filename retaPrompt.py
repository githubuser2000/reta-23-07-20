#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import os
import platform
import pprint
import re
import subprocess
import sys
from collections import OrderedDict, defaultdict
from copy import copy, deepcopy
from enum import Enum
from itertools import zip_longest
from typing import Optional

from prompt_toolkit import PromptSession, print_formatted_text, prompt
# from prompt_toolkit.completion import Completer, Completion, WordCompleter
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style

from center import (cliout, isZeilenAngabe, isZeilenAngabe_betweenKommas,
                    retaPromptHilfe, teiler)
from LibRetaPrompt import (BereichToNumbers2, PromptModus,
                           gebrochenErlaubteZahlen, isReTaParameter,
                           notParameterValues, stextFromKleinKleinKleinBefehl,
                           verifyBruchNganzZahlBetweenCommas, verkuerze_dict,
                           wahl15)
# import reta
from nestedAlx import (ComplSitua, NestedCompleter, ausgabeParas, befehle,
                       befehle2, hauptForNeben, kombiMainParas, mainParas,
                       reta, retaProgram, spalten, spaltenDict, zeilenParas)
from word_completerAlx import WordCompleter

wahl15["_"] = wahl15["_15"]
befehleBeenden = {"ende", "exit", "quit", "q", ":q"}


def anotherOberesMaximum(c, maxNum):
    maximizing = list(BereichToNumbers2(c, False, 0))
    if len(maximizing) > 0:
        maximizing.sort()
        maxNum2 = maximizing[-1]
    else:
        maxNum2 = maxNum
    return "--oberesmaximum=" + str(max(maxNum, maxNum2) + 1)


class CharType(Enum):
    decimal = 0
    alpha = 1
    neithernor = 2
    begin = 3


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
        if isReTaParameter(t):
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


def grKl(A: set, B: set) -> tuple[set, set]:
    """
    Gibt 2 Mengen zurück: eine Menge aus allem, das größer ist als im ersten Parameter aus dem zweiten Parameter
    und in die zweite Menge kommt alles, das kleiner ist, als in der ersten Menge aus der zweiten Menge
    """
    C = set()
    D = set()
    if len(B) == 0:
        return A, A
    for a in A:
        if a > max(B):
            C.add(a)
        elif a < min(B):
            D.add(a)
    return C, D


def getDictLimtedByKeyList(d: dict, keys) -> dict:
    """
    Gibt ein dict zurück, das aus einem dict gebildet wird, aber davon nur das nimmt, was an mehreren keys genommen werden soll.
    """
    return OrderedDict({k: d[k] for k in keys if k in d})


def bruchSpalt(text) -> list:
    """
    Gibt eine Liste aus Tupeln zurück, die entweder einen bis mehrere oder zwei Werte enthalten.
    Eingabe sind Brüche gemischt mit Textwerten
    Das Ergebnis bei zwei Werten ist der Bruch
    Bei ein bis mehreren Werten, also auch 2 handelt es sich um die Textwerte, welche zwischen den Brüchen waren.
    Die Reihenfolge vom Ergebnis ist die Gleiche, wie bei dem Eingabe-Text
    """
    if type(text) is not str:
        return []
    bruchSpalten: list[str] = text.split("/")
    bruchSpaltenNeu = []
    bruchSpaltenNeu2 = []
    if len(bruchSpalten) < 2:
        """Ein Bruch hat immer mindestens 2 Zahlen"""
        return []
    keineZahl = OrderedDict()
    for k, bS in enumerate(bruchSpalten):
        keineZahlBefore = keineZahl
        zahl, keineZahl, bsNeu = OrderedDict(), OrderedDict(), []
        countChar = 0
        countNumber = 0
        wasNumber = False
        goNext = 0
        for char in bS:
            if char.isdecimal():
                """alles was Zahlen sind"""
                if not wasNumber:
                    goNext += 1
                try:
                    zahl[goNext] += char
                except KeyError:
                    zahl[goNext] = char
                wasNumber = True
                countNumber += 1
                countChar = 0
            else:
                """alles was keine Zahlen sind"""
                if wasNumber:
                    goNext += 1
                try:
                    keineZahl[goNext] += char
                except KeyError:
                    keineZahl[goNext] = char
                wasNumber = False
                countChar += 1
                countNumber = 0
        print("ä {},{}".format(zahl, keineZahl))
        flag: bool = False
        allVergleich: list[bool] = [
            zahl > c for c, zahl in zip(keineZahl.keys(), zahl.keys())
        ]
        """bool Liste wann es keine ist und wann eine zahl im string"""
        zahlSet: set = set(zahl.keys())
        keineZahlSet: set = set(keineZahl.keys())
        if len(zahlSet) == 0:
            return []
        anfang, ende = k == 0, k == len(bruchSpalten) - 1
        if anfang and all(allVergleich):
            flag = True
        elif ende and not any(allVergleich):
            flag = True
        elif (
            not anfang
            and not ende
            and keineZahlSet.issubset(range(min(zahlSet) + 1, max(zahlSet)))
        ):
            flag = True
        else:
            flag = False
        if flag is False:
            return []
        # bsAlt = bsNeu
        if len(keineZahlSet) > 0:
            zahlenGroesserSet, zahlenKleinerSet = grKl(zahlSet, keineZahlSet)
            """siehe erklärung der Fkt in Fkt"""
            zahlenKleinerDict: dict = getDictLimtedByKeyList(zahl, zahlenKleinerSet)
            zahlenGroesserDict: dict = getDictLimtedByKeyList(zahl, zahlenGroesserSet)
            """siehe erklärung der Fkt in Fkt"""
            if k == len(bruchSpalten) - 1 and len(zahlenGroesserDict) > 0:
                return []
            bsNeu = [zahlenKleinerDict, keineZahl, zahlenGroesserDict]
        elif k == 0 or k == len(bruchSpalten) - 1:
            bsNeu = [zahl]
        else:
            return []
        bruchSpaltenNeu += [bsNeu]
        if k == 1:
            vorZahl1 = (
                () if len(bruchSpaltenNeu[0]) == 1 else bruchSpaltenNeu[0][1].values()
            )
            vorZahl1 = tuple(vorZahl1)
            zahl1 = (
                bruchSpaltenNeu[0][0].values()
                if len(bruchSpaltenNeu[0]) == 1
                else bruchSpaltenNeu[0][2].values()
            )
            zahl2 = bruchSpaltenNeu[1][0].values()
            zahl1 = tuple(zahl1)
            zahl2 = tuple(zahl2)
            if k == len(bruchSpalten) - 1:
                nachZahl2 = (
                    ()
                    if len(bruchSpaltenNeu[-1]) == 1
                    else bruchSpaltenNeu[-1][1].values()
                )
                nachZahl2 = tuple(nachZahl2)
                bruchSpaltenNeu2 += [vorZahl1, zahl1 + zahl2, nachZahl2]
            else:
                bruchSpaltenNeu2 += [vorZahl1, zahl1 + zahl2]
        elif k == len(bruchSpalten) - 1 and k > 1:
            vorZahl1 = (
                () if len(bruchSpaltenNeu[-2]) == 1 else bruchSpaltenNeu[-2][1].values()
            )
            vorZahl1 = tuple(vorZahl1)
            zahl1 = (
                bruchSpaltenNeu[-2][0].values()
                if len(bruchSpaltenNeu[-2]) == 1
                else bruchSpaltenNeu[-2][2].values()
            )
            zahl2 = bruchSpaltenNeu[-1][0].values()
            zahl1 = tuple(zahl1)
            zahl2 = tuple(zahl2)
            nachZahl2 = (
                () if len(bruchSpaltenNeu[-1]) == 1 else bruchSpaltenNeu[-1][1].values()
            )
            nachZahl2 = tuple(nachZahl2)
            bruchSpaltenNeu2 += [vorZahl1, zahl1 + zahl2, nachZahl2]
        elif k > 1:
            vorZahl1 = (
                () if len(bruchSpaltenNeu[-2]) == 1 else bruchSpaltenNeu[-2][1].values()
            )
            vorZahl1 = tuple(vorZahl1)
            zahl1 = (
                bruchSpaltenNeu[-2][0].values()
                if len(bruchSpaltenNeu[-2]) == 1
                else bruchSpaltenNeu[-2][2].values()
            )
            zahl2 = bruchSpaltenNeu[-1][0].values()
            zahl1 = tuple(zahl1)
            zahl2 = tuple(zahl2)
            bruchSpaltenNeu2 += [vorZahl1, zahl1 + zahl2]
            # return bruchSpaltenNeu, bruchSpaltenNeu2
    return bruchSpaltenNeu2


def dictToList(dict_: dict) -> list:
    liste = []
    for key, value in dict_.items():
        liste += [value]
    return liste


def createRangesForBruchLists(bruchList: list) -> tuple:
    n1, n2 = [], []
    listenRange: range = range(0)
    listenRangeUrsprung: range = range(0)
    flag = 0
    # ergebnis: list[tuple[range | str]] = []
    ergebnis = []
    print(bruchList)
    if (
        len(bruchList) == 3
        and len(bruchList[0]) == 0
        and len(bruchList[1]) == 2
        and len(bruchList[2]) == 0
        and (bruchList[1][0] + bruchList[1][1]).isdecimal()
    ):
        return [int(bruchList[1][0])], bruchList[1][1]
    for i, b in enumerate(bruchList):
        if flag == -1:
            return []
        if flag > 3:
            """illegal"""
            return []
        elif flag == 3:
            """Es war ein Bruch"""
            ergebnis += [str(n2[-2]), "-", str(n2[-1])]

            print("ü {}".format(ergebnis))
            listenRange = range(int(n1[-2]), int(n1[-1]) + 1)
            listenRangeUrsprung = listenRange
            flag = -1
        if len(b) == 2 and (b[0] + b[1]).isdecimal():
            """Es ist ein Bruch"""
            if (
                len(bruchList) >= i
                and len(bruchList[i + 1]) == 1
                and bruchList[i + 1][0] == "-"
                and flag == 0
            ) or (
                i > 0
                and len(bruchList[i - 1]) == 1
                and bruchList[i - 1][0] == "-"
                and flag == 2
            ):
                n1 += [int(b[0])]
                n2 += [int(b[1])]
                flag += 1
            else:
                ergebnis += [b[1]]
                if (
                    len(listenRange) > 0
                    and i > 0
                    and len(bruchList[i - 1]) == 1
                    and bruchList[i - 1][0] == "+"
                ):
                    listenRange2 = []
                    for lr in listenRangeUrsprung:
                        listenRange2 += [lr + int(b[0]), lr - int(b[0])]
                    listenRange = listenRange2
                elif len(listenRange) == 0:
                    listenRange = [int(b[0])]
                    listenRangeUrsprung = listenRange
        elif len(b) == 1 and b[0] == "-" and flag > 0:
            flag += 1

        else:
            """Es ist kein Bruch"""
            flag = 0
            ergebnis += [*b]
    print("d {}".format(ergebnis))
    ergebnis2 = "".join(ergebnis)
    return listenRange, ergebnis2


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
    (
        bedingungX,
        bruecheX,
        cX,
        ketten2X,
        maxNum2X,
        stextX,
        zahlenAngaben_X,
        ifKurzKurz_X,
    ) = promptVorbereitungGrosseAusgabe(
        ketten,
        platzhalter,
        PromptModus.normal,
        PromptModus.normal,
        PromptModus.normal,
        platzhalter,
        [],
    )

    # textDazu0 = platzhalter.split()
    textDazu0 = stextX
    # print([ketten, platzhalter, text, textDazu0, promptMode2, "end"])
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
            bedingung,
            brueche,
            c,
            ketten,
            maxNum,
            stext,
            zahlenAngaben_,
            ifKurzKurz,
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
            zahlenAngaben_,
            ifKurzKurz,
        )


def PromptGrosseAusgabe(
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
    zahlenAngaben_,
    ifKurzKurz,
):
    (
        EsGabzahlenAngaben,
        c2,
        bruch_GanzZahlReziproke,
        fullBlockIsZahlenbereichAndBruch,
        rangesBruecheDict,
        rangesBruecheDictReverse,
    ) = (False, "", [], False, {}, {})
    if not bedingung:
        (
            bruch_GanzZahlReziproke,
            c,
            c2,
            fullBlockIsZahlenbereichAndBruch,
            rangesBruecheDict,
            EsGabzahlenAngaben,
            rangesBruecheDictReverse,
        ) = bruchBereichsManagementAndWbefehl(c, stext, zahlenAngaben_)
    if "mulpri" in stext or "p" in stext:
        stext += ["multis", "prim"]
    if "--art=bbcode" in stext and "reta" == stext[0]:
        if "--nocolor" in stext:
            print("[code]" + text + "[/code]")
        else:
            cliout("[code]" + text + "[/code]", True, "bbcode")
    if (
        ifKurzKurz
        and "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar" not in stext
    ):
        print(
            "'{}' ergibt sich aus '{}' und ergibt danach reta-Befehl:".format(
                " ".join(stext), text
            )
        )
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
        EsGabzahlenAngaben,
        (len(bruch_GanzZahlReziproke) > 0 or len(rangesBruecheDict) > 0)
        or len(rangesBruecheDictReverse) > 0,
    )
    if bedingung:
        warBefehl = True
        import reta

        reta.Program(stext, int(shellRowsAmountStr) - 2)

    if len(bruch_GanzZahlReziproke) > 0:
        zeiln3 = "--vorhervonausschnitt=" + ",".join(bruch_GanzZahlReziproke)
    else:
        zeiln3 = ""
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

            zeiln2 = anotherOberesMaximum(c, maxNum)
    else:
        zeiln1 = ""
        zeiln2 = ""

    if bedingungZahl:
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
                *[
                    "--keineleereninhalte"
                    if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                    in stext
                    else ""
                ],
            ] + returnOnlyParasAsList(stext)
            kette += ketten
            if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar" not in stext:
                print(" ".join(kette))
            reta.Program(
                kette,
                int(shellRowsAmountStr),
            )

    # if bedingungZahl or bedingungBrueche:
    if fullBlockIsZahlenbereichAndBruch and (bedingungZahl or bedingungBrueche):
        if len({"absicht", "absichten", "motiv", "motive"} & set(stext)) > 0 or (
            (("a" in stext) != ("mo" in stext))
            and "abc" not in stext
            and "abcd" not in stext
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
                    "--menschliches=motivation",
                    "--breite=" + str(int(shellRowsAmountStr) - 2),
                    "-ausgabe",
                    "--spaltenreihenfolgeundnurdiese=1",
                    *[
                        "--keineleereninhalte"
                        if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                        in stext
                        else ""
                    ],
                ] + returnOnlyParasAsList(stext)
                kette += ketten
                if (
                    "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                    not in stext
                ):
                    print(" ".join(kette))
                reta.Program(
                    kette,
                    int(shellRowsAmountStr),
                )

            if len(bruch_GanzZahlReziproke) > 0 and zeiln3 != "":
                import reta

                kette = [
                    "reta",
                    "-zeilen",
                    zeiln3,
                    zeiln2,
                    "-spalten",
                    "--menschliches=motivation",
                    "--breite=" + str(int(shellRowsAmountStr) - 2),
                    "-ausgabe",
                    "--spaltenreihenfolgeundnurdiese=3",
                    *[
                        "--keineleereninhalte"
                        if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                        in stext
                        else ""
                    ],
                ] + returnOnlyParasAsList(stext)
                kette += ketten
                if (
                    "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                    not in stext
                ):
                    print(" ".join(kette))
                reta.Program(
                    kette,
                    int(shellRowsAmountStr),
                )

            if len(rangesBruecheDict) > 0:
                for nenner, zaehler in rangesBruecheDict.items():
                    import reta

                    hierBereich = ",".join(zaehler)
                    kette = [
                        "reta",
                        "-zeilen",
                        "--vorhervonausschnitt=" + hierBereich,
                        "-spalten",
                        "--gebrochengalaxie=" + str(nenner),
                        "--breite=" + str(int(shellRowsAmountStr) - 2),
                        "-kombination",
                        "-ausgabe",
                        "--spaltenreihenfolgeundnurdiese=1",
                        *[
                            "--keineleereninhalte"
                            if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                            in stext
                            else ""
                        ],
                    ] + returnOnlyParasAsList(stext)
                    kette += ketten
                    if (
                        "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                        not in stext
                    ) and not len(BereichToNumbers2(hierBereich)) == 0:
                        print(" ".join(kette))
                    reta.Program(
                        kette,
                        int(shellRowsAmountStr),
                    )
            elif len(rangesBruecheDictReverse) > 0:
                for nenner, zaehler in rangesBruecheDictReverse.items():
                    import reta

                    hierBereich = ",".join(zaehler)
                    kette = [
                        "reta",
                        "-zeilen",
                        "--vorhervonausschnitt=" + hierBereich,
                        "-spalten",
                        "--gebrochengalaxie=" + str(nenner),
                        "--breite=" + str(int(shellRowsAmountStr) - 2),
                        "-kombination",
                        "-ausgabe",
                        "--spaltenreihenfolgeundnurdiese=2",
                        *[
                            "--keineleereninhalte"
                            if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                            in stext
                            else ""
                        ],
                    ] + returnOnlyParasAsList(stext)
                    kette += ketten
                    if (
                        "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                        not in stext
                    ) and not len(BereichToNumbers2(hierBereich)) == 0:
                        print(" ".join(kette))
                    reta.Program(
                        kette,
                        int(shellRowsAmountStr),
                    )

        eigN, eigR = [], []
        for aa in stext:
            if "EIGN" == aa[:4]:
                eigN += [aa[4:]]
            if "EIGR" == aa[:4]:
                eigR += [aa[4:]]

        if len(eigN) > 0:
            warBefehl = True
            if len(c) > 0:
                import reta

                kette = [
                    "reta",
                    "-zeilen",
                    zeiln1,
                    zeiln2,
                    "-spalten",
                    "--konzept=" + ",".join(eigN),
                    "--breite=" + str(int(shellRowsAmountStr) - 2),
                    "-ausgabe",
                    *[
                        "--keineleereninhalte"
                        if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                        in stext
                        else ""
                    ],
                ] + returnOnlyParasAsList(stext)
                kette += ketten
                if (
                    "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                    not in stext
                ):
                    print(" ".join(kette))
                reta.Program(
                    kette,
                    int(shellRowsAmountStr),
                )

        if len(eigR) > 0:
            warBefehl = True
            if len(c) > 0:
                import reta

                kette = [
                    "reta",
                    "-zeilen",
                    zeiln1,
                    zeiln2,
                    "-spalten",
                    "--konzept2=" + ",".join(eigR),
                    "--breite=" + str(int(shellRowsAmountStr) - 2),
                    "-ausgabe",
                    *[
                        "--keineleereninhalte"
                        if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                        in stext
                        else ""
                    ],
                ] + returnOnlyParasAsList(stext)
                kette += ketten
                if (
                    "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                    not in stext
                ):
                    print(" ".join(kette))
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
                    *[
                        "--keineleereninhalte"
                        if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                        in stext
                        else ""
                    ],
                ] + returnOnlyParasAsList(stext)
                kette += ketten
                if (
                    "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                    not in stext
                ):
                    print(" ".join(kette))
                reta.Program(
                    kette,
                    int(shellRowsAmountStr),
                )

            if len(bruch_GanzZahlReziproke) > 0 and zeiln3 != "":
                import reta

                kette = [
                    "reta",
                    "-zeilen",
                    zeiln3,
                    zeiln2,
                    "-spalten",
                    "--universum=transzendentaliereziproke",
                    "--breite=" + str(int(shellRowsAmountStr) - 2),
                    "-ausgabe",
                    "--spaltenreihenfolgeundnurdiese=1",
                    *[
                        "--keineleereninhalte"
                        if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                        in stext
                        else ""
                    ],
                ] + returnOnlyParasAsList(stext)
                kette += ketten
                if (
                    "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                    not in stext
                ):
                    print(" ".join(kette))
                reta.Program(
                    kette,
                    int(shellRowsAmountStr),
                )

            if len(rangesBruecheDict) > 0:
                for nenner, zaehler in rangesBruecheDict.items():
                    import reta

                    hierBereich = ",".join(zaehler)
                    kette = [
                        "reta",
                        "-zeilen",
                        "--vorhervonausschnitt=" + hierBereich,
                        "-spalten",
                        "--gebrochenuniversum=" + str(nenner),
                        "--breite=" + str(int(shellRowsAmountStr) - 2),
                        "-kombination",
                        "-ausgabe",
                        "--spaltenreihenfolgeundnurdiese=1",
                        *[
                            "--keineleereninhalte"
                            if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                            in stext
                            else ""
                        ],
                    ] + returnOnlyParasAsList(stext)
                    kette += ketten
                    if (
                        "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                        not in stext
                    ) and not len(BereichToNumbers2(hierBereich)) == 0:
                        print(" ".join(kette))
                    reta.Program(
                        kette,
                        int(shellRowsAmountStr),
                    )
            elif len(rangesBruecheDictReverse) > 0:
                for nenner, zaehler in rangesBruecheDictReverse.items():
                    import reta

                    hierBereich = ",".join(zaehler)
                    kette = [
                        "reta",
                        "-zeilen",
                        "--vorhervonausschnitt=" + hierBereich,
                        "-spalten",
                        "--gebrochenuniversum=" + str(nenner),
                        "--breite=" + str(int(shellRowsAmountStr) - 2),
                        "-kombination",
                        "-ausgabe",
                        "--spaltenreihenfolgeundnurdiese=2",
                        *[
                            "--keineleereninhalte"
                            if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                            in stext
                            else ""
                        ],
                    ] + returnOnlyParasAsList(stext)
                    kette += ketten
                    if (
                        "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                        not in stext
                    ) and not len(BereichToNumbers2(hierBereich)) == 0:
                        print(" ".join(kette))
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
                *[
                    "--keineleereninhalte"
                    if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                    in stext
                    else ""
                ],
            ] + returnOnlyParasAsList(stext)
            kette += ketten
            if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar" not in stext:
                print(" ".join(kette))
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
                *[
                    "--keineleereninhalte"
                    if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                    in stext
                    else ""
                ],
            ] + returnOnlyParasAsList(stext)
            kette += ketten
            if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar" not in stext:
                print(" ".join(kette))
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
                *[
                    "--keineleereninhalte"
                    if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                    in stext
                    else ""
                ],
            ] + returnOnlyParasAsList(stext)
            kette += ketten
            if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar" not in stext:
                print(" ".join(kette))
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
                anotherOberesMaximum(c, 1028),
                "-spalten",
                "--bedeutung=primzahlkreuz",
                "--breite=" + str(int(shellRowsAmountStr) - 2),
                "-ausgabe",
                *[
                    "--keineleereninhalte"
                    if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                    in stext
                    else ""
                ],
            ] + returnOnlyParasAsList(stext)
            kette += ketten
            if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar" not in stext:
                print(" ".join(kette))
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
                *[
                    "--keineleereninhalte"
                    if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                    in stext
                    else ""
                ],
            ] + returnOnlyParasAsList(stext)
            kette += ketten
            if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar" not in stext:
                print(" ".join(kette))
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
                    *[
                        "--keineleereninhalte"
                        if "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                        in stext
                        else ""
                    ],
                ] + returnOnlyParasAsList(stext)
                kette += ketten
                if (
                    "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                    not in stext
                ):
                    print(" ".join(kette))
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
            print("Das ist kein Befehl! -> '{}''".format(" ".join(stext)))
    return loggingSwitch


def bruchBereichsManagementAndWbefehl(c, stext, zahlenAngaben_):
    bruch_GanzZahlReziproke = []
    bruch_KeinGanzZahlReziproke = []
    bruch_KeinGanzZahlReziprok_ = []
    fullBlockIsZahlenbereichAndBruch = True
    bruchRanges2 = []
    bruch_KeinGanzZahlReziprokeEn = []
    rangesBruecheDict = {}
    rangesBruecheDictReverse: dict = {}
    bruch_KeinGanzZahlReziprokeEnDictAbzug = {}
    bruchRanges3Abzug = {}
    for g, a in enumerate(stext):
        bruchAndGanzZahlEtwaKorrekterBereich = []
        bruchBereichsAngaben = []
        bruchRanges = []
        abzug = False
        for etwaBruch in a.split(","):
            bruchRange, bruchBereichsAngabe = createRangesForBruchLists(
                bruchSpalt(etwaBruch)
            )
            print("_ {}".format(bruchBereichsAngabe))
            (
                bruchAndGanzZahlEtwaKorrekterBereich,
                bruchBereichsAngaben,
                bruchRanges,
                zahlenAngaben_,
                etwaAllTrue,
            ) = verifyBruchNganzZahlBetweenCommas(
                bruchAndGanzZahlEtwaKorrekterBereich,
                bruchBereichsAngabe,
                bruchBereichsAngaben,
                bruchRange,
                bruchRanges,
                etwaBruch,
                zahlenAngaben_,
            )
            print(bruchBereichsAngaben)
            if etwaAllTrue:
                fullBlockIsZahlenbereichAndBruch = (
                    fullBlockIsZahlenbereichAndBruch
                    and all(bruchAndGanzZahlEtwaKorrekterBereich)
                )

        print(bruchBereichsAngaben)
        for bruchBereichsAngabe, bruchRange in zip(bruchBereichsAngaben, bruchRanges):
            if isZeilenAngabe(bruchBereichsAngabe):
                if 1 in bruchRange:
                    bruch_GanzZahlReziproke += [bruchBereichsAngabe]
                if len(bruchRange) > 1 or 1 not in bruchRange:
                    bruch_KeinGanzZahlReziproke += [bruchBereichsAngabe]
                    bruchRanges2 += [bruchRange]
        bruchDict = {}
        for bruchRange, bruch_KeinGanzZahlReziprok_ in zip(
            bruchRanges2, bruch_KeinGanzZahlReziproke
        ):
            for rangePunkt in bruchRange:
                if rangePunkt != 1:
                    try:
                        bruchDict[rangePunkt] |= {bruch_KeinGanzZahlReziprok_}
                    except KeyError:
                        bruchDict[rangePunkt] = {bruch_KeinGanzZahlReziprok_}
        bruchRanges = []
        bruch_KeinGanzZahlReziprokeEn = []
        bruchRange = []
        for key, value in bruchDict.items():
            if key != 1 and (
                (key not in bruchRange) and (value not in bruch_KeinGanzZahlReziprokeEn)
            ):
                bruchRange += [key]
                bruch_KeinGanzZahlReziprokeEn += [value]
        bruch_GanzZahlReziproke = list(set(bruch_GanzZahlReziproke))
        if len(zahlenAngaben_) > 0:
            a = ",".join(zahlenAngaben_)
            c2 = ",".join([str(zahl) for zahl in BereichToNumbers2(a, False, 0)])
            if "w" in stext or "teiler" in stext:
                c: str = ",".join(teiler(a)[0])
            else:
                c = a
        if ("v" in stext) or ("vielfache" in stext):
            bruchRanges3 = {}
            bruch_KeinGanzZahlReziprokeEnDict = {}
            for k, (br, no1brueche) in enumerate(
                zip(bruchRange, bruch_KeinGanzZahlReziprokeEn)
            ):

                for no1bruch in no1brueche:
                    i = 1
                    if len(no1bruch) > 0 and no1bruch[0] == "v":
                        no1bruch = no1bruch[1:]
                    if len(no1bruch) > 0 and no1bruch[0] == "-":
                        no1bruch = no1bruch[1:]
                        print("abzug true {}".format(no1bruch))
                        abzug = True
                    else:
                        print("abzug false {}".format(no1bruch))
                        abzug = False
                    no1bruch = int(no1bruch) if no1bruch.isdecimal() else 0
                    print("l {}".format(no1bruch))
                    rechnung2 = no1bruch * i
                    while rechnung2 in gebrochenErlaubteZahlen:
                        print(rechnung2)
                        if rechnung2 not in bruch_KeinGanzZahlReziprokeEnDict.values():
                            if abzug:
                                print("z abzug {}: {}".format(rechnung2, rechnung2))
                                try:
                                    bruch_KeinGanzZahlReziprokeEnDictAbzug[k] += [
                                        rechnung2
                                    ]
                                except KeyError:
                                    bruch_KeinGanzZahlReziprokeEnDictAbzug[k] = [
                                        rechnung2
                                    ]
                            else:
                                print("z dazu {}: {}".format(rechnung2, rechnung2))
                                try:
                                    bruch_KeinGanzZahlReziprokeEnDict[k] += [rechnung2]
                                except KeyError:
                                    bruch_KeinGanzZahlReziprokeEnDict[k] = [rechnung2]
                        i += 1
                        rechnung2 = no1bruch * i
                i = 1
                rechnung = br * i
                while rechnung in gebrochenErlaubteZahlen:
                    print(rechnung)
                    if abzug:
                        try:
                            if rechnung not in bruchRanges3Abzug:
                                bruchRanges3Abzug[k] += [rechnung]
                        except KeyError:
                            bruchRanges3Abzug[k] = [rechnung]
                    else:
                        try:
                            if rechnung not in bruchRanges3:
                                bruchRanges3[k] += [rechnung]
                        except KeyError:
                            bruchRanges3[k] = [rechnung]
                    i += 1
                    rechnung = br * i

            print("abzug if true {}".format(abzug))
            print("jjj {}: {}".format(bruchRanges3, bruch_KeinGanzZahlReziprokeEnDict))
            for keyRanges, valueRanges in bruchRanges3.items():
                for (
                    keyBrueche,
                    valueBrueche,
                ) in bruch_KeinGanzZahlReziprokeEnDict.items():
                    for eineRange in valueRanges:
                        for einBruch in valueBrueche:
                            if keyRanges == keyBrueche:
                                print("s dazu {}:{}".format(eineRange, einBruch))
                                try:
                                    strBruch = str(einBruch)
                                    if strBruch not in rangesBruecheDict[eineRange]:
                                        rangesBruecheDict[eineRange] += [strBruch]
                                except KeyError:
                                    rangesBruecheDict[eineRange] = [str(einBruch)]
            print(
                "jjj {}: {}".format(
                    bruchRanges3Abzug, bruch_KeinGanzZahlReziprokeEnDictAbzug
                )
            )
            if len(bruchRanges3Abzug) > 0:
                print("jjj- {}: {}".format(bruchRanges3, rangesBruecheDict))
                rangesBruecheDict2 = deepcopy(rangesBruecheDict)
                bruchRanges4 = deepcopy(bruchRanges3)
                for AbzugNenners, AbzugZaehlers in zip(
                    bruchRanges3Abzug.values(),
                    bruch_KeinGanzZahlReziprokeEnDictAbzug.values(),
                ):
                    for aNenner, aZaehler in zip(AbzugNenners, AbzugZaehlers):
                        print("s abzug {}:{}".format(aNenner, aZaehler))
                        for key, value in zip(
                            bruchRanges3.values(), rangesBruecheDict.values()
                        ):
                            print("bla {}:{}".format(key, value))
                            try:
                                if key.index(int(aNenner)) == value.index(
                                    str(aZaehler)
                                ):
                                    print("bla2 {}:{}".format(key, aNenner))
                                    print("bla3 {}".format(rangesBruecheDict))
                                    print(
                                        "bla4 {}:{}:{}:{}".format(
                                            value, aZaehler, key, aNenner
                                        )
                                    )
                                    try:
                                        value.remove(str(aZaehler))
                                    except:
                                        pass
                                    try:
                                        key.remove(str(aNenner))
                                    except:
                                        pass
                                    try:
                                        value.remove(aZaehler)
                                    except:
                                        pass
                                    try:
                                        key.remove(aNenner)
                                    except:
                                        pass
                                    print("bla5 {}:{}:{}".format(aNenner, key, value))
                                    rangesBruecheDict2[aNenner] = value
                                    bruchRanges4[aNenner] = key
                            except ValueError:
                                pass
                rangesBruecheDict = rangesBruecheDict2
                bruchRanges3 = bruchRanges4
                bruchRanges3Abzug = {}
                bruch_KeinGanzZahlReziprokeEnDictAbzug = {}
            print("jjj_ {}: {}".format(bruchRanges3, rangesBruecheDict))
        else:
            rangesBruecheDict = bruchDict
        valueLenSum = 0
        bereicheVorherBestimmtListofSets = []
        bereicheVorherBestimmtSet = set()
        for values in rangesBruecheDict.values():
            bereichVorherBestimmt = [BereichToNumbers2(value) for value in values]
            bereicheVorherBestimmtListofSets += bereichVorherBestimmt
            neuSet = set()
            for b in bereichVorherBestimmt:
                neuSet |= b
            bereicheVorherBestimmtSet |= b
        valueLenSum += len(bereicheVorherBestimmtSet)
        del bereicheVorherBestimmtSet
        dictLen = len(rangesBruecheDict)
        if dictLen != 0:
            avg = valueLenSum / dictLen
            if avg < 1:
                print(
                    "zu {}:{}".format(
                        bereicheVorherBestimmtListofSets, rangesBruecheDict
                    )
                )
                for ListeAusBereichNummern, (key, values) in zip(
                    bereicheVorherBestimmtListofSets, rangesBruecheDict.items()
                ):
                    for value in values:
                        for newKey in ListeAusBereichNummern:
                            try:
                                strKey = str(key)
                                if strKey not in rangesBruecheDictReverse[newKey]:
                                    rangesBruecheDictReverse[newKey] += [strKey]
                            except KeyError:
                                rangesBruecheDictReverse[newKey] = [str(key)]
                rangesBruecheDict = {}

    try:
        del bruchRanges3
    except:
        pass
    try:
        del rechnung
    except:
        pass
    try:
        del rechnung2
    except:
        pass
    try:
        del bruchDict
    except:
        pass
    try:
        del no1brueche
    except:
        pass
    try:
        del bruchRanges
    except:
        pass
    try:
        del bruchRange
    except:
        pass
    try:
        del bruchRange2
    except:
        pass
    try:
        del bruch_KeinGanzZahlReziproke
    except:
        pass
    try:
        del bruch_KeinGanzZahlReziprokeEn
    except:
        pass
    try:
        c2
    except:
        c2 = ""
    print(
        "{},{},{},{},{}".format(
            bruch_GanzZahlReziproke,
            fullBlockIsZahlenbereichAndBruch,
            rangesBruecheDict,
            zahlenAngaben_,
            rangesBruecheDictReverse,
        )
    )
    return (
        bruch_GanzZahlReziproke,
        c,
        c2,
        fullBlockIsZahlenbereichAndBruch,
        rangesBruecheDict,
        len(zahlenAngaben_) > 0,
        rangesBruecheDictReverse,
    )


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
    ifKurzKurz = False
    if len(stext) > 0:
        textDazu: list = []
        stext2: list = []
        s_2: list

        ifKurzKurz, stext = stextFromKleinKleinKleinBefehl(
            ifKurzKurz, promptMode2, stext, stext2, textDazu
        )
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
    zahlenAngaben_ = []
    c = ""
    if len(set(stext) & befehleBeenden) > 0:
        stext = [tuple(befehleBeenden)[0]]
    replacements = {
        "e": "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar",
        "a": "absicht",
        "u": "universum",
        "t": "thomas",
        "r": "richtung",
        "v": "vielfache",
        "h": "help",
        "w": "teiler",
        "S": "BefehlSpeichernDanach",
        "s": "BefehlSpeichernDavor",
        "l": "BefehlSpeicherungLöschen",
        "o": "BefehlSpeicherungAusgeben",
    }
    for i, token in enumerate(stext):
        try:
            stext[i] = replacements[token]
        except KeyError:
            pass
    stext = list(set(stext))
    return (
        bedingung,
        brueche,
        c,
        ketten,
        maxNum,
        stext,
        zahlenAngaben_,
        ifKurzKurz,
    )


def PromptAllesVorGroesserSchleife():
    global promptMode2, textDazu0, befehleBeenden
    pp1 = pprint.PrettyPrinter(indent=2)
    pp = pp1.pprint
    startpunkt1 = NestedCompleter(
        {a: None for a in befehle},
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
    text = str(text).strip()
    s_text = text.split()
    zuloeschen = text
    loeschbares1 = {i + 1: a for i, a in enumerate(platzhalter.split())}
    loeschbares2 = {a: i + 1 for i, a in enumerate(platzhalter.split())}
    flag = False
    if isZeilenAngabe(zuloeschen):
        if zuloeschen not in loeschbares2.keys():
            zuloeschen2 = BereichToNumbers2(zuloeschen, False, 0)
            for todel in zuloeschen2:
                try:
                    del loeschbares1[todel]
                except:
                    pass
            platzhalter = " ".join(loeschbares1.values())
        else:
            flag = True
    else:
        flag = True
    if flag:
        for wort in s_text:
            try:
                del loeschbares2[wort]
            except:
                pass
        platzhalter = " ".join(loeschbares2.keys())
    promptMode = PromptModus.normal
    if len(platzhalter.strip()) == 0:
        promptMode2 = PromptModus.normal
        textDazu0 = []
    textDazu0 = platzhalter.split()
    return platzhalter, promptMode, text


def promptSpeicherungB(nochAusageben, platzhalter, promptMode, text):
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
        text: str = str(text).strip()
    except KeyboardInterrupt:
        sys.exit()
    return befehlDavor, text


PromptScope()
