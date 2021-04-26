#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from copy import deepcopy
from enum import Enum
from typing import Iterable, Union

from center import (alxp, cliout, getTextWrapThings, infoLog, output,
                    primzahlvielfachesgalaxie, re, x)
from lib4tables import isPrimMultiple, moonNumber

shellRowsAmount, h_de, dic, fill = getTextWrapThings()


class Wraptype(Enum):
    pyphen = 1
    pyhyphen = 2
    nohyphen = 3


wrappingType: Wraptype = Wraptype.pyhyphen
# wrappingType: Wraptype = Wraptype.nohyphen
# wrappingType: Wraptype = Wraptype.pyphen


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def splitMoreIfNotSmall(textList: list, lenToBe: int) -> tuple:
    newList: list = []
    neededToBeDoneAtAll = False
    lenToBe -= 0
    for k, text in enumerate(textList):
        if len(text) > lenToBe:
            neededToBeDoneAtAll = True
    if neededToBeDoneAtAll:
        for k, text in enumerate(textList):
            if len(text) > lenToBe:
                newList += list(chunks(text, lenToBe))
            else:
                newList += [text]
    if neededToBeDoneAtAll:
        return tuple(newList)
    else:
        return tuple(textList)


def alxwrap(text: str, len_: int):
    global wrappingType
    """ Ich könnte hier beschleunigen, indem ich funktionszeiger verwende,
    anstelle jedes mal hier ein if durch gehen zu lassen
    """
    try:
        fill
    except NameError:
        return (text,)
    if "Brython" in sys.version.split():
        return (text,)
    try:
        return (
            dic.wrap(text, len_)
            if wrappingType == Wraptype.pypheni and len_ != 0
            else (
                splitMoreIfNotSmall(
                    fill(text, width=len_, use_hyphenator=h_de).split("\n"), len_
                )
                if wrappingType == Wraptype.pyhyphen and len_ != 0
                else (text,)
            )
        )
    except:
        return (
            dic.wrap(text, len_)
            if wrappingType == Wraptype.pyhyphen and len_ != 0
            else (
                splitMoreIfNotSmall(
                    fill(text, width=len_, use_hyphenator=h_de).split("\n"), len_
                )
                if wrappingType == Wraptype.pyphen and len_ != 0
                else (text,)
            )
        )


class Prepare:
    def __init__(self, tables, originalLinesRange, shellRowsAmount):
        self.tables = tables
        self.originalLinesRange = originalLinesRange
        self.shellRowsAmount = shellRowsAmount
        self.zaehlungen = [
            0,
            {},
            {},
            {},
            {},
        ]  # Strukturangaben zur Zeile wegen Mondzahlen und Sonnenzahlen
        self.religionNumbers = 0
        self.gezaehlt = False

    def setZaehlungen(
        self, num: int
    ):  # mehrere Zählungen finden festlegen zum später auslesen
        """Eine Zahl wird untersucht und die Variable self.zaehlungen wegen dieser Ergänzt
        self.zaehlungen bekommt informationen über mondzahlen und sonnenzahlen
        i ist eine zu Untersuchende Zahl kleinergeich num
        self.zaehlungen[4][i] bekommt die mondtypen, d.h. (Basis, Exponent) immer
        self.zaehlungen[1][zaehlung] welche zählung fängt mit welcher Zahl an
        self.zaehlungen[2][i] ist welcher Zählung es ist für eine beliebige Zahl: 1 ist 1-4, 2 ist 5-9, 3 ist 10-16
        self.zaehlungen[3][i] ist auch welche Zählung es ist für eine beliebige Zahl: 1 ist 1-4, 2 ist 5-9, 3 ist 10-16
        self.zaehlungen[0] ist bis zu welcher Zahl diese Untersuchung beim letzten Mal durchgeführt wurde
        self.zaehlungen  # [bis zu welcher zahl, {zaehlung:zahl},{zahl:zaehlung},{jede zahl,zugehoerigeZaehlung}]

        @type num: int
        @param num: zu untersuchende Zahl
        @rtype: kein Typ
        @return: nichts
        """
        num = self.originalLinesRange[-1]
        if self.gezaehlt:
            return
        else:
            self.gezaehlt = True
        wasMoon: bool = True
        if self.zaehlungen[0] == 0:
            isMoon = True
        else:
            isMoon = moonNumber(self.zaehlungen[0])[0] != []

        for i in range(int(self.zaehlungen[0]) + 1, num + 1):
            wasMoon = isMoon
            moonType = moonNumber(i)
            isMoon = moonType[0] != []
            if wasMoon and not isMoon:
                isMoon = False
                self.zaehlungen[1][len(self.zaehlungen[1]) + 1] = i
                self.zaehlungen[2][i] = len(self.zaehlungen[2]) + 1
            self.zaehlungen[3][i] = len(self.zaehlungen[2])
            self.zaehlungen[4][i] = moonType

    @property
    def breitenn(self):
        return self.breiten

    @breitenn.setter
    def breitenn(self, value: bool):
        self.breiten = value

    @property
    def nummeriere(self):
        """ # Nummerierung der Zeilen, z.B. Religion 1,2,3 """
        return self.nummerierung

    @nummeriere.setter
    def nummeriere(self, value):
        self.nummerierung = value

    @property
    def textWidth(self):
        return self.textwidth

    @textWidth.setter
    def textWidth(self, value):
        self.textwidth = value

    def wrapping(self, text: str, length: int) -> list:
        """Hier wird der Zeilenumbruch umgesetzt

        @type text: str
        @param text: Der Text dessen Zeilen umbgebrochen werden sollen
        @type lenght: int
        @param lenght: ab welcher Zeilenlänge umgebrochen werden soll
        @rtype: list[str]
        @return: Liste aus umgebrochenen Teilstrings
        """
        if len(text) > length and length != 0:
            isItNone = alxwrap(text, length)
        else:
            isItNone = None
        return isItNone

    def setWidth(self, rowToDisplay: int, combiRows1: int = 0) -> int:
        if self.shellRowsAmount == 0:
            return 0
        combiRows = combiRows1 if combiRows1 != 0 else len(self.rowsAsNumbers)
        if len(self.rowsAsNumbers) - combiRows < len(self.breiten):
            breiten: list = self.breiten[len(self.rowsAsNumbers) - combiRows :]
        else:
            breiten: list = []
        # delta = -1 if not self.nummerierung and combiRows1 != 0 else -1
        delta = -1
        if rowToDisplay + delta < len(breiten) and rowToDisplay + delta >= 0:
            certaintextwidth = breiten[rowToDisplay + delta]
        else:
            certaintextwidth = self.textwidth
        return certaintextwidth

    def parametersCmdWithSomeBereich(
        self, MehrereBereiche: str, symbol: str, neg: str
    ) -> set:
        """Erstellen des Befehls: Bereich

        @type MehrereBereiche: str
        @param MehrereBereiche: der Bereich von bis
        @type symbol: str
        @param symbol: welche Art Bereich soll es werden, symbol typisiert den Bereich
        @type neg: string
        @param neg: Vorzeichen, wenn es darum geht dass diese Zeilen nicht angezeigt werden sollen
        @rtype: set
        @return: Alle Zeilen die dann ausgegeben werden sollen
        """
        results = set()
        for EinBereich in MehrereBereiche.split(","):
            if (
                (neg == "" and len(EinBereich) > 0 and EinBereich[0].isdecimal())
                or (neg == EinBereich[: len(neg)] and len(neg) > 0)
            ) and len(EinBereich) > 0:
                EinBereich = (
                    EinBereich[len(neg) :]
                    if neg == EinBereich[: len(neg)]
                    else EinBereich
                )
                if EinBereich.isdecimal():
                    EinBereich = EinBereich + "-" + EinBereich
                BereichCouple = EinBereich.split("-")
                if (
                    len(BereichCouple) == 2
                    and BereichCouple[0].isdecimal()
                    and BereichCouple[0] != "0"
                    and BereichCouple[1].isdecimal()
                    and BereichCouple[1] != "0"
                ):
                    results.add(
                        "".join(
                            [BereichCouple[0]]
                            + ["-"]
                            + [symbol]
                            + ["-"]
                            + [BereichCouple[1]]
                        )
                    )

        return results

    def deleteDoublesInSets(self, set1: set, set2: set) -> Iterable[Union[set, set]]:
        """Wenn etwas in 2 Mengen doppelt vorkommt wird es gelöscht
        @rtype: tuple[set,set]
        @return: Beide Mengen werden ausgegeben
        """
        intersection = set1 & set2
        return set1 - intersection, set2 - intersection

    def fromUntil(self, a) -> tuple:
        """2 Zahlen sollen ein ordentlicher Zahlenbereich sein, sonst werden sie es

        @rtype: tuple[int,int]
        @return: Eine Bereichsangabe
        """
        if a[0].isdecimal():
            a[0] = int(a[0])
            if len(a) == 2 and a[1].isdecimal():
                a[1] = int(a[1])
            elif len(a) == 1:
                swap = a[0]
                a[0] = 1
                a += [swap]
                a[0] = 1
            else:
                return (1, 1)
            return tuple(a)
        else:
            return (1, 1)

    def zeileWhichZaehlung(self, zeile: int) -> int:
        return self.zaehlungen[3][zeile]

    # ich wollte je pro extra num, nun nicht mehr nur sondern modular ein mal alles und dann pro nummer in 2 funktionen geteilt
    def FilterOriginalLines(self, numRange: set, paramLines: set) -> set:
        """Hier werden die Befehle der Angabe welche Zeilen angezeigt werden in konkrete Zeilen umgewandelt.

        @type results: Menge
        @param set: Bereiche von Zeilen einer Art: Anzeigen, ja, nein, von woanders, etc.
        @rtype: set
        @return: Mehrere Bereichsbezeichnugen
        """

        def diffset(wether, a: set, b: set) -> set:
            if wether:
                # result = a.difference(b)
                result = a - b
                if result is None:
                    return set()
                else:
                    return result
            return a

        numRange -= {0}

        def cutset(wether, a: set, b: set) -> set:
            if wether:
                # result = a.intersection(b)
                result = a & b
                if result is None:
                    return set()
                else:
                    return result
            return a

        for condition in paramLines:
            if "all" == condition:
                return set(self.originalLinesRange)

        numRangeYesZ = set()
        if_a_AtAll = False
        for condition in paramLines:
            if "-a-" in condition:
                if_a_AtAll = True
                a = self.fromUntil(condition.split("-a-"))
                for n in numRange.copy():
                    if a[0] <= n and a[1] >= n:
                        # numRange.remove(n)
                        numRangeYesZ.add(n)

        numRange = cutset(if_a_AtAll, numRange, numRangeYesZ)
        numRangeYesZ = set()
        ifZeitAtAll = False

        for condition in paramLines:
            if "=" == condition:
                ifZeitAtAll = True
                numRangeYesZ.add(10)
            elif "<" == condition:
                ifZeitAtAll = True
                for n in numRange:
                    if n < 10:
                        numRangeYesZ.add(n)
            elif ">" == condition:
                ifZeitAtAll = True
                for n in numRange:
                    if n > 10:
                        numRangeYesZ.add(n)

        numRange = cutset(ifZeitAtAll, numRange, numRangeYesZ)

        numRangeYesZ = set()
        ifZaehlungenAtAll = False
        for condition in paramLines:
            if "-n-" in condition:
                ifZaehlungenAtAll = True
                a = self.fromUntil(condition.split("-n-"))
                for n in numRange.copy():
                    if a[0] <= n and a[1] >= n:
                        # numRange.remove(n)
                        numRangeYesZ.add(n)
        if ifZaehlungenAtAll or True:
            self.setZaehlungen(self.originalLinesRange[-1])
        if ifZaehlungenAtAll:
            # self.setZaehlungen(self.originalLinesRange[-1])
            numRangeYesZ2 = set()
            for n in numRange:  # nur die nummern, die noch infrage kommen
                for z in numRangeYesZ:
                    if self.zaehlungen[3][n] == int(z):  # 1-4:1,5-9:2 == jetzt ?
                        numRangeYesZ2.add(n)
                        # numRange.remove(n)
            numRange = cutset(ifZaehlungenAtAll, numRange, numRangeYesZ2)
            # set().add
            # exit()
        ifTypAtAll = False
        numRangeYesZ = set()

        def moonsun(MoonNotSun: bool, numRangeYesZ: set):
            if not ifZaehlungenAtAll:
                self.setZaehlungen(self.originalLinesRange[-1])
            for n in numRange:
                if (self.zaehlungen[4][n][0] != []) == MoonNotSun:
                    numRangeYesZ.add(n)
            return numRangeYesZ

        for condition in paramLines:
            if "mond" in condition:
                numRangeYesZ, ifTypAtAll = moonsun(True, numRangeYesZ), True
            elif "schwarzesonne" in condition:
                ifTypAtAll = True
                for n in numRange:
                    if n % 3 == 0:
                        numRangeYesZ.add(n)
            elif "sonne" in condition:
                numRangeYesZ, ifTypAtAll = moonsun(False, numRangeYesZ), True
            elif "planet" in condition:
                ifTypAtAll = True
                for n in numRange:
                    if n % 2 == 0:
                        numRangeYesZ.add(n)

        x("_x3_", numRange)
        numRange = cutset(ifTypAtAll, numRange, numRangeYesZ)
        x("_x2_", numRange)

        primMultiples: list = []
        ifPrimAtAll = False
        for condition in paramLines:
            if (
                len(condition) > 1
                and condition[-1] == "p"
                and condition[:-1].isdecimal()
            ):
                ifPrimAtAll = True
                primMultiples += [int(condition[:-1])]

        numRangeYesZ = set()
        for n in numRange:
            if isPrimMultiple(n, primMultiples):
                numRangeYesZ.add(n)
        numRange = cutset(ifPrimAtAll, numRange, numRangeYesZ)

        x("_x1_", numRange)

        toPowerIt: list = []
        ifPowerAtall: bool = False
        for condition in paramLines:
            if (
                len(condition) > 1
                and condition[-1] == "^"
                and condition[:-1].isdecimal()
            ):
                ifPowerAtall = True
                toPowerIt += [int(condition[:-1])]
        if ifPowerAtall:
            numRangeYesZ = set()
            x("_y1_", (toPowerIt, numRange))
            lastEl = list(numRange)
            lastEl.sort()
            lastEl = lastEl[-1]
            for base in toPowerIt:
                for n in range(lastEl):
                    onePower = pow(base, n)
                    numRangeMax = max(numRange)
                    x("_y2_", (onePower, numRangeMax))
                    if onePower <= numRangeMax:
                        numRangeYesZ |= {onePower}
                    else:
                        break
            numRange = cutset(ifPowerAtall, numRange, numRangeYesZ)
        x("_x4_", numRange)

        numRangeYesZ = set()

        ifMultiplesFromAnyAtAll = False
        anyMultiples = []
        for condition in paramLines:
            if (
                len(condition) > 1
                and condition[-1] == "v"
                and condition[:-1].isdecimal()
            ):
                ifMultiplesFromAnyAtAll = True
                anyMultiples += [int(condition[:-1])]

        if ifMultiplesFromAnyAtAll:
            numRangeYesZ = set()
            for n in numRange:
                for divisor in anyMultiples:
                    if n % divisor == 0:
                        numRangeYesZ.add(n)
            numRange = cutset(ifMultiplesFromAnyAtAll, numRange, numRangeYesZ)

        ifNachtraeglichAtAll = False
        for condition in paramLines:
            if "-z-" in condition:
                if not ifNachtraeglichAtAll:
                    numRange2: list = list(numRange)
                    numRange2.sort()
                    ifNachtraeglichAtAll = True
                a = self.fromUntil(condition.split("-z-"))
                for i, n in enumerate(numRange2.copy()):
                    if a[0] - 1 > i or a[1] - 1 < i:
                        numRange2.remove(n)
        if ifNachtraeglichAtAll:
            numRange = set(numRange2)
        return numRange

    def prepare4out(
        self,
        paramLines: set,
        paramLinesNot: set,
        contentTable: list,
        rowsAsNumbers: set,
        combiRows: int = 0,
    ) -> tuple:
        """Aus einer Tabelle wird eine gemacht, bei der der Zeilenumbruch durchgeführt wird.
        Dabei werden alle Spalten und Zeilen entfernt die nicht ausgegeben werden sollen.

        @type paramLines: set
        @param paramLines: welche Linien ja, andere fallen weg
        @type paramLinesNot: set
        @param paramLinesNot: welche Linien nein, werden abgezogen von ja
        @type contentTable: list
        @param contentTable: die Tabelle die verändert werden soll
        @type rowsAsNumberss: set
        @param rowsAsNumberss: anzuzeigende Spalten
        @rtype: tuple[set,set,int,range,list]
        @return: Zeilen die ausgegeben werden sollen, neue Tabelle, Nummer der letzten Zeile , \
            range aus zu zeigenden Spalten 1-n nicht alle , welche neuen Spalten welche alten waren und umgekehrt
        return finallyDisplayLines, newerTable, numlen, rowsRange, old2Rows
        """
        newerTable: list = []
        if len(contentTable) > 0:
            headingsAmount = len(contentTable[0])
            rowsRange = range(headingsAmount)
        else:
            headingsAmount = 0
            rowsRange = range(0)
        finallyDisplayLines: set = self.FilterOriginalLines(
            set(self.originalLinesRange), paramLines
        )
        if not len(paramLinesNot) == 0:
            finallyDisplayLines2 = self.FilterOriginalLines(
                deepcopy(finallyDisplayLines), paramLinesNot
            )
            hasAnythingCanged = (
                set(self.originalLinesRange) - finallyDisplayLines2 - {0}
            )
            if len(hasAnythingCanged) > 0:
                finallyDisplayLines -= finallyDisplayLines2
        finallyDisplayLines.add(0)
        finallyDisplayLines3: list = list(finallyDisplayLines)
        finallyDisplayLines3.sort()
        finallyDisplayLines = set(finallyDisplayLines3)
        #    maxPartLineLen = 0
        numlen = len(str(finallyDisplayLines3[-1]))
        old2Rows: tuple = ({}, {})
        reliNumbersBool = False if self.religionNumbers != [] else True
        for u, line in enumerate(contentTable):
            if u in finallyDisplayLines:
                if reliNumbersBool:
                    self.religionNumbers += [int(u)]
                new2Lines: list = []
                rowToDisplay = 0
                h = 0
                for t, cell in enumerate(line):
                    if t in rowsAsNumbers:
                        if u == 0 and combiRows == 0:
                            x("_x_", rowToDisplay)
                            x("_y_", self.tables.generatedSpaltenParameter)
                            if rowToDisplay in self.tables.generatedSpaltenParameter:
                                x(
                                    "FehlerY",
                                    self.tables.generatedSpaltenParameter[rowToDisplay],
                                )
                                if self.tables.SpaltenVanillaAmount > t:
                                    x("FehlerX", rowToDisplay)
                                    x("FehlerX", t)
                                    x("FehlerX", self.tables.dataDict[0][t])
                                # raise ValueError
                            try:
                                if (
                                    rowToDisplay
                                    not in self.tables.generatedSpaltenParameter
                                ):
                                    pass
                                    self.tables.generatedSpaltenParameter[
                                        rowToDisplay
                                    ] = self.tables.dataDict[0][t]
                            except KeyError:
                                x("rrr", t)
                                alxp("__")
                                x("wwi", cell)
                                x("iii", self.tables.dataDict[0])

                        rowToDisplay += 1
                        newLines = [[]] * headingsAmount
                        certaintextwidth = self.setWidth(rowToDisplay, combiRows)
                        into = self.cellWork(cell, newLines, certaintextwidth, t)
                        if into != [""] or True:
                            new2Lines += [into]
                        if u == 0:
                            old2Rows[0][t] = h
                            old2Rows[1][h] = t
                        h += 1

                if new2Lines != []:
                    newerTable += [new2Lines]

        x("idiot", self.tables.generatedSpaltenParameter)
        return finallyDisplayLines, newerTable, numlen, rowsRange, old2Rows

    def cellWork(self, cell: str, newLines, certaintextwidth: int, t: int) -> list:
        """aus String mach Liste aus Strings mit korrektem Zeilenumbruch

        @type cell: str
        @param cell: Text, für in Teilstrings, korrekter Zeilenumbruch!
        @type newLines: list[str]
        @param newLines: voran gegangene Versuche dieser Liste aus Strings
        @type certaintextwidth: int
        @param certaintextwidth: an dieser Stelle Zeilenumbruch
        @type t: int
        @param t: welcher Versuch einer Liste aus strings soll von dieser Funktion zurück gegeben werden
        @rtype: list[str]
        @return: Liste aus Strings mit korrektem Zeilenumbruch
        """
        # certaintextwidth -= 1
        cell = cell.strip()
        isItNone = self.wrapping(cell, certaintextwidth)
        cell2: tuple = tuple()
        rest: str = cell
        if certaintextwidth == 0:
            return [cell]

        while isItNone not in [None, ()]:
            cell2 += isItNone
            isItNone = self.wrapping(cell2[-1], certaintextwidth)
            rest = cell2[-1]
            cell2 = cell2[:-1]
            if len(rest) > certaintextwidth and isItNone is None:
                cell2 += (rest[0:certaintextwidth],)
                isItNone = (rest[certaintextwidth:],)
        else:
            cell2 += (rest[0:certaintextwidth],)
            for k, cellInCells in enumerate(cell2):
                if k < len(newLines):
                    newLines[k] += [cellInCells]
                else:
                    pass
        return newLines[t]
