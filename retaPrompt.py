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

from center import (alxp, cliout, i18n, invert_dict_B, isZeilenAngabe,
                    isZeilenAngabe_betweenKommas, isZeilenBruchAngabe, moduloA,
                    primfaktoren, primRepeat, retaPromptHilfe, teiler,
                    textHatZiffer, x)
from LibRetaPrompt import (BereichToNumbers2, PromptModus,
                           gebrochenErlaubteZahlen, isReTaParameter,
                           notParameterValues, stextFromKleinKleinKleinBefehl,
                           verifyBruchNganzZahlBetweenCommas, verkuerze_dict,
                           wahl15, wahl16)
from multis import mult
# import reta
from nestedAlx import (ComplSitua, NestedCompleter, ausgabeParas, befehle,
                       befehle2, hauptForNeben, kombiMainParas, mainParas,
                       reta, retaProgram, spalten, spaltenDict, zeilenParas)
from word_completerAlx import WordCompleter

i18nRP = i18n.retaPrompt
wahl15[""] = wahl15["15"]
wahl16[""] = wahl16["16"]
befehle += ["15_"]
befehle += ["16_"]
befehleBeenden = i18nRP.befehleBeenden
# befehleBeenden = {"ende", "exit", "quit", "q", ":q"}
infoLog = False
sprachenWahl = "deutsch"


class TXT(object):
    _text = ""
    _platzhalter = ""
    _stext = []
    _stextE = []
    _e = []
    _stextEmenge = {}
    _stextSet = {}
    _befehlDavor = ""

    def hasWithoutABC(self, hasSet: set) -> bool:
        """tells if any values of given set exists in TXT.menge and command abc and abcd is not inside"""
        return (
            len(hasSet & self._stextSet) > 0
            and len({"abc", "abcd"} & self._stextSet) == 0
        )

    def has(self, hasSet: set) -> bool:
        """tells if any values of given set exists in TXT.menge"""
        return len(hasSet & self._stextSet) > 0

    def __init__(self, txt=""):
        self.text = txt

    @property
    def e(self):
        return self._e

    @property
    def menge(self):
        return self._stextSet

    @property
    def listeE(self):
        return self._stextE

    @property
    def liste(self):
        return self._stext

    @property
    def mengeE(self):
        return self._stextEmenge

    @property
    def platzhalter(self):
        return self._platzhalter

    @property
    def text(self):
        return self._text

    @platzhalter.setter
    def platzhalter(self, value):
        self._platzhalter = value

    @text.setter
    def text(self, value):
        assert type(value) is str
        self._text = str(value).strip()
        self._stext = self._text.split()
        self._stextSet = set(self._stext)
        self._stextEmenge = self._stextSet | set(self._e)
        self._stextE = self._stext + self._e

    @liste.setter
    def liste(self, value):
        assert type(value) is list
        self._stext = value
        self._stextSet = set(value)
        self._stextEmenge = self._stextSet | set(self._e)
        self._stextE = self._stext + self._e

    @e.setter
    def e(self, value):
        assert type(value) is list
        self._e = value
        self._stextEmenge = self._stextSet | set(self._e)
        self._stextE = self._stext + self._e

    @property
    def befehlDavor(self):
        return self._befehlDavor

    @befehlDavor.setter
    def befehlDavor(self, value):
        self._befehlDavor = value


def anotherOberesMaximum(zahlenBereichC, maxNum):
    maximizing = list(BereichToNumbers2(zahlenBereichC, False, 0))
    if len(maximizing) > 0:
        maximizing.sort()
        maxNum2 = maximizing[-1]
    else:
        maxNum2 = maxNum
    return (
        "--" + i18n.zeilenParas["oberesmaximum"] + "=" + str(max(maxNum, maxNum2) + 1)
    )


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


# def externCommand(cmd: str, StrNummern: str):
#    nummern: list = list(BereichToNumbers2(StrNummern, False, 0))
#    nummern.sort()
#    nummernStr: list = [str(nummer) for nummer in nummern]
#    try:
#        process = subprocess.Popen(
#            [os.path.dirname(__file__) + os.sep + cmd, *nummernStr]
#        )
#        process.wait()
#    except:
#        pass
#


def grKl(A: set, B: set) -> tuple:
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
    bruchSpalten: list = text.split("/")
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
        flag: bool = False
        allVergleich: list[bool] = [
            zahl2 > zahl1 for zahl1, zahl2 in zip(keineZahl.keys(), zahl.keys())
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
    ergebnis2 = "".join(ergebnis)
    return listenRange, ergebnis2


def speichern(ketten, platzhalter, text):
    global promptMode2, textDazu0
    bedingung1 = len(platzhalter) > 0
    bedingung2 = len(ketten) > 0
    Txt = TXT(text)
    Txt.platzhalter = platzhalter
    if bedingung1 or bedingung2:
        if bedingung1:
            woRetaBefehl = []
            TxtPlatzhalter = TXT(Txt.platzhalter)
            if Txt.liste[:1] == ["reta"]:
                woRetaBefehl += ["bereits-dabei"]
                Txt.liste.pop(0)
            if TxtPlatzhalter.liste[:1] == ["reta"]:
                woRetaBefehl += ["bei-dazu"]
                TxtPlatzhalter.liste.pop(0)
            if len(woRetaBefehl) > 0:
                Txt.platzhalter = (
                    "reta " + " ".join(TxtPlatzhalter.liste) + " " + " ".join(Txt.liste)
                )
            else:  # erstes und zweites heißt nicht reta am Anfang
                # nochmal für nicht Kurzbefehle befehle, also ohne "reta" am Anfang
                textUndPlatzHalterNeu = []
                langKurzBefehle = []
                for rpBefehl in Txt.platzhalter.split() + Txt.liste:
                    if rpBefehl in befehle and len(rpBefehl) > 1:
                        langKurzBefehle += [rpBefehl.strip()]
                    else:  # Kurzbefehl oder irgendwas anderes
                        textUndPlatzHalterNeu += [rpBefehl.strip()]
                rpBefehlE = ""
                for rpBefehl in textUndPlatzHalterNeu:
                    rpBefehlSplitted = str(rpBefehl).split()
                    if len(rpBefehlSplitted) > 0:
                        rpBefehlE += " ".join(rpBefehlSplitted) + " "
                rpBefehlE = rpBefehlE[:-1]
                Txt2 = TXT()
                Txt2.liste = textUndPlatzHalterNeu
                ifKurzKurz, Txt2.liste = stextFromKleinKleinKleinBefehl(
                    PromptModus.AusgabeSelektiv, Txt2.liste, []
                )
                replacements = i18nRP.replacements
                if len(textUndPlatzHalterNeu) > 0 and Txt2.liste[0] not in [
                    "reta",
                    "shell",
                    "python",
                    "abstand",
                ]:
                    listeNeu: list = []
                    for token in Txt2.liste:
                        try:
                            listeNeu += [replacements[token]]
                        except KeyError:
                            listeNeu += [token]
                    Txt2.liste = listeNeu

                Txt.platzhalter = " ".join(Txt2.liste + langKurzBefehle)
    else:
        Txt.platzhalter = "" if Txt.text is None else str(Txt.text)
    Txt.text = ""
    if Txt.platzhalter != "" or not (bedingung1 or bedingung2):
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
        Txt.platzhalter,
        promptMode2,
        promptMode2,
        PromptModus.normal,
        Txt.platzhalter,
        [],
    )

    # textDazu0 = platzhalter.split()
    textDazu0 = stextX

    return ketten, Txt


def PromptScope():
    global promptMode2, textDazu0
    (
        befehleBeenden,
        loggingSwitch,
        promptDavorDict,
        promptMode,
        startpunkt1,
        nurEinBefehl,
        immerEbefehlJa,
    ) = PromptAllesVorGroesserSchleife()
    global textDazu0, sprachenWahl
    Txt = TXT("")
    nochAusageben = ""
    ketten = []
    while len(Txt.menge & befehleBeenden) == 0:
        cmd_gave_output = False
        promptModeLast = promptMode

        if promptMode not in (
            PromptModus.speicherungAusgaben,
            PromptModus.speicherungAusgabenMitZusatz,
        ):
            Txt = promptInput(
                loggingSwitch,
                promptDavorDict,
                promptMode,
                startpunkt1,
                Txt,
                nurEinBefehl,
                immerEbefehlJa,
            )
            ketten, Txt = promptSpeicherungA(ketten, promptMode, Txt)

        else:
            Txt = promptSpeicherungB(nochAusageben, promptMode, Txt)
            # textE = []

        if promptMode == PromptModus.loeschenSelect:
            Txt.text, promptMode, _ = PromptLoescheVorSpeicherungBefehle(
                Txt.platzhalter, promptMode, Txt.text
            )
            Txt.platzhalter = Txt.text
            textDazu0 = Txt.liste
            continue

        promptMode = PromptModus.normal

        if (
            (i18n.befehle2["S"] in Txt.liste)
            or (i18n.befehle2["BefehlSpeichernDanach"] in Txt.liste)
        ) and len(Txt.liste) == 1:
            promptMode = PromptModus.speichern
            continue
        elif (
            (i18n.befehle2["s"] in Txt.liste)
            or (i18n.befehle2["BefehlSpeichernDavor"] in Txt.liste)
        ) and len(Txt.liste) == 1:
            ketten, Txt = speichern(ketten, Txt.platzhalter, Txt.befehlDavor)
            promptMode = PromptModus.normal
            continue
        elif len(
            Txt.menge
            - {
                i18n.befehle2["s"],
                i18n.befehle2["BefehlSpeichernDavor"],
                i18n.befehle2["S"],
                i18n.befehle2["BefehlSpeichernDanach"],
            }
        ) > 0 and (
            len(
                Txt.menge
                & {
                    i18n.befehle2["s"],
                    i18n.befehle2["BefehlSpeichernDavor"],
                    i18n.befehle2["S"],
                    i18n.befehle2["BefehlSpeichernDanach"],
                }
            )
            == 1
        ):
            stextB = copy(Txt.liste)
            for val in (
                i18n.befehle2["s"],
                i18n.befehle2["S"],
                i18n.befehle2["BefehlSpeichernDavor"],
                i18n.befehle2["BefehlSpeichernDanach"],
            ):
                try:
                    stextB.remove(val)
                except ValueError:
                    pass
            ketten, Txt = speichern(ketten, Txt.platzhalter, " ".join(stextB))
            Txt.liste = []
            Txt.text = ""
            Txt.befehlDavor = ""
            promptMode = PromptModus.normal
            continue
        elif (
            (i18n.befehle2["o"] in Txt.liste)
            or ("BefehlSpeicherungAusgeben" in Txt.liste)
        ) and len(Txt.liste) == 1:
            promptMode = PromptModus.speicherungAusgaben
            continue
        elif (
            (i18n.befehle2["o"] in Txt.liste)
            or ("BefehlSpeicherungAusgeben" in Txt.liste)
        ) and len(Txt.menge - {i18n.befehle2["o"], "BefehlSpeicherungAusgeben"}) > 1:
            nochAusageben = Txt.liste
            promptMode = PromptModus.speicherungAusgabenMitZusatz
            continue
        elif (
            (i18n.befehle2["l"] in Txt.liste)
            or ("BefehlSpeicherungLöschen" in Txt.liste)
        ) and len(Txt.liste) == 1:

            if "--" + i18n.ausgabeParas["nocolor"] in Txt.listeE:
                print(str([{i + 1, a} for i, a in enumerate(Txt.platzhalter.split())]))
            else:
                cliout(
                    str([{i + 1, a} for i, a in enumerate(Txt.platzhalter.split())]),
                    True,
                )
                alxp(i18nRP.promptModeSatz.format(promptMode, promptMode2))
                promptMode = PromptModus.loeschenSelect
                continue

        text1, text2, text3 = verdreheWoReTaBefehl(
            Txt.platzhalter, Txt.text, textDazu0, promptMode
        )

        (
            IsPureOnlyReTaCmd,
            brueche,
            zahlenBereichC,
            ketten,
            maxNum,
            Txt.liste,
            zahlenAngaben_,
            ifKurzKurz,
        ) = promptVorbereitungGrosseAusgabe(
            text1,
            promptMode,
            promptMode2,
            promptModeLast,
            text2,
            text3,
        )
        loggingSwitch = PromptGrosseAusgabe(
            IsPureOnlyReTaCmd,
            befehleBeenden,
            brueche,
            zahlenBereichC,
            ketten,
            loggingSwitch,
            maxNum,
            cmd_gave_output,
            zahlenAngaben_,
            ifKurzKurz,
            nurEinBefehl,
            Txt,
        )


def PromptGrosseAusgabe(
    IsPureOnlyReTaCmd,
    befehleBeenden,
    brueche,
    zahlenBereichC,
    ketten,
    loggingSwitch,
    maxNum,
    cmd_gave_output,
    zahlenAngaben_,
    ifKurzKurz,
    nurEinBefehl,
    Txt,
):
    # global alxp, cliout, i18n, invert_dict_B, isZeilenAngabe, isZeilenAngabe_betweenKommas, isZeilenBruchAngabe, moduloA, primfaktoren, primRepeat, retaPromptHilfe, teiler, textHatZiffer, x
    global i18nRP, sprachenWahl

    (
        EsGabzahlenAngaben,
        zahlenReiheKeineWteiler,
        bruch_GanzZahlReziproke,
        fullBlockIsZahlenbereichAndBruch,
        rangesBruecheDict,
        rangesBruecheDictReverse,
    ) = (False, "", [], False, {}, {})
    if not IsPureOnlyReTaCmd:
        (
            bruch_GanzZahlReziproke,
            zahlenBereichC,
            zahlenReiheKeineWteiler,
            fullBlockIsZahlenbereichAndBruch,
            rangesBruecheDict,
            EsGabzahlenAngaben,
            rangesBruecheDictReverse,
            Txt.liste,
        ) = bruchBereichsManagementAndWbefehl(zahlenBereichC, Txt.liste, zahlenAngaben_)
    if i18n.befehle2["mulpri"] in Txt.listeE or i18n.befehle2["p"] in Txt.listeE:
        Txt.liste += [i18n.befehle2["multis"], i18n.befehle2["prim"]]

    if ifPrintCmdAgain(Txt):
        if "--" + i18n.ausgabeParas["nocolor"] in Txt.listeE:
            print("[code]" + Txt.text + "[/code]")
        else:
            cliout("[code]" + Txt.text + "[/code]", True, "bbcode")
    if (
        ifKurzKurz
        and i18n.befehle2["keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"]
        not in Txt.listeE
    ):

        if "--" + i18n.ausgabeParas["nocolor"] in Txt.listeE:
            print(i18nRP.promptModeSatz2.format(" ".join(Txt.listeE), Txt.text))
        else:
            cliout(
                i18nRP.promptModeSatz2.format(" ".join(Txt.listeE), Txt.text), True, ""
            )
    if (
        i18n.befehle2["abc"] in Txt.listeE or i18n.befehle2["abcd"] in Txt.listeE
    ) and len(Txt.liste) == 2:
        cmd_gave_output = True
        buchstabe: str
        if (
            Txt.liste[0] == i18n.befehle2["abc"]
            or Txt.liste[0] == i18n.befehle2["abcd"]
        ):
            buchstaben = Txt.liste[1]
        else:
            buchstaben = Txt.liste[0]
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
    if len({i18n.befehle2["befehle"]} & Txt.mengeE) > 0:
        cmd_gave_output = True
        print("{}: {}".format(i18nRP.befehleWort["Befehle"], str(befehle)[1:-1]))
    if len({i18n.befehle2["help"], i18n.befehle2["hilfe"]} & Txt.mengeE) > 0 or (
        i18n.befehle2["h"] in Txt.listeE
        and i18n.befehle2["abc"] not in Txt.listeE
        and i18n.befehle2["abcd"] not in Txt.listeE
    ):
        cmd_gave_output = True
        retaPromptHilfe()
    bedingungZahl, bedingungBrueche = (
        EsGabzahlenAngaben,
        (len(bruch_GanzZahlReziproke) > 0 or len(rangesBruecheDict) > 0)
        or len(rangesBruecheDictReverse) > 0,
    )
    if IsPureOnlyReTaCmd:
        cmd_gave_output = True
        import reta

        if (
            i18n.befehle2["keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"]
            not in Txt.listeE
            and not ifKurzKurz
        ):
            if not ifPrintCmdAgain(Txt):
                # weil sonst das doppelt gemacht wird
                cliout(" ".join(Txt.liste), True, "")
        reta.Program(Txt.liste)

    zeiln1, zeiln2, zeiln3, zeiln4 = zeiln1234create(
        Txt,
        bedingungZahl,
        bruch_GanzZahlReziproke,
        zahlenBereichC,
        maxNum,
        zahlenReiheKeineWteiler,
    )

    if bedingungZahl:
        if (len({i18n.befehle2["thomas"]} & Txt.mengeE) > 0) or (
            i18n.befehle2["t"] in Txt.listeE
            and i18n.befehle2["abc"] not in Txt.listeE
            and i18n.befehle2["abcd"] not in Txt.listeE
        ):
            cmd_gave_output = True
            retaExecuteNprint(
                ketten,
                Txt.listeE,
                zeiln1,
                zeiln2,
                [
                    "".join(
                        ("--", i18n.ParametersMain.galaxie[0], "=", i18n.thomasWort)
                    ),
                ],
                "2",
            )

    if (
        False
        and {"english", "englisch"} & Txt.menge != set()
        and sys.argv[0].split(os.sep)[-1] == "rpl"
    ):
        cmd_gave_output = True
        sprachenWahl = "english"
        print("set to english")
        return loggingSwitch
        from importlib import reload

        import __main__
        import prompt_toolkit
        import prompt_toolkit.completion
        import prompt_toolkit.history
        import prompt_toolkit.styles

        import center
        import lib4tables
        import lib4tables_concat
        import lib4tables_Enum
        import lib4tables_prepare
        import LibRetaPrompt
        import nestedAlx
        import reta
        import retaPrompt
        import tableHandling
        import word_completerAlx

        for a in range(2):
            reload(center)
            reload(i18n)
            reload(LibRetaPrompt)
            reload(tableHandling)
            reload(reta)
            reload(nestedAlx)
            reload(word_completerAlx)
            reload(tableHandling)
            reload(lib4tables_Enum)
            reload(lib4tables_prepare)
            reload(lib4tables)
            reload(lib4tables_concat)
            reload(prompt_toolkit)
            reload(prompt_toolkit.completion)
            reload(prompt_toolkit.history)
            reload(prompt_toolkit.styles)
            reload(retaPrompt)
            i18nRP = i18n.retaPrompt

    if fullBlockIsZahlenbereichAndBruch and (bedingungZahl or bedingungBrueche):
        was_n_1proN_cmd, cmd_gave_output = retaCmdAbstraction_n_and_1pron(
            Txt.hasWithoutABC({i18n.befehle2["emotion"], i18n.befehle2["E"]}),
            [
                "".join(
                    (
                        "--",
                        i18n.ParametersMain.grundstrukturen[0],
                        "=",
                        i18n.emotionWort,
                    )
                )
            ],
            None,
            ("1,2", "3,4"),
            Txt,
            bruch_GanzZahlReziproke,
            zahlenBereichC,
            ketten,
            cmd_gave_output,
            zeiln1,
            zeiln2,
            zeiln3,
            zeiln4,
        )
        was_n_1proN_cmd, cmd_gave_output = retaCmdAbstraction_n_and_1pron(
            Txt.hasWithoutABC({i18n.befehle2["B"], i18n.befehle2["bewusstsein"]}),
            [
                "".join(
                    (
                        "--",
                        i18n.ParametersMain.grundstrukturen[0],
                        "=",
                        wahl15["15"],
                    )
                )
            ],
            None,
            ("6", "7"),
            Txt,
            bruch_GanzZahlReziproke,
            zahlenBereichC,
            ketten,
            cmd_gave_output,
            zeiln1,
            zeiln2,
            zeiln3,
            zeiln4,
        )
        was_n_1proN_cmd, cmd_gave_output = retaCmdAbstraction_n_and_1pron(
            Txt.hasWithoutABC({i18n.befehle2["geist"], i18n.befehle2["G"]}),
            [
                "".join(
                    (
                        "--",
                        i18n.ParametersMain.grundstrukturen[0],
                        "=",
                        i18n.geistWort,
                    )
                )
            ],
            None,
            ("3", "4"),
            Txt,
            bruch_GanzZahlReziproke,
            zahlenBereichC,
            ketten,
            cmd_gave_output,
            zeiln1,
            zeiln2,
            zeiln3,
            zeiln4,
        )
        was_n_1proN_cmd, cmd_gave_output = retaCmdAbstraction_n_and_1pron(
            Txt.hasWithoutABC(
                {
                    i18n.befehle2["absicht"],
                    i18n.befehle2["absichten"],
                    i18n.befehle2["motiv"],
                    i18n.befehle2["motive"],
                    i18n.befehle2["a"],
                }
            ),
            [
                "".join(
                    (
                        "--",
                        i18n.ParametersMain.menschliches[0],
                        "=",
                        i18n.motivationWort,
                    )
                )
            ],
            None,
            ("1", "3"),
            Txt,
            bruch_GanzZahlReziproke,
            zahlenBereichC,
            ketten,
            cmd_gave_output,
            zeiln1,
            zeiln2,
            zeiln3,
            zeiln4,
        )
        if was_n_1proN_cmd:
            if len(rangesBruecheDict) > 0:
                cmd_gave_output = True
                for nenner, zaehler in rangesBruecheDict.items():
                    retaExecuteNprint(
                        ketten,
                        Txt.listeE,
                        "".join(("--", i18n.zeilenParas["vorhervonausschnitt"], "="))
                        + ",".join(zaehler),
                        "",
                        [
                            "".join(
                                (
                                    "--",
                                    i18n.gebrochenUniGal["gebrochengalaxie"],
                                    "=",
                                    str(nenner),
                                )
                            )
                        ],
                        "2",
                    )
            elif len(rangesBruecheDictReverse) > 0:
                cmd_gave_output = True
                for nenner, zaehler in rangesBruecheDictReverse.items():
                    retaExecuteNprint(
                        ketten,
                        Txt.listeE,
                        "".join(("--", i18n.zeilenParas["vorhervonausschnitt"], "="))
                        + ",".join(zaehler),
                        "",
                        [
                            "".join(
                                (
                                    "--",
                                    i18n.gebrochenUniGal["gebrochengalaxie"],
                                    "=",
                                    str(nenner),
                                )
                            )
                        ],
                        "1",
                    )

        eigN, eigR = [], []
        for aa in Txt.listeE:
            if i18n.EIGS_N_R[0] == aa[: len(i18n.EIGS_N_R[0])]:
                eigN += [aa[len(i18n.EIGS_N_R[0]) :]]
            if i18n.EIGS_N_R[1] == aa[: len(i18n.EIGS_N_R[1])]:
                eigR += [aa[len(i18n.EIGS_N_R[0]) :]]

        if len(eigN) > 0:
            if len(zahlenBereichC) > 0:
                cmd_gave_output = True
                retaExecuteNprint(
                    ketten,
                    Txt.listeE,
                    zeiln1,
                    zeiln2,
                    ["".join(("--", i18n.konzeptE["konzept"], "=", (",".join(eigN))))],
                    None,
                )

        if len(eigR) > 0:
            cmd_gave_output = True
            # zeilenAusReziprokenDazu = ",".join(
            #    [
            #        bruch.split("/")[0]
            #        for bruch in bruch_GanzZahlReziproke.split(",")
            #        if bruch.split("/")[0] != ""
            #    ]
            # )

            # if len(zeiln1) > 1 and i18n.zeilenParas["oberesmaximum"] not in zeiln1:
            #    zeiln1 += (
            #        "," if zeiln1[-1].isdecimal() else ""
            #    ) + zeilenAusReziprokenDazu
            # if len(zeiln2) > 1 and i18n.zeilenParas["oberesmaximum"] not in zeiln2:
            #    zeiln2 += (
            #        "," if zeiln2[-1].isdecimal() else ""
            #    ) + zeilenAusReziprokenDazu
            ZahlenAngabenCneu = zahlenBereichC + "," + bruch_GanzZahlReziproke
            x("CNEU", ZahlenAngabenCneu)
            ZahlenAngabenCneu = ZahlenAngabenCneu.replace(",,", ",")
            ZahlenAngabenCneu = ZahlenAngabenCneu.strip(",")
            x("CNEU", ZahlenAngabenCneu)

            TxtNeu = deepcopy(Txt)
            TxtNeu.text += " " + bruch_GanzZahlReziproke
            # zeiln1Neu, zeiln2Neu, _, _ = zeiln1234create(
            #    TxtNeu,
            #    lenbruch_GanzZahlReziproke > 0,
            #    "",
            #    cNeu,
            #    maxNum,
            #    zahlenReiheKeineWteiler
            #    + ("," if len(zahlenReiheKeineWteiler) > 0 else "")
            #    + bruch_GanzZahlReziproke,
            # )
            # x(
            #    "EIGR",
            #    (
            #        cNeu,
            #        ketten,
            #        Txt.listeE,
            #        " ".join((zeiln3, zeiln1)),
            #        " ".join((zeiln4, zeiln2)),
            #        zahlenReiheKeineWteiler,
            #    ),
            # )
            if len(ZahlenAngabenCneu) > 0:
                retaExecuteNprint(
                    ketten + ["-" + i18n.hauptForNeben["zeilen"], zeiln1, zeiln2],
                    Txt.listeE,
                    zeiln3,
                    zeiln4,
                    ["".join(("--", i18n.konzeptE["konzept2"], "=", (",".join(eigR))))],
                    None,
                )
            del ZahlenAngabenCneu
        was_n_1proN_cmd, cmd_gave_output = retaCmdAbstraction_n_and_1pron(
            Txt.hasWithoutABC({i18n.befehle2["universum"], i18n.befehle2["u"]}),
            [
                "".join(
                    (
                        "--",
                        i18n.ParametersMain.universum[0],
                        "=",
                        i18n.transzendentalienWort,
                    )
                )
            ],
            [
                "".join(
                    (
                        "--",
                        i18n.ParametersMain.universum[0],
                        "=",
                        i18n.transzendentaliereziprokeWort,
                    )
                )
            ],
            (
                "1" + (",4" if len(Txt.menge & set(befehle)) <= 2 else ""),
                "1" + (",2" if len(Txt.menge & set(befehle)) <= 2 else ""),
            ),
            Txt,
            bruch_GanzZahlReziproke,
            zahlenBereichC,
            ketten,
            cmd_gave_output,
            zeiln1,
            zeiln2,
            zeiln3,
            zeiln4,
        )
        if was_n_1proN_cmd:
            nennerZaehlerGleich = []
            if len(rangesBruecheDict) > 0:
                cmd_gave_output = True
                for nenner, zaehler in rangesBruecheDict.items():
                    hierBereich = ",".join(zaehler)
                    retaExecuteNprint(
                        ketten,
                        Txt.listeE,
                        "".join(("--", i18n.zeilenParas["vorhervonausschnitt"], "="))
                        + hierBereich,
                        "",
                        [
                            "".join(
                                (
                                    "--",
                                    i18n.gebrochenUniGal["gebrochenuniversum"],
                                    "=",
                                    str(nenner),
                                )
                            )
                        ],
                        "2",
                    )
                    nennerZaehlerGleich += findEqualNennerZaehler(
                        hierBereich, nenner, nennerZaehlerGleich
                    )

            elif len(rangesBruecheDictReverse) > 0:
                cmd_gave_output = True
                for nenner, zaehler in rangesBruecheDictReverse.items():
                    hierBereich = ",".join(zaehler)
                    retaExecuteNprint(
                        ketten,
                        Txt.listeE,
                        "".join(("--", i18n.zeilenParas["vorhervonausschnitt"], "="))
                        + hierBereich,
                        "",
                        [
                            "".join(
                                (
                                    "--",
                                    i18n.gebrochenUniGal["gebrochenuniversum"],
                                    "=",
                                    str(nenner),
                                )
                            )
                        ],
                        "1",
                    )
                    nennerZaehlerGleich += findEqualNennerZaehler(
                        hierBereich, nenner, nennerZaehlerGleich
                    )
            if len(nennerZaehlerGleich) != 0:
                cmd_gave_output = True
                nennerZaehlerGleich = set(nennerZaehlerGleich)
                nennerZaehlerGleich = ",".join(nennerZaehlerGleich)
                retaExecuteNprint(
                    ketten,
                    Txt.listeE,
                    "".join(("--", i18n.zeilenParas["vorhervonausschnitt"], "="))
                    + nennerZaehlerGleich,
                    "",
                    [
                        "".join(
                            (
                                "--",
                                i18n.ParametersMain.universum[0],
                                "=",
                                i18n.verhaeltnisgleicherzahlWort,
                            )
                        )
                    ],
                    "1",
                )
    if bedingungZahl:
        if (
            len(
                {i18n.befehle2["prim24"], i18n.befehle2["primfaktorzerlegungModulo24"]}
                & Txt.mengeE
            )
            > 0
        ):
            cmd_gave_output = True

            for arg in BereichToNumbers2(zahlenReiheKeineWteiler):
                print(
                    str(arg)
                    + ": "
                    + str(primRepeat(primfaktoren(int(arg), True)))[1:-1]
                    .replace("'", "")
                    .replace(", ", " ")
                )

        if Txt.hasWithoutABC({"prim", "primfaktorzerlegung"}):
            for arg in BereichToNumbers2(zahlenReiheKeineWteiler):
                cmd_gave_output = True
                print(
                    str(arg)
                    + ": "
                    + str(primRepeat(primfaktoren(int(arg))))[1:-1]
                    .replace("'", "")
                    .replace(", ", " ")
                )

        if Txt.hasWithoutABC({"multis"}) > 0:
            cmd_gave_output = True

            listeStrWerte = BereichToNumbers2(zahlenReiheKeineWteiler)
            mult(listeStrWerte)

            # externCommand(i18n.befehle2["prim"], c)

        if len({i18n.befehle2["mond"]} & Txt.mengeE) > 0:
            cmd_gave_output = True
            retaExecuteNprint(
                ketten,
                Txt.listeE,
                zeiln1,
                zeiln2,
                [
                    "".join(
                        (
                            "--",
                            i18n.ParametersMain.bedeutung[0],
                            "=",
                            i18n.gestirnWort,
                        )
                    )
                ],
                "3-6",
            )

        if len({i18n.befehle2["modulo"]} & Txt.mengeE) > 0:
            cmd_gave_output = True
            moduloA([str(num) for num in BereichToNumbers2(zahlenBereichC)])
        if len({i18n.befehle2["alles"]} & Txt.mengeE) > 0:
            cmd_gave_output = True
            retaExecuteNprint(
                ketten,
                Txt.listeE,
                zeiln1,
                zeiln2,
                ["--" + i18n.ParametersMain.alles[0]],
                None,
            )

        if len({i18n.befehle2["primzahlkreuz"]} & Txt.mengeE) > 0:
            cmd_gave_output = True
            retaExecuteNprint(
                ketten,
                Txt.listeE,
                zeiln1,
                anotherOberesMaximum(zahlenBereichC, 1028),
                [
                    "".join(
                        (
                            "--",
                            i18n.ParametersMain.bedeutung[0],
                            "=",
                            i18n.primzahlkreuzWort,
                        )
                    )
                ],
                None,
            )
            import reta

        if (len({i18n.befehle2["richtung"]} & Txt.mengeE) > 0) or (
            i18n.befehle2["r"] in Txt.listeE
            and i18n.befehle2["abc"] not in Txt.listeE
            and i18n.befehle2["abcd"] not in Txt.listeE
        ):
            cmd_gave_output = True
            retaExecuteNprint(
                ketten,
                Txt.listeE,
                zeiln1,
                zeiln2,
                [
                    "".join(
                        (
                            "--",
                            i18n.ParametersMain.primzahlwirkung[0],
                            "=",
                            i18n.GalaxieabsichtWort,
                        )
                    )
                ],
                None,
            )
        if (
            len(Txt.listeE) > 0
            and any(
                [token[:3] == "16_" and token[:5] != "16_15" for token in Txt.listeE]
            )
            and i18n.befehle2["abc"] not in Txt.listeE
            and i18n.befehle2["abcd"] not in Txt.listeE
        ):
            cmd_gave_output = True
            import reta

            befehle16 = []
            for token in Txt.listeE:
                if token[:3] == "16_":
                    befehle16 += [wahl16[token[3:]]]
            grundstruk = ",".join(befehle16)
            retaExecuteNprint(
                ketten,
                Txt.listeE,
                zeiln1,
                zeiln2,
                [
                    "".join(
                        (
                            "--",
                            i18n.ParametersMain.multiversum[0],
                            "=",
                            grundstruk,
                        )
                    )
                ],
                None,
            )
        if (
            len(Txt.listeE) > 0
            and any(
                [token[:3] == "15_" or token[:5] == "16_15" for token in Txt.listeE]
            )
            and i18n.befehle2["abc"] not in Txt.listeE
            and i18n.befehle2["abcd"] not in Txt.listeE
        ):
            cmd_gave_output = True
            import reta

            befehle15 = []
            for token in Txt.listeE:
                if token[:3] == "15_":
                    befehle15 += [wahl15[token[3:]]]
                if token == "16_15":
                    befehle15 += [wahl15["15"]]
                if token[:6] == "16_15_":
                    befehle15 += [wahl15[token[6:]]]
            grundstruk = ",".join(befehle15)
            retaExecuteNprint(
                ketten,
                Txt.listeE,
                zeiln1,
                zeiln2,
                [
                    "".join(
                        (
                            "--",
                            i18n.ParametersMain.grundstrukturen[0],
                            "=",
                            grundstruk,
                        )
                    )
                ],
                None,
            )
    if (
        len(Txt.liste) == 3
        and i18n.befehle2["abstand"] in Txt.liste
        and any([s.isdecimal() for s in Txt.liste])
    ):
        flag = False
        for i, s in enumerate(Txt.liste):
            if s.isdecimal():
                zahlNum = i
            if isZeilenAngabe(s):
                flag = True
                bereich = s
        if flag:
            cmd_gave_output = True
            zahl = int(Txt.liste[zahlNum])
            zeige = {b: abs(b - zahl) for b in BereichToNumbers2(bereich)}
            print(str(zeige)[1:-1])
    elif i18n.befehle2["abstand"] in Txt.liste:
        print(i18nRP.abstandMeldung)

    loggingSwitch, cmd_gave_output = PromptVonGrosserAusgabeSonderBefehlAusgaben(
        loggingSwitch, Txt, cmd_gave_output
    )
    if len(nurEinBefehl) > 0:
        Txt.liste = list(befehleBeenden)
        nurEinBefehl = " ".join(befehleBeenden)
        exit()
    if (
        not cmd_gave_output
        and len(Txt.liste) > 0
        and Txt.listeE[0] not in befehleBeenden
    ):
        if len(Txt.menge & set(befehle)) > 0:
            print(i18nRP.out1Saetze[0] + " ".join(Txt.listeE) + i18nRP.out1Saetze[1])
        else:
            print(i18nRP.out2Satz.format(" ".join(Txt.listeE)))
    return loggingSwitch


def retaCmdAbstraction_n_and_1pron(
    condition,
    paras,
    paras2,
    selectedCols,
    Txt,
    bruch_GanzZahlReziproke,
    zahlenBereichC,
    ketten,
    cmd_gave_output,
    zeiln1,
    zeiln2,
    zeiln3,
    zeiln4,
):
    """abstraction for commands giving results forr n and 1/n"""
    was_n_1proN_cmd = False
    if condition and (
        i18n.befehle2["abc"] not in Txt.listeE
        and i18n.befehle2["abcd"] not in Txt.listeE
    ):
        was_n_1proN_cmd = True
        if len(zahlenBereichC) > 0:
            cmd_gave_output = True
            retaExecuteNprint(
                ketten,
                Txt.listeE,
                zeiln1,
                zeiln2,
                paras,
                selectedCols[0],
            )
        if (
            len(bruch_GanzZahlReziproke) > 0
            and textHatZiffer(bruch_GanzZahlReziproke)
            and zeiln3 != ""
        ):
            cmd_gave_output = True
            retaExecuteNprint(
                ketten,
                Txt.listeE,
                zeiln3,
                zeiln4,
                paras if paras2 in [None, [], ()] else paras2,
                selectedCols[1],
            )
    return was_n_1proN_cmd, cmd_gave_output


def ifPrintCmdAgain(Txt):
    return (
        "".join(("--", i18n.ausgabeParas["art"], "=", i18n.ausgabeArt["bbcode"]))
        in Txt.listeE
        and "reta" == Txt.listeE[0]
    )


def zeiln1234create(
    Txt,
    bedingungZahl,
    bruch_GanzZahlReziproke,
    zahlenBereichC,
    maxNum,
    zahlenReiheKeineWteiler,
):
    if len(bruch_GanzZahlReziproke) > 0 and textHatZiffer(bruch_GanzZahlReziproke):
        zeiln3 = (
            "".join(("--", i18n.zeilenParas["vorhervonausschnitt"], "="))
            + bruch_GanzZahlReziproke
        )
        zeiln4 = ""
    else:
        zeiln3 = "".join(("--", i18n.zeilenParas["vorhervonausschnitt"], "=0"))
        zeiln4 = ""
    if bedingungZahl:
        zahlenBereiche = str(zahlenBereichC).strip()
        if textHatZiffer(zahlenBereiche):
            if i18n.befehle2["einzeln"] not in Txt.listeE and (
                (i18n.befehle2["vielfache"] in Txt.listeE)
                or (
                    i18n.befehle2["v"] in Txt.listeE
                    and i18n.befehle2["abc"] not in Txt.listeE
                    and i18n.befehle2["abcd"] not in Txt.listeE
                )
            ):
                if len(Txt.menge & {i18n.befehle2["teiler"], i18n.befehle2["w"]}) == 0:
                    zeiln1 = (
                        "".join(("--", i18n.zeilenParas["vielfachevonzahlen"], "="))
                        + zahlenReiheKeineWteiler
                    )
                else:
                    zeiln1 = ""
                zeiln2 = "".join(
                    [
                        "".join(("--", i18n.zeilenParas["vorhervonausschnitt"], "=")),
                        zahlenBereiche,
                        ",",
                        ",".join(
                            [
                                i18n.befehle2["v"] + str(z)
                                for z in zahlenReiheKeineWteiler.split(",")
                            ]
                        ),
                    ]
                )

                # zeiln2 = ""
            else:
                zeiln1 = (
                    "".join(("--", i18n.zeilenParas["vorhervonausschnitt"], "="))
                    + zahlenBereiche
                )

                zeiln2 = anotherOberesMaximum(zahlenBereichC, maxNum)
        else:
            zeiln1 = "".join(("--", i18n.zeilenParas["vorhervonausschnitt"], "=0"))
            zeiln2 = ""

    else:
        zeiln1 = ""
        zeiln2 = ""
    return zeiln1, zeiln2, zeiln3, zeiln4


def retaExecuteNprint(
    ketten: list,
    stextE,
    zeiln1: str,
    zeiln2: str,
    welcheSpalten: list,
    ErlaubteSpalten: str,
):
    import reta

    kette = [
        "reta",
        "".join(("-", i18n.hauptForNeben["zeilen"])),
        zeiln1,
        zeiln2,
        "".join(("-", i18n.hauptForNeben["spalten"])),
        "".join(welcheSpalten),
        "".join(("--", i18n.ausgabeParas["breite"], "=0")),
        "".join(("-", i18n.hauptForNeben["ausgabe"])),
        "".join(
            (
                "--",
                i18n.ausgabeParas["spaltenreihenfolgeundnurdiese"],
                "=",
                ErlaubteSpalten,
            )
        )
        if ErlaubteSpalten is not None
        else "",
        *[
            "--" + i18n.ausgabeParas["keineleereninhalte"]
            if i18n.befehle2["keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"]
            in stextE
            else ""
        ],
    ] + returnOnlyParasAsList(stextE)
    kette += ketten
    if (
        i18n.befehle2["keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"]
        not in stextE
    ):

        if "--" + i18n.ausgabeParas["nocolor"] in stextE:
            cliout(" ".join(kette), True)
        else:
            print(" ".join(kette))
    # x("ENDE", kette)
    reta.Program(
        kette,
    )


def findEqualNennerZaehler(hierBereich, nenner, nennerZaehlerGleich):
    hierBereich2 = BereichToNumbers2(str(hierBereich))
    nenner2 = BereichToNumbers2(str(nenner))
    for nn3 in nenner2:
        for hB3 in hierBereich2:
            if nn3 == hB3 and nn3 not in [0, 1]:
                nennerZaehlerGleich += [str(nn3)]
    return nennerZaehlerGleich


def bruchBereichsManagementAndWbefehl(zahlenBereichC, stext, zahlenAngaben_):
    bruch_GanzZahlReziproke = []
    bruch_GanzZahlReziprokeAbzug = []
    bruch_KeinGanzZahlReziproke = {}
    bruch_KeinGanzZahlReziprokeAbzug = {}
    bruch_KeinGanzZahlReziprok_ = []
    fullBlockIsZahlenbereichAndBruch = True
    rangesBruecheDict = {}
    rangesBruecheDictReverse: dict = {}
    bruch_KeinGanzZahlReziprokeEnDictAbzug = {}
    bruchRanges3Abzug = {}
    valueLenSum = 0
    zahlenAngaben_mehrere = []
    Minusse = {}
    pfaue = {}
    pfaueAbzug = {}

    for g, a in enumerate(stext):
        bruchAndGanzZahlEtwaKorrekterBereich = []
        bruchBereichsAngaben = []
        bruchRanges = []
        abzug = False
        for etwaBruch in a.split(","):
            bruchRange, bruchBereichsAngabe = createRangesForBruchLists(
                bruchSpalt(etwaBruch)
            )
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
            if etwaAllTrue:
                fullBlockIsZahlenbereichAndBruch = (
                    fullBlockIsZahlenbereichAndBruch
                    and all(bruchAndGanzZahlEtwaKorrekterBereich)
                )

        if fullBlockIsZahlenbereichAndBruch:
            for bruchBereichsAngabe, bruchRange in zip(
                bruchBereichsAngaben, bruchRanges
            ):
                if isZeilenAngabe(bruchBereichsAngabe):
                    bruchRange = {b for b in bruchRange if b > 0}
                    EinsInBereichHier1 = BereichToNumbers2(bruchBereichsAngabe)
                    EinsInBereichHier = 1 in EinsInBereichHier1
                    if (
                        bruchBereichsAngabe[:1] == "-"
                        or bruchBereichsAngabe[:2] == i18n.befehle2["v"] + "-"
                    ):
                        minusHier = True
                        if bruchBereichsAngabe[:2] == i18n.befehle2["v"] + "-":
                            pass
                        if bruchBereichsAngabe[:1] == "-":
                            pass
                    else:
                        minusHier = False
                    if 1 in bruchRange:
                        if minusHier:
                            bruch_GanzZahlReziprokeAbzug += [bruchBereichsAngabe]
                        else:
                            bruch_GanzZahlReziproke += [bruchBereichsAngabe]
                    bruchRangeOhne1 = frozenset(set(bruchRange) - {1})
                    neuerBereich = ",".join(
                        {str(zahl) for zahl in EinsInBereichHier1} - {"1"}
                    )
                    Minusse[tuple(bruchRange)] = minusHier
                    if len(bruchRangeOhne1) > 0:
                        if minusHier:
                            try:
                                bruch_KeinGanzZahlReziprokeAbzug[bruchRangeOhne1] += [
                                    bruchBereichsAngabe
                                ]
                                pfaueAbzug[bruchRangeOhne1] += [
                                    bruchBereichsAngabe[:1] == i18n.befehle2["v"]
                                ]
                            except KeyError:
                                bruch_KeinGanzZahlReziprokeAbzug[bruchRangeOhne1] = [
                                    bruchBereichsAngabe
                                ]
                                pfaueAbzug[bruchRangeOhne1] = [
                                    bruchBereichsAngabe[:1] == i18n.befehle2["v"]
                                ]
                        else:
                            try:
                                bruch_KeinGanzZahlReziproke[bruchRangeOhne1] += [
                                    neuerBereich
                                ]
                                pfaue[bruchRangeOhne1] += [
                                    bruchBereichsAngabe[:1] == i18n.befehle2["v"]
                                ]
                            except KeyError:
                                bruch_KeinGanzZahlReziproke[bruchRangeOhne1] = [
                                    neuerBereich
                                ]
                                pfaue[bruchRangeOhne1] = [
                                    bruchBereichsAngabe[:1] == i18n.befehle2["v"]
                                ]
                    if EinsInBereichHier:
                        neueRange = ",".join([str(zahl) for zahl in bruchRange])
                        stext += [neueRange]
                        EsGabzahlenAngaben = True
                        zahlenAngaben_mehrere += [neueRange]
        zahlenAngaben_mehrere += zahlenAngaben_
    try:
        EsGabzahlenAngaben
    except UnboundLocalError:
        EsGabzahlenAngaben = False
    if (i18n.befehle2["v"] in stext) or (i18n.befehle2["vielfache"] in stext):
        if not (
            (i18n.befehle2["e"] in stext)
            or (
                i18n.befehle2["keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"]
                in stext
            )
        ):
            if (
                len(bruch_GanzZahlReziproke) > 0
                or any(
                    [
                        any([1 in BereichToNumbers2(val2) for val2 in val])
                        for val in bruch_KeinGanzZahlReziproke.values()
                    ]
                )
                or EsGabzahlenAngaben
            ):

                print(i18nRP.out3Saetze)
        bdNeu = set()
        for bDazu in bruch_GanzZahlReziproke:
            for bDazu in BereichToNumbers2(bDazu):
                i = 1
                rechnung = i * bDazu
                while rechnung < retaProgram.tables.hoechsteZeile[1024]:
                    bdNeu |= {rechnung}
                    i += 1
                    rechnung = i * bDazu
        for bDazu in bruch_GanzZahlReziprokeAbzug:
            if bDazu[:1] == i18n.befehle2["v"]:
                bDazu = bDazu[1:]
            if bDazu[:1] == "-":
                bDazu = bDazu[1:]
            for bDazu in BereichToNumbers2(bDazu):
                i = 1
                rechnung = i * bDazu
                while rechnung < retaProgram.tables.hoechsteZeile[1024]:
                    try:
                        bdNeu -= {rechnung}
                        i += 1
                        rechnung = i * bDazu
                    except:
                        pass
        bruch_GanzZahlReziproke = ",".join((str(b) for b in bdNeu))
        bruchRanges3 = {}
        bruch_KeinGanzZahlReziprokeEnDict = {}
        for k, (brZahlen, no1brueche) in enumerate(bruch_KeinGanzZahlReziproke.items()):

            for no1bruch in no1brueche:
                if len(no1bruch) > 0 and no1bruch[0] == i18n.befehle2["v"]:
                    no1bruch = no1bruch[1:]
                if len(no1bruch) > 0 and no1bruch[0] == "-":
                    no1bruch = no1bruch[1:]
                    abzug = True
                else:
                    abzug = False
                no1brueche = BereichToNumbers2(no1bruch)
                for no1bruch in no1brueche:
                    i = 1
                    rechnung2 = no1bruch * i
                    while rechnung2 in gebrochenErlaubteZahlen:
                        if rechnung2 not in bruch_KeinGanzZahlReziprokeEnDict.values():
                            if abzug:
                                try:
                                    bruch_KeinGanzZahlReziprokeEnDictAbzug[k] += [
                                        rechnung2
                                    ]
                                except KeyError:
                                    bruch_KeinGanzZahlReziprokeEnDictAbzug[k] = [
                                        rechnung2
                                    ]
                            else:
                                try:
                                    bruch_KeinGanzZahlReziprokeEnDict[k] += [rechnung2]
                                except KeyError:
                                    bruch_KeinGanzZahlReziprokeEnDict[k] = [rechnung2]
                        i += 1
                        rechnung2 = no1bruch * i
            for br in brZahlen:
                i = 1
                rechnung = br * i
                while rechnung in gebrochenErlaubteZahlen:
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

        for keyRanges, valueRanges in bruchRanges3.items():
            for (
                keyBrueche,
                valueBrueche,
            ) in bruch_KeinGanzZahlReziprokeEnDict.items():
                for eineRange in valueRanges:
                    for einBruch in valueBrueche:
                        if keyRanges == keyBrueche:
                            try:
                                strBruch = str(einBruch)
                                if strBruch not in rangesBruecheDict[eineRange]:
                                    rangesBruecheDict[eineRange] += [strBruch]
                            except KeyError:
                                rangesBruecheDict[eineRange] = [str(einBruch)]
        if len(bruchRanges3Abzug) > 0:
            rangesBruecheDict2 = deepcopy(rangesBruecheDict)
            for AbzugNenners, AbzugZaehlers in zip(
                bruchRanges3Abzug.values(),
                bruch_KeinGanzZahlReziprokeEnDictAbzug.values(),
            ):
                for aNenner, aZaehler in zip(AbzugNenners, AbzugZaehlers):
                    for key, value in zip(
                        bruchRanges3.values(), rangesBruecheDict.values()
                    ):
                        try:
                            if key.index(int(aNenner)) == value.index(str(aZaehler)):
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
                                rangesBruecheDict2[aNenner] = value
                        except ValueError:
                            pass
            rangesBruecheDict = rangesBruecheDict2
            bruchRanges3Abzug = {}
            bruch_KeinGanzZahlReziprokeEnDictAbzug = {}
    else:
        if (
            len(bruch_GanzZahlReziproke) == 0
            or type(bruch_GanzZahlReziproke) is not str
        ):
            bruch_GanzZahlReziproke = ",".join(
                (
                    ",".join(bruch_GanzZahlReziproke),
                    ",".join(bruch_GanzZahlReziprokeAbzug),
                )
            )
        elif type(bruch_GanzZahlReziproke) is str:
            bruch_GanzZahlReziproke += "," + (
                ",".join(
                    (
                        ",".join(bruch_GanzZahlReziproke),
                        ",".join(bruch_GanzZahlReziprokeAbzug),
                    )
                )
            )

        bruchDict = {}
        for ((bruchRange, bruch_KeinGanzZahlReziprok_), pfauList) in zip(
            bruch_KeinGanzZahlReziproke.items(), pfaue.values()
        ):
            bruch_KeinGanzZahlReziprok_2 = set()
            for pfau, nenners in zip(pfauList, bruch_KeinGanzZahlReziprok_):
                if pfau:
                    nenners = BereichToNumbers2(nenners)
                    for nenner in nenners:
                        i = 1
                        rechnung = i * int(nenner)
                        while rechnung in gebrochenErlaubteZahlen:
                            bruch_KeinGanzZahlReziprok_2 |= {str(rechnung)}
                            i += 1
                            rechnung = i * int(nenner)
                else:
                    bruch_KeinGanzZahlReziprok_2 |= set(nenners.split(","))
            bruch_KeinGanzZahlReziprok_ = ",".join(bruch_KeinGanzZahlReziprok_2)
            for rangePunkt in bruchRange:
                try:
                    bruchDict[rangePunkt] |= {bruch_KeinGanzZahlReziprok_}
                except KeyError:
                    bruchDict[rangePunkt] = {bruch_KeinGanzZahlReziprok_}

                for (
                    bruchRangeA,
                    bruch_KeinGanzZahlReziprok_A,
                ) in bruch_KeinGanzZahlReziprokeAbzug.items():
                    bruch_KeinGanzZahlReziprok_A = ",".join(
                        bruch_KeinGanzZahlReziprok_A
                    )
                    for rangePunktA in bruchRangeA:
                        if rangePunkt == rangePunktA:
                            try:
                                bruchDict[rangePunkt] |= {
                                    bruch_KeinGanzZahlReziprok_,
                                    bruch_KeinGanzZahlReziprok_A,
                                }
                            except KeyError:
                                bruchDict[rangePunkt] = {
                                    bruch_KeinGanzZahlReziprok_,
                                    bruch_KeinGanzZahlReziprok_A,
                                }
        rangesBruecheDict = bruchDict
    rangesBruecheDict2 = {}
    bereicheVorherBestimmtSet = set()
    for key, values in rangesBruecheDict.items():
        bereichVorherBestimmt = [BereichToNumbers2(value) for value in values]
        bereicheVorherBestimmtSet2 = set()
        for b in bereichVorherBestimmt:
            bereicheVorherBestimmtSet2 |= b
        bereicheVorherBestimmtSet |= bereicheVorherBestimmtSet2
        rangesBruecheDict2[key] = list(bereicheVorherBestimmtSet2)
    valueLenSum += len(bereicheVorherBestimmtSet)
    dictLen = len(rangesBruecheDict)
    if dictLen != 0:
        avg = valueLenSum / dictLen
        if avg < 1:
            rangesBruecheDictReverse = invert_dict_B(rangesBruecheDict2)
            rangesBruecheDict = {}
    zahlenAngaben_mehrere = list(set(zahlenAngaben_mehrere))
    if len(zahlenAngaben_mehrere) > 0:
        zahlenAngaben_mehrereStr = ",".join(zahlenAngaben_mehrere)
        zahlenReiheKeineWteiler = copy(zahlenAngaben_mehrereStr)
        if i18n.befehle2["w"] in stext or i18n.befehle2["teiler"] in stext:
            zahlenAngaben_mehrereStr = ",".join(
                [
                    str(zahl)
                    for zahl in BereichToNumbers2(
                        ",".join(
                            [
                                str(z).split("+")[0]
                                for z in zahlenReiheKeineWteiler.split(",")
                            ]
                        ),
                        False,
                        0,
                    )
                ]
            )
            zahlenBereichC: str = ",".join(teiler(zahlenAngaben_mehrereStr)[0])
            if len(zahlenReiheKeineWteiler) > 1:
                zahlenBereichC += "," + zahlenReiheKeineWteiler
        else:
            zahlenBereichC = zahlenAngaben_mehrereStr

    try:
        zahlenReiheKeineWteiler
    except (UnboundLocalError, NameError):
        zahlenReiheKeineWteiler = ""

    return (
        bruch_GanzZahlReziproke,
        zahlenBereichC,
        zahlenReiheKeineWteiler,
        fullBlockIsZahlenbereichAndBruch,
        rangesBruecheDict,
        len(zahlenAngaben_) > 0 or EsGabzahlenAngaben,
        rangesBruecheDictReverse,
        stext,
    )


def PromptVonGrosserAusgabeSonderBefehlAusgaben(loggingSwitch, Txt, cmd_gave_output):
    if len(Txt.liste) > 0 and Txt.liste[0] in (i18n.befehle2["shell"]):
        cmd_gave_output = True
        try:
            process = subprocess.Popen([*Txt.liste[1:]])
            process.wait()
        except:
            pass
    if len(Txt.liste) > 0 and i18n.befehle2["python"] == Txt.liste[0]:
        cmd_gave_output = True
        try:
            process = subprocess.Popen(["python3", "-c", " ".join(Txt.liste[1:])])
            process.wait()
        except:
            pass
    if len(Txt.liste) > 0 and i18n.befehle2["math"] == Txt.liste[0]:
        cmd_gave_output = True
        for st in "".join(Txt.liste[1:2]).split(","):
            try:
                process = subprocess.Popen(["python3", "-c", "print(" + st + ")"])
                process.wait()
            except:
                pass
    if i18n.befehle2["loggen"] in Txt.liste:
        cmd_gave_output = True
        loggingSwitch = True
    elif i18n.befehle2["nichtloggen"] in Txt.liste:
        cmd_gave_output = True
        loggingSwitch = False
    return loggingSwitch, cmd_gave_output


def verdreheWoReTaBefehl(text1: str, text2: str, text3: str, PromptMode: PromptModus):

    # x("VERDREHT ?", [text1, text2, text3, PromptMode])
    if text2[:4] == "reta" and text1[:4] != "reta" and len(text3) > 0:
        # x("VERDREHT", PromptMode)
        return text2, text1, text2.split()
    # x("NICHT VERDREHT", PromptMode)
    return text1, text2, text3


def promptVorbereitungGrosseAusgabe(
    platzhalter, promptMode, promptMode2, promptModeLast, text, textDazu0
):
    Txt = TXT(text)
    Txt.platzhalter = platzhalter
    ketten = []
    # AusgabeSelektiv = 5
    ifKurzKurz = False
    if len(Txt.liste) > 0:
        textDazu: list = []
        s_2: list

        ifKurzKurz, Txt.liste = stextFromKleinKleinKleinBefehl(
            promptMode2, Txt.liste, textDazu
        )
    if Txt.liste is not None:
        nstextnum: list = []
        for astext in Txt.liste:
            if astext.isdecimal():
                nstextnum += [int(astext)]
        if len(nstextnum) > 0:
            maxNum = max(nstextnum)
        else:
            maxNum = 1024
    zahlenBereichNeu: map = {}
    zahlenBereichNeu1: map = {}
    for swort in Txt.liste:
        try:
            zahlenBereichNeu1[bool(isZeilenAngabe(swort))] += [swort]
        except KeyError:
            zahlenBereichNeu1[bool(isZeilenAngabe(swort))] = [swort]
    for key, value in zahlenBereichNeu1.items():
        zahlenBereichNeu[key] = ",".join(value)

    zahlenBereichMatch = tuple(zahlenBereichNeu.keys())
    if (
        promptMode2 == PromptModus.AusgabeSelektiv
        and promptModeLast == PromptModus.normal
    ):
        Txt.liste = textDazu0 + Txt.liste
    if (
        promptMode == PromptModus.normal
        and len(Txt.platzhalter) > 1
        and Txt.platzhalter[:4] == "reta"
        and any(zahlenBereichMatch)
        and zahlenBereichMatch.count(True) == 1
    ):
        zeilenn = False
        woerterToDel = []
        for i, wort in enumerate(Txt.liste):
            if len(wort) > 1 and wort[0] == "-" and wort[1] != "-":
                zeilenn = False
            if zeilenn is True or wort == zahlenBereichNeu[True]:
                woerterToDel += [i]
            if wort == "-" + i18n.hauptForNeben["zeilen"]:
                zeilenn = True
                woerterToDel += [i]
        stextDict = {i: swort for i, swort in enumerate(Txt.liste)}
        for todel in woerterToDel:
            del stextDict[todel]
        Txt.liste = list(stextDict.values())

        if len({i18n.befehle2["w"], i18n.befehle2["teiler"]} & Txt.menge) > 0:
            BereichMenge = BereichToNumbers2(zahlenBereichNeu[True], False, 0)
            BereichMengeNeu = teiler(",".join([str(b) for b in BereichMenge]))[1]
            zahlenBereichNeu[True] = ""
            for a in BereichMengeNeu:
                zahlenBereichNeu[True] += str(a) + ","
            zahlenBereichNeu[True] = zahlenBereichNeu[True][:-1]

            try:
                tx = Txt.liste
                tx.remove(i18n.befehle2["w"])
                Txt.liste = x
            except:
                pass
            try:
                tx = Txt.liste
                tx.remove(i18n.befehle2["teiler"])
                Txt.liste = x
            except:
                pass

        if len({i18n.befehle2["v"], i18n.befehle2["vielfache"]} & Txt.menge) == 0:
            Txt.liste += [
                "".join(("-", i18n.hauptForNeben["zeilen"])),
                "".join(("--", i18n.zeilenParas["vorhervonausschnitt"], "="))
                + zahlenBereichNeu[True],
            ]

        else:
            Txt.liste += [
                "".join(("-", i18n.hauptForNeben["zeilen"])),
                "".join(("--", i18n.zeilenParas["vielfachevonzahlen"], "="))
                + zahlenBereichNeu[True],
            ]
            try:
                tx = Txt.liste
                tx.remove(i18n.befehle2["v"])
                Txt.liste = x
            except:
                pass
            try:
                tx = Txt.liste
                tx.remove(i18n.befehle2["vielfache"])
                Txt.liste = x
            except:
                pass
    IsPureOnlyReTaCmd: bool = len(Txt.liste) > 0 and Txt.liste[0] == "reta"
    brueche = []
    zahlenAngaben_ = []
    zahlenAngabenC = ""
    if len(Txt.menge & befehleBeenden) > 0:
        Txt.liste = [tuple(befehleBeenden)[0]]
        exit()
    replacements = i18nRP.replacements
    if len(Txt.liste) > 0 and Txt.liste[0] not in [
        "reta",
        "shell",
        "python",
        "abstand",
    ]:
        listeNeu: list = []
        for token in Txt.liste:
            try:
                listeNeu += [replacements[token]]
            except KeyError:
                listeNeu += [token]
        Txt.liste = listeNeu
    if Txt.liste[:1] != ["reta"]:
        Txt.liste = list(Txt.menge)
    return (
        IsPureOnlyReTaCmd,
        brueche,
        zahlenAngabenC,
        ketten,
        maxNum,
        Txt.liste,
        zahlenAngaben_,
        ifKurzKurz,
    )


def PromptAllesVorGroesserSchleife():
    global promptMode2, textDazu0, befehleBeenden
    if "-" + i18nRP.retaPromptParameter["vi"] not in sys.argv:
        retaPromptHilfe()
    if "-" + i18nRP.retaPromptParameter["log"] in sys.argv:
        loggingSwitch = True
    else:
        loggingSwitch = False
    if ("-" + i18nRP.retaPromptParameter["h"] in sys.argv) or (
        "-" + i18nRP.retaPromptParameter["help"] in sys.argv
    ):
        print(i18nRP.helptext)
        exit()
    if "-" + i18nRP.retaPromptParameter["debug"] in sys.argv:
        retaProgram.propInfoLog = True
        if "-" + i18nRP.retaPromptParameter["e"] not in sys.argv:
            alxp(i18nRP.infoDebugAktiv)

    if "-" + i18nRP.retaPromptParameter["befehl"] in sys.argv:
        von = sys.argv.index("-" + i18nRP.retaPromptParameter["befehl"]) + 1
        nurEinBefehl = sys.argv[von:]
    else:
        nurEinBefehl = []
    if "-" + i18nRP.retaPromptParameter["e"] in sys.argv:
        alxp(i18nRP.infoDebugAktiv)
        immerEbefehlJa = True
    else:
        immerEbefehlJa = False
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
    promptMode = PromptModus.normal
    promptMode2 = PromptModus.normal
    promptDavorDict = defaultdict(lambda: ">")
    promptDavorDict[PromptModus.speichern] = i18nRP.wspeichernWort
    promptDavorDict[PromptModus.loeschenSelect] = i18nRP.wloeschenWort
    textDazu0 = []
    return (
        befehleBeenden,
        loggingSwitch,
        promptDavorDict,
        promptMode,
        startpunkt1,
        nurEinBefehl,
        immerEbefehlJa,
    )


def PromptLoescheVorSpeicherungBefehle(platzhalter, promptMode, text):
    global promptMode2, textDazu0
    TxtZuloeschen = TXT(text)
    TxtLoeschbereiche = TXT(platzhalter)
    loeschbares1 = {i + 1: a for i, a in enumerate(TxtLoeschbereiche.liste)}
    loeschbares2 = {a: i + 1 for i, a in enumerate(TxtLoeschbereiche.liste)}
    flag = False
    if isZeilenAngabe(TxtZuloeschen.text):
        if (
            TxtZuloeschen.text not in loeschbares2.keys()
            or not TxtZuloeschen.text.isdecimal()
        ):
            zuloeschen2 = BereichToNumbers2(TxtZuloeschen.text, False, 0)
            for todel in zuloeschen2:
                try:
                    del loeschbares1[todel]
                except:
                    pass
            TxtLoeschbereiche.platzhalter = " ".join(loeschbares1.values())
        else:
            flag = True
    else:
        flag = True
    if flag:
        zuloeschen2 = set()
        for wort in TxtZuloeschen.liste:
            try:
                TxtLoeschbereiche.liste = list(
                    filter(lambda a: a != wort, TxtLoeschbereiche.liste)
                )
            except:
                pass
        TxtZuloeschen = TXT(",".join(zuloeschen2))
        TxtLoeschbereiche.platzhalter = " ".join(TxtLoeschbereiche.liste)

    promptMode = PromptModus.normal
    return TxtLoeschbereiche.platzhalter, promptMode, TxtZuloeschen.text


def promptSpeicherungB(nochAusageben, promptMode, Txt):
    if promptMode == PromptModus.speicherungAusgaben:
        Txt.text = Txt.platzhalter
    elif promptMode == PromptModus.speicherungAusgabenMitZusatz:
        Txt.text = Txt.platzhalter + " " + nochAusageben
    return Txt


def promptSpeicherungA(ketten, promptMode, Txt):
    if promptMode == PromptModus.speichern:
        ketten, Txt = speichern(ketten, Txt.platzhalter, Txt.text)
    return ketten, Txt


def promptInput(
    loggingSwitch,
    promptDavorDict,
    promptMode,
    startpunkt1,
    Txt,
    nurEinBefehl,
    immerEbefehlJa,
):
    if len(nurEinBefehl) == 0:
        session = newSession(loggingSwitch)
        try:
            Txt.befehlDavor = Txt.text

            Txt.text = session.prompt(
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
                vi_mode=True
                if "-" + i18nRP.retaPromptParameter["vi"] in sys.argv
                else False,
                style=Style.from_dict({"bla": "#0000ff bg:#ffff00"})
                if loggingSwitch
                else Style.from_dict({"bla": "#0000ff bg:#ff0000"}),
                # placeholder="reta",
                placeholder=Txt.platzhalter,
            )
            if immerEbefehlJa and Txt.text[:4] != "reta":
                Txt.e = [
                    i18n.befehle2[
                        "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
                    ]
                ]
            else:
                Txt.e = []
        except KeyboardInterrupt:
            sys.exit()

    else:
        Txt.text = " ".join(nurEinBefehl)
        Txt.e = []
        Txt.befehlDavor = ""
    return Txt


if __name__ == "__main__":
    PromptScope()


def start(sprachenWahl1="deutsch"):
    global sprachenWahl
    alxp(sys.argv)
    PromptScope()
    return sprachenWahl
