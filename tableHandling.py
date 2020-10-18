#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import io
import os
import sys
import bbcode
from copy import copy, deepcopy
from enum import Enum
from typing import Iterable, Union
from center import (alxp, cliout, getTextWrapThings, infoLog, output,
                    primzahlvielfachesuniversum, re, x)
from lib4tables import moonNumber, primFak, divisorGenerator, primCreativity, primRepeat, primMultiple, isPrimMultiple, couldBePrimeNumberPrimzahlkreuz, math, OutputSyntax, htmlSyntax, csvSyntax, markdownSyntax, bbCodeSyntax

shellRowsAmount, h_de, dic, fill = getTextWrapThings()

originalLinesRange = range(1028)  # Maximale Zeilenanzahl



class Tables:
    def getRowAmountofAnyPart(self):
        return {
            "numerierung": 1 if self.nummeriere else 0,
            "main prepare relitable orignal | combi & concat-prim drin": self.getPrepare.rowsAsNumbers,
            "prim (concat)": self.puniverseprims,
            "combi": (self.getCombis.rowsOfcombi, self.getCombis.ChosenKombiLines),
            "len(AllCombiRows)": self.getCombis.sumOfAllCombiRowsAmount,
            "row of prim multi generated": self.primUniverseRow,
        }

    @property
    def outType(self) -> OutputSyntax:
        return self.getOut.outType

    @outType.setter
    def outType(self, value: OutputSyntax):
        self.getOut.outType = value

    @property
    def generRows(self):
        return self.__generRows__

    @generRows.setter
    def generRows(self, value: set):
        self.__generRows__ = value

    @property
    def ifPrimMultis(self):
        return self.getPrepare.ifprimmultis

    @ifPrimMultis.setter
    def ifPrimMultis(self, value: bool):
        self.getPrepare.ifprimmultis = value

    @property
    def primUniversePrimsSet(self):
        return self.puniverseprims

    @property
    def breitenn(self):
        return self.getOut.breiten

    @breitenn.setter
    def breitenn(self, value: list):
        global shellRowsAmount
        for i, v in enumerate(copy(value)):
            value[i] = (
                v
                if shellRowsAmount > v + 9 or shellRowsAmount == 0
                else shellRowsAmount - 9
            )
        self.getPrepare.breiten = value
        self.getOut.breiten = value

    @property
    def nummeriere(self):
        """ # Nummerierung der Zeilen, z.B. Religion 1,2,3 """
        return self.getOut.nummerierung

    @nummeriere.setter
    def nummeriere(self, value: bool):
        self.getOut.nummerierung = value
        self.getPrepare.nummerierung = value

    @property
    def textHeight(self):
        return self.getOut.textHeight

    @textHeight.setter
    def textHeight(self, value: int):
        self.getOut.textHeight = value

    @property
    def textWidth(self):
        return self.textwidth

    @textWidth.setter
    def textWidth(self, value: int):
        self.getPrepare.textWidth = value
        self.getOut.textWidth = value
        self.textwidth = value

    def __init__(self):
        global originalLinesRange
        self.rowNumDisplay2rowNumOrig = {}
        self.generatedSpaltenParameter = {}
        self.getPrepare = self.Prepare(self, originalLinesRange, shellRowsAmount)
        self.getCombis = self.Combi(self)
        self.getConcat = self.Concat(self)
        self.getOut = self.Output(self)
        self.getMainTable = self.Maintable(self)
        self.textHeight = 0
        self.textWidth = 21
        self.nummeriere = True
        self.spaltegGestirn = False
        self.breitenn: list = []
        self.puniverseprims: set = set()  # welche Spalten von "primenumbers.csv"
        self.getOut.primUniversePrimsSet = self.puniverseprims
        self.getConcat.primUniversePrimsSet = self.puniverseprims
        self.religionNumbers: list = []
        self.getOut.religionNumbers = self.religionNumbers
        self.getPrepare.religionNumbers = self.religionNumbers
        self.getCombis.religionNumbers = self.religionNumbers
        self.getPrepare.ifprimmultis = False
        self.getCombis.rowsOfcombi = set()
        # self.getPrepare.rowsAsNumbers = set()
        self.getConcat.concatRowsAmount = 0
        self.__generRows__: set = set()

    class Output:
        def __init__(self, tables):
            self.tables = tables
            self.__oneTable = False
            self.__color = True
            self.__outType: OutputSyntax = OutputSyntax()

        @property
        def outType(self) -> OutputSyntax:
            return self.__outType

        @outType.setter
        def outType(self, value: OutputSyntax):
            self.__outType = value

        @property
        def color(self):
            return self.__color

        @color.setter
        def color(self, value: bool):
            self.__color = value

        @property
        def oneTable(self):
            return self.__oneTable

        @oneTable.setter
        def oneTable(self, value: bool):
            self.__oneTable = value

        @property
        def primUniversePrimsSet(self):
            return self.puniverseprims

        @primUniversePrimsSet.setter
        def primUniversePrimsSet(self, value: set):
            self.puniverseprims = value

        @property
        def breitenn(self):
            return self.breiten

        @breitenn.setter
        def breitenn(self, value: list):
            self.breiten = value

        @property
        def nummeriere(self):
            """ # Nummerierung der Zeilen, z.B. Religion 1,2,3 """
            return self.nummerierung

        @nummeriere.setter
        def nummeriere(self, value):
            self.nummerierung = value

        @property
        def textHeight(self):
            return self.textheight

        @textHeight.setter
        def textHeight(self, value):
            self.textheight = value

        @property
        def textWidth(self):
            return self.textwidth

        @textWidth.setter
        def textWidth(self, value):
            global shellRowsAmount
            self.textwidth = (
                value
                if shellRowsAmount > value + 9 or shellRowsAmount == 0
                else shellRowsAmount - 9
            )

        def onlyThatColumns(self, table, onlyThatColumns):
            if len(onlyThatColumns) > 0:
                newTable = []
                for row in table:
                    newCol = []
                    for i in onlyThatColumns:
                        try:
                            newCol += [deepcopy(row[i - 1])]
                        except IndexError:
                            pass
                    newTable += [newCol]
                if len(newTable) > 0:
                    return newTable
                else:
                    return table
            else:
                return table

        def cliOut(
            self,
            finallyDisplayLinesSet: set,
            newTable: list,
            numlen: int,
            rowsRange: range,
        ):
            """gibt eine Tabelle aus

            @type finallyDisplayLines: set
            @param finallyDisplayLines: Zeilen die ausgegeben werden sollen
            @type newRows: list
            @param newRows: Tabelle um die es geht
            @type rowsRange: set
            @param rowsRange: range(spaltenanzahl)
            @rtype:
            @return: nichts
            """
            global output, shellRowsAmount

            def findMaxCellTextLen(
                finallyDisplayLines: set, newTable: list, rowsRange: range
            ):
                """Gibt eine Liste mit Integern zurück, bzw. eigentlich ein Dict.
                Die Integer sind die Zellbreite, die an einer Stelle mindestens
                maximal war. Dieses Maximum wird zurück gegeben, als eine Zahl,
                bestimmt durch Überprüfung mehrerer Felder.

                @type finallyDisplayLines: set
                @param finallyDisplayLines: Zeilen die ausgegeben werden sollen
                @type newTable: list
                @param newTable: Tabelle um die es geht
                @type rowsRange: set
                @param rowsRange: range(spaltenanzahl)
                @rtype: dict[int,int]
                @return: Zellbreiten
                """
                maxCellTextLen: dict = {}
                # for k in finallyDisplayLines: # n Linien einer Zelle, d.h. 1 EL = n Zellen
                for k, (f, r) in enumerate(
                    zip(newTable, finallyDisplayLines)
                ):  # n Linien einer Zelle, d.h. 1 EL = n Zellen
                    for iterWholeLine, m in enumerate(
                        rowsRange
                    ):  # eine Bildhschirm-Zeile immer
                        # for i in self.rowsAsNumbers: # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                        for i, c in enumerate(
                            newTable[k]
                        ):  # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                            if not i in maxCellTextLen:
                                try:
                                    maxCellTextLen[i] = len(newTable[k][i][m])
                                except:
                                    pass
                            else:
                                try:
                                    textLen = len(newTable[k][i][m])
                                    if textLen > int(maxCellTextLen[i]):
                                        maxCellTextLen[i] = textLen
                                except:
                                    pass
                return maxCellTextLen

            def determineRowWidth(i, maxCellTextLen):
                if i < len(self.breiten):
                    # if i + (1 if self.nummerierung else 0) <= len(self.breiten):
                    certaintextwidth = self.breiten[i]
                else:
                    certaintextwidth = self.textwidth
                if certaintextwidth > maxCellTextLen[i]:
                    i_textwidth = maxCellTextLen[i]
                else:
                    i_textwidth = certaintextwidth
                return i_textwidth

            maxCellTextLen = findMaxCellTextLen(
                finallyDisplayLinesSet, newTable, rowsRange
            )
            self.finallyDisplayLines: list = list(finallyDisplayLinesSet)
            self.finallyDisplayLines.sort()
            # ColumnsRowsAmount, shellRowsAmount1 = (
            ##    os.popen("stty size", "r").read().split()
            # )  # Wie viele Zeilen und Spalten hat die Shell ?
            shellRowsAmount -= (
                len(str(self.finallyDisplayLines[-1]))
                if len(self.finallyDisplayLines) > 0 and shellRowsAmount != 0
                else 0
            )
            x("NIXX", self.tables.dataDict)
            self.finallyDisplayLines[0] = ""
            lastSubCellIndex = -1
            lastlastSubCellIndex = -2
            headingfinished = False
            if type(self.__outType) is csvSyntax:
                strio = io.StringIO()
                writer = csv.writer(
                    strio,
                    quoting=csv.QUOTE_NONE,
                    delimiter=";",
                    quotechar="",
                )
            while (
                len(newTable) > 0
                and lastSubCellIndex < len(newTable[0]) - 1
                and lastSubCellIndex > lastlastSubCellIndex
            ):
                cliout(self.__outType.beginTable)
                lastlastSubCellIndex = lastSubCellIndex
                for (
                    BigCellLineNumber,
                    (TablesLineOfBigCells, filteredLineNumbersofOrignal),
                ) in enumerate(
                    zip(newTable, self.finallyDisplayLines)
                ):  # n Linien einer Zelle, d.h. 1 EL = n Zellen
                    for iterWholeLine, OneWholeScreenLine_AllSubCells in enumerate(
                        rowsRange
                    ):  # eine Bildhschirm-Zeile immer
                        # x("abcde", self.tables.getPrepare.zaehlungen)
                        line = (
                            (
                                (
                                    self.__outType.generateCell(
                                        -2,
                                        self.tables.generatedSpaltenParameter,
                                        self.tables.getPrepare.zeileWhichZaehlung(
                                            int(filteredLineNumbersofOrignal)
                                        ),
                                        zeile=BigCellLineNumber,
                                    )
                                    + (
                                        "█"
                                        if type(self.__outType) in [OutputSyntax]
                                        else str(
                                            self.tables.getPrepare.zeileWhichZaehlung(
                                                int(filteredLineNumbersofOrignal)
                                            )
                                        )
                                    )
                                    + self.__outType.endCell
                                    if self.tables.getPrepare.zeileWhichZaehlung(
                                        int(filteredLineNumbersofOrignal)
                                    )
                                    % 2
                                    == 0
                                    else self.__outType.generateCell(
                                        -2,
                                        self.tables.generatedSpaltenParameter,
                                        self.tables.getPrepare.zeileWhichZaehlung(
                                            int(filteredLineNumbersofOrignal)
                                        ),
                                        zeile=BigCellLineNumber,
                                    )
                                    + (
                                        " "
                                        if type(self.__outType) in [OutputSyntax]
                                        else str(
                                            self.tables.getPrepare.zeileWhichZaehlung(
                                                int(filteredLineNumbersofOrignal)
                                            )
                                        )
                                    )
                                    + self.__outType.endCell
                                )
                                if str(filteredLineNumbersofOrignal).isdecimal
                                and filteredLineNumbersofOrignal != ""
                                and int(filteredLineNumbersofOrignal) > 0
                                else self.__outType.generateCell(
                                    -2,
                                    self.tables.generatedSpaltenParameter,
                                    zeile=BigCellLineNumber,
                                )
                                + " "
                                + self.__outType.endCell
                            )
                            if self.nummerierung
                            else ""
                        )
                        linePlus = (
                            ""
                            if not self.nummerierung
                            else self.__outType.generateCell(
                                -1,
                                self.tables.generatedSpaltenParameter,
                                zeile=BigCellLineNumber,
                            )
                            + (
                                "".rjust(numlen + 1)
                                if iterWholeLine != 0
                                else (str(filteredLineNumbersofOrignal) + " ").rjust(
                                    numlen + 1
                                )
                            )
                            + self.__outType.endCell
                        )
                        if type(self.__outType) is csvSyntax:
                            line = [line, linePlus]
                        else:
                            line += linePlus
                        rowsEmpty = 0
                        sumWidths = 0
                        lastSubCellIndex = 0
                        emptyEntries: int = 0
                        entriesHere: int = 0
                        for subCellIndexRightLeft, subCellContentLeftRight in enumerate(
                            newTable[BigCellLineNumber]
                        ):  # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                            if (
                                subCellIndexRightLeft > lastlastSubCellIndex
                                or self.__oneTable
                            ):
                                subCellWidth = determineRowWidth(
                                    subCellIndexRightLeft, maxCellTextLen
                                )
                                sumWidths += subCellWidth + 1
                                if sumWidths < shellRowsAmount or self.__oneTable:
                                    lastSubCellIndex = subCellIndexRightLeft
                                    try:
                                        entry = newTable[BigCellLineNumber][
                                            subCellIndexRightLeft
                                        ][OneWholeScreenLine_AllSubCells]
                                        entriesHere += 1
                                        if len(entry.strip()) == 0:
                                            emptyEntries += 1
                                        if (
                                            self.color
                                            and type(self.__outType) is OutputSyntax
                                        ):
                                            coloredSubCell = self.colorize(
                                                entry.replace("\n", "").ljust(
                                                    subCellWidth
                                                ),
                                                filteredLineNumbersofOrignal,
                                            )
                                        elif type(self.__outType) is csvSyntax:
                                            coloredSubCell = newTable[
                                                BigCellLineNumber
                                            ][subCellIndexRightLeft][
                                                OneWholeScreenLine_AllSubCells
                                            ].replace(
                                                "\n", ""
                                            )
                                        else:
                                            coloredSubCell = (
                                                self.__outType.generateCell(
                                                    subCellIndexRightLeft,
                                                    self.tables.generatedSpaltenParameter,
                                                    zeile=BigCellLineNumber,
                                                )
                                                + (
                                                    entry.replace("\n", "").ljust(
                                                        subCellWidth
                                                    )
                                                )
                                                + self.__outType.endCell
                                            )
                                        if type(self.__outType) is csvSyntax:
                                            line += [coloredSubCell]
                                        else:
                                            line += (
                                                coloredSubCell + " "
                                            )  # neben-Einander
                                    except:
                                        rowsEmpty += 1
                                        if (
                                            self.color
                                            and type(self.__outType) is OutputSyntax
                                        ):
                                            coloredSubCell = self.colorize(
                                                "".ljust(subCellWidth),
                                                filteredLineNumbersofOrignal,
                                                True,
                                            )
                                        else:
                                            coloredSubCell = (
                                                self.__outType.generateCell(
                                                    subCellIndexRightLeft,
                                                    self.tables.generatedSpaltenParameter,
                                                    zeile=BigCellLineNumber,
                                                )
                                                + "".ljust(subCellWidth)
                                                + self.__outType.endCell
                                            )
                                        if type(self.__outType) is csvSyntax:
                                            line += [coloredSubCell]
                                        else:
                                            line += (
                                                coloredSubCell + " "
                                            )  # neben-Einander
                                else:
                                    rowsEmpty += 1
                            else:
                                rowsEmpty += 1

                        if rowsEmpty != len(self.rowsAsNumbers) and (
                            iterWholeLine < self.textheight or self.textheight == 0
                        ):  # and m < actualPartLineLen:
                            if type(self.__outType) is markdownSyntax:
                                line += self.__outType.generateCell(
                                    subCellIndexRightLeft,
                                    self.tables.generatedSpaltenParameter,
                                    zeile=BigCellLineNumber,
                                )

                                if BigCellLineNumber > 0 and not headingfinished:
                                    headingfinished = True
                                if BigCellLineNumber == 0 and not headingfinished:
                                    addionalLine = ""
                                    for l in line:
                                        if l != self.__outType.generateCell(
                                            subCellIndexRightLeft,
                                            self.tables.generatedSpaltenParameter,
                                            zeile=BigCellLineNumber,
                                        ):
                                            addionalLine += "-"
                                        else:
                                            addionalLine += self.__outType.generateCell(
                                                subCellIndexRightLeft,
                                                self.tables.generatedSpaltenParameter,
                                                zeile=BigCellLineNumber,
                                            )

                                    line += "\n" + addionalLine
                            if emptyEntries != entriesHere:
                                if type(self.__outType) is csvSyntax:
                                    writer.writerow(line)
                                else:
                                    if (
                                        type(filteredLineNumbersofOrignal) is str
                                        and filteredLineNumbersofOrignal == ""
                                    ):
                                        filteredLineNumbersofOrignal = 0
                                    # if (
                                    #    not str(
                                    #        filteredLineNumbersofOrignal
                                    #    ).isdecimal()
                                    #    or True
                                    # ):
                                    #    sys.stderr.write(
                                    #        " ALXALX "
                                    #        + str(filteredLineNumbersofOrignal)
                                    #        + " "
                                    #        + line
                                    #        + "\n"
                                    #    )
                                    cliout(
                                        self.__outType.coloredBeginCol(
                                            filteredLineNumbersofOrignal
                                        )
                                        + line
                                        + self.__outType.endZeile
                                    )
                cliout(self.__outType.endTable)
                if self.__oneTable:
                    break
                if type(self.__outType) is csvSyntax:
                    cliout(strio.getvalue())

        def colorize(self, text, num: int, rest=False) -> str:

            """Die Ausagabe der Tabelle wird coloriert

            @type text: str
            @param text: der zu colorierende Text
            @type num: int
            @param num: die Zeilennummer, die coloriert werden soll
            @type rest: bool
            @param rest: andere Colorierung
            @rtype: str
            @return: der colorierte Text
            """
            # \033[0;34mblaues Huhn\033[0m.
            num = int(num) if str(num).isdecimal() else 0
            if rest:
                if num == 0:
                    return "\033[41m" + "\033[30m" + "\033[1m" + text + "\033[0m"
                elif num % 2 == 0:
                    return "\033[47m" + "\033[30m" + text + "\033[0m" + "\033[0m"
                else:
                    return "\033[40m" + "\033[37m" + text + "\033[0m" + "\033[0m"
            elif moonNumber(num)[1] != []:
                # 00;33
                if num % 2 == 0:
                    return "\033[106m" + "\033[30m" + text + "\033[0m" + "\033[0m"
                else:
                    return "\033[46m" + "\033[30m" + text + "\033[0m" + "\033[0m"
            elif len(primFak(num)) == 1:
                if num % 2 == 0:
                    return "\033[103m" + "\033[30m" + "\033[1m" + text + "\033[0m"
                else:
                    return "\033[43m" + "\033[30m" + text + "\033[0m" + "\033[0m"
            elif num % 2 == 0:
                if num == 0:
                    return "\033[41m" + "\033[30m" + "\033[1m" + text + "\033[0m"
                else:
                    return "\033[47m" + "\033[30m" + text + "\033[0m" + "\033[0m"
            else:
                return "\033[100m" + "\033[37m" + text + "\033[0m" + "\033[0m"

    from lib4tables_prepare import Prepare

    class Combi:
        def __init__(self, tables):
            self.ChosenKombiLines: dict = {}
            self.sumOfAllCombiRowsAmount = 0
            self.tables = tables
            self.parameterName = "kombination"
            """alle  Schritte für kombi:
            1. lesen: KombiTable und relation, was von kombitable zu haupt gehört
                      und matrix mit zellen sind zahlen der kombinationen
                      d.h. 3 Sachen sind das Ergebnis
            2. prepare: die Zeilen, die infrage kommen für Kombi, d.h.:
                                    key = haupttabellenzeilennummer
                                    value = kombitabellenzeilennummer
            3. Zeilenumbruch machen, wie es bei der Haupt+Anzeige-Tabelle auch gemacht wurde
               prepare4out
            4. Vorbereiten des Joinens beider Tabellen direkt hier ( in völlig falsche Klasse ) rein programmiert
               (Müsste ich unbedingt mal refactoren!)
            5. joinen
            6. noch mal nur das ausgeben lassen, das nur ausgegeben werden soll
            7. letztendliche Ausagebe von allem!!
            """

        def prepareTableJoin(self, ChosenKombiLines, newTable_kombi_1):
            KombiTables = []
            for key, value in ChosenKombiLines.items():
                """Zeilennummern der kombi, die hinten dran kommen sollen
                     an die Haupt- und Anzeigetabelle
                     key = haupttabellenzeilennummer
                g    value = kombitabellenzeilennummer
                """
                tables = {}
                for kombiLineNumber in value:
                    """
                    alle kombitabellenzeilennummern hier durchiterieren
                    pro haupttabellenzeilennummer (diese umschließende Schleife)

                    into = eine neue Tabelle mit nur erlaubten Zeilen, gemacht
                    aus der Tabelle von der kombi.csv, die schon mit Zeilenumbrüchen
                    usw. vorbereitet wurde.
                    """

                    into = self.tables.tableReducedInLinesByTypeSet(
                        newTable_kombi_1, {kombiLineNumber}
                    )
                    """into = self.tabless.tableReducedInLinesByTypeSet(
                        animalsProfessionsTable, {kombiLineNumber}
                    )"""
                    if len(into) > 0:
                        if key in tables:
                            """Ergibt Matrix:
                            KombigesamttabelleMitZeilenumbruchVorbereitung[kombi.csv Zeilenummer][nur die relevanten Spaltens ihre erste Spalte ]
                            d.h. das ist aus kombi.csv die erste Spalte mit den Kombinationszahlen
                            die hier zugeordnet zu den kombi.csv zeilennummern gespeichert werden,
                            d.h. nicht den haupt+ausgabezeilen
                            """
                            tables[key] += [into[0]]
                        else:
                            tables[key] = [into[0]]
                    # cliOut({0,kombiLineNumber}, oneTable, 2, rowsRange_kombi_1)
                    """ Liste aus Tabellen: eine Untertabelle = was in Haupttabellenzeilennummer rein soll aus der Kombitabelle
                    Zusammen ist das die Matrix der Kombis, die an die Haupt+Anzeige Tabelle deneben ran soll
                """
                KombiTables += [tables]
            return KombiTables

        def tableJoin(
            self,
            mainTable: list,
            manySubTables: list,
            maintable2subtable_Relation: list,
            old2newRows: list,
            rowsOfcombi,
        ) -> list:
            """Verbindet kombi tabelle mit haupttabelle
            @type mainTable: list
            @param mainTable: Haupttabelle, die angezeigt werden soll
            @type manySubTables: list
            @param manySubTables: Die Teiltabellen, von denen Teile pro Spalte in die Haupttabelle als Spalten und Zeilen rein sollen
            @type maintable2subtable_Relation: list
            @param maintable2subtable_Relation: Wie die Kombitabelle in die Haupttabelle rein kommen soll, d.h. hier sind die Verknüpfungspunkte beider Seiten enthalten
            @type old2newRows: list
            @param old2newRows: list
            @type rowsOfcombi: list
            @param rowsOfcombi: Welche Spalten der Kombitabelle in die Haupttabelle rein sollen
            @rtype table2: list[list]
            @return table2: Die resultierende gesamte später anzuzeigende Haupttabelle

            """
            rowsOfcombi = list(rowsOfcombi)
            rowsOfcombi.sort()
            table2 = mainTable
            """ Hätte ich mich gleich für SQL entschieden, oder hätte ich Pandas gewählt, dann hätte ich diesen Komplizierten Mist nicht programmieren müssen!
            """
            # if self.tables.textWidth == 0 and type(self.tables.getOut.outType) in [
            if type(self.tables.getOut.outType) in [
                htmlSyntax,
                bbCodeSyntax,
            ]:
                oneLinePerLine = True
            else:
                oneLinePerLine = False
            for colNum, (reliNum, col) in enumerate(
                zip(self.religionNumbers, mainTable)
            ):
                """geht die Zeilen der anzuzeigenden Haupttabelle durch
                1. Zeilenummer, 2. richtige Nummer der Religion (z.B: 1-10), 3. anzuzeigende Haupttabellenzeile
                """
                for subTable in manySubTables:
                    """Liste aus Tabellen: eine Untertabelle = was in Haupttabellenzeilennummer rein soll aus der Kombitabelle
                    Zusammen ist das die Matrix der Kombis, die an die Haupt+Anzeige Tabelle deneben ran soll

                    hier werden also alle Orginal-Haupt+Anzeige Zeilen durchgegangen
                    """
                    if reliNum in subTable:
                        """Wenn z.B. Religion 2 als Spalte 2 auch als Spalte 2 drin ist als Zelle der kombis die als Zelle in die Haupt+Anzeige Tabelle rein soll
                        d.h. hier die Frage ob z.B. 2==2    viel mehr ist das nicht"""
                        for row, bigCell in enumerate(mainTable[colNum]):
                            """HauptTabellenzeilen werden durchIteriert"""
                            if old2newRows[1][row] in maintable2subtable_Relation[0]:
                                """Wenn Haupttabellenzeile der Kombitabellenzeile entspricht"""
                                subRowNum = maintable2subtable_Relation[0][
                                    old2newRows[1][row]
                                ]
                                for subTableCell in subTable[reliNum]:
                                    """Die zu wählenden Religionen z.B. 1-10 durchiterieren
                                    und dessen zugehörige subTableZellen die als Zellen in die Haupt+Anzeige Tabelle rein sollen
                                    genomen
                                    """
                                    if rowsOfcombi.index(subRowNum + 1) < len(
                                        subTableCell
                                    ) and subTableCell != [[""]]:
                                        """Hier kommt jetzt endlich die Zelle in die Zelle rein:
                                        D.h. die Sache aus der Kombitabelle kommt in die Zelle der Haupt+Anzeige-Tabelle rein.
                                        Dabei ist die Zelle in die die Zelle rein kommt, widerum selbst eine kleine Tabelle, eigentlich.
                                        """
                                        if oneLinePerLine:

                                            if (
                                                len(table2[colNum][row]) == 1
                                                and table2[colNum][row][0] == ""
                                            ):
                                                table2[colNum][row] = deepcopy(
                                                    subTableCell[
                                                        rowsOfcombi.index(subRowNum + 1)
                                                    ]
                                                )
                                            else:
                                                table2[colNum][row][
                                                    -1
                                                ] += " | " + deepcopy(
                                                    subTableCell[
                                                        rowsOfcombi.index(subRowNum + 1)
                                                    ][0]
                                                )
                                        else:
                                            if (
                                                len(table2[colNum][row]) == 1
                                                and table2[colNum][row][0] == ""
                                            ):
                                                table2[colNum][row] = deepcopy(
                                                    subTableCell[
                                                        rowsOfcombi.index(subRowNum + 1)
                                                    ]
                                                )
                                            else:
                                                table2[colNum][row] += deepcopy(
                                                    subTableCell[
                                                        rowsOfcombi.index(subRowNum + 1)
                                                    ]
                                                )
            return table2

        def prepare_kombi(
            self,
            finallyDisplayLines_kombi_1: set,
            kombiTable: list,
            paramLines: set,
            displayingMainLines: set,
            kombiTable_Kombis: list,
        ) -> dict:
            """Vorbereiten zum Kombinieren von Tabellen, wie bei einem SQL-Join
            siehe hier Return-Value, der hiermit erstellt wird.
            Nur darum geht es.

            @type finallyDisplayLines: set
            @param finallyDisplayLines: set
            @type kombiTable: list
            @param kombiTable: Tabelle um die es geht, die zur Haupttabelle dazu kommt
            @type paramLines: set
            @param paramLines: Befehle die aus den Shell Paramentern konstruiert wurden
            @type displayingMainLines: set
            @param displayingMainLines: Zeilen die angezeigt werden sollen
            @type kombiTable_Kombis: list
            @param kombiTable_Kombis: wird anscheinend hier gar nicht gebraucht
            @rtype: dict[set[int]]
            @return: ZeilenNummern die miteinander als Join kombiniert werden sollen zwischen Haupttabelle und weiterer
                key = haupttabellenzeilennummer
                value = kombitabellenzeilennummer
            """
            # kombitypes = {"displaying": False, "or": False, "and": False}
            # self.ChosenKombiLines: dict = {}
            for condition in paramLines:
                if "ka" == condition:
                    # kombitypes["displaying"] = True
                    for MainLineNum in displayingMainLines:
                        for kombiLineNumber, kombiLine in enumerate(kombiTable_Kombis):
                            """kombiLineNumber ist die csv Zeilennummer in der Kombitabelle
                            kombiLine ist aus der ersten Spalte die jeweilige Liste an Zahlenkombinationen pro Zeile"""
                            for kombiNumber in kombiLine:
                                """kombiNumber ist demzufolge eine so eine Zahl
                                von n*m Zahlen
                                if: wenn eine dieser Zahlen zu denen gehört, die am Ende angezeigt werden sollen und
                                wenn diese Zahl eine ist, die genau der richtigen Anzeigezeile entspricht"""
                                if (
                                    kombiNumber in displayingMainLines
                                    and kombiNumber == MainLineNum
                                ):
                                    try:
                                        """Zugehörig zur richtigen Anzeigeezeile wird diese Kombizeile ausgewählt
                                        d.h. anzeige in zeile enthält die richtige kombizeile
                                        NUMMERN werden da rein gelistet
                                        key = haupttabellenzeilennummer
                                        value = kombitabellenzeilennummer
                                        """
                                        self.ChosenKombiLines[MainLineNum] |= {
                                            kombiLineNumber + 1
                                        }
                                    except KeyError:
                                        self.ChosenKombiLines[MainLineNum] = {
                                            kombiLineNumber + 1
                                        }
            return self.ChosenKombiLines

        def readKombiCsv(
            self, relitable: list, rowsAsNumbers: set, rowsOfcombi: set
        ) -> tuple:
            """Fügt eine Tabelle neben der self.relitable nicht daneben sondern als join an, wie ein sql-join
            Hier wird aber noch nicht die join Operation durchgeführt
            momentan ist es noch fix auf animalsProfessions.csv

            @type relitable: list
            @param relitable: Haupttabelle self.relitable
            @type rowsAsNumbers: set
            @param rowsAsNumbers: welche Spalten  der Anzeigetabelle sind gewählt
            @type rowsOfcombi: set
            @param rowsOfcombi: welche Spalten der kombi Tabelle dazu kommen sollen
            @rtype: tuple[list,list,list,list]
            @return: neue Tabelle - die der kombi.csv entspricht, haupttabelle self.relitable, \
                Liste mit allen Zeilen der neuen Tabelle aus der ersten Spalte je Liste aus allem darin \
                das mit Komma getrennt wurde , was zu was gehört als Info für den join später
            return kombiTable, self.relitable, kombiTable_Kombis, maintable2subtable_Relation
            """
            global folder
            self.rowsOfcombi = rowsOfcombi
            place = os.path.join(
                os.getcwd(), os.path.dirname(__file__), os.path.basename("./kombi.csv")
            )
            self.sumOfAllCombiRowsAmount += len(self.rowsOfcombi)
            self.relitable = relitable
            headingsAmount = len(self.relitable[0])
            self.maintable2subtable_Relation: tuple = ({}, {})
            if len(self.rowsOfcombi) > 0:
                with open(place, mode="r") as csv_file:
                    self.kombiTable: list = []
                    self.kombiTable_Kombis: list = []
                    for z, col in enumerate(csv.reader(csv_file, delimiter=";")):
                        """jede Zeile in der kombi.csv"""
                        for i, row in enumerate(col):
                            """jede Spalte also dann eigentlich Zelle der kombi.csv"""
                            if (
                                i > 0
                                and col[i].strip() != ""
                                and len(col[0].strip()) != 0
                            ):
                                col[i] += " (" + col[0] + ")"
                        self.kombiTable += [col]
                        self.kombiTable_Kombis_Col: list = []
                        if len(col) > 0 and z > 0:
                            """die Behandlung des Auslesens von Religionsnummern in Kombination
                            in der ersten Spalte der kombi.csv"""
                            for num in col[0].split("|"):
                                """self.kombiTable_Kombis:
                                Liste mit allen Zeilen der neuen Tabelle aus der ersten
                                Spalte je Liste aus allem darin das mit Komma getrennt wurde
                                """
                                if num.isdecimal() or (
                                    num[0] in ["+", "-"] and num[1:].isdecimal()
                                ):
                                    """Nummer ... Liste mit alles Zahlen einer Religionskombination
                                    in eine Zeile pro Religionskombination und nicht bereits hier
                                    mit was eine Religion mit anderen Zahlen kombiniert werden würde,
                                    denn das kommt später und wird genau daraus hier gebaut.
                                    """
                                    self.kombiTable_Kombis_Col += [abs(int(num))]
                                elif num[1:-1].isdecimal() or (
                                    num[1] in ["+", "-"] and num[2:-1].isdecimal()
                                ):
                                    self.kombiTable_Kombis_Col += [abs(int(num[1:-1]))]
                                    # arg[(arg.find("=") + 1) :].split(",")
                                elif (
                                    "/" in num and num[num.find("/") + 1 :].isdecimal()
                                ):
                                    self.kombiTable_Kombis_Col += [
                                        abs(int(num[num.find("/") + 1 :])),
                                        abs(int(num[: num.find("/")])),
                                    ]
                                elif (
                                    "/" in num
                                    and num[num.find("/") + 2 : -1].isdecimal()
                                ):
                                    self.kombiTable_Kombis_Col += [
                                        abs(int(num[num.find("/") + 2 : -1])),
                                        abs(int(num[1 : num.find("/")])),
                                    ]
                                else:
                                    raise BaseException(
                                        "Die kombi.csv ist in der ersten Spalte nicht so wie sie sein soll mit den Zahlen."
                                    )
                            self.kombiTable_Kombis += [self.kombiTable_Kombis_Col]
                    self.relitable, animalsProfessionsCol = Tables.fillBoth(
                        self.relitable, list(self.kombiTable)
                    )
                    lastlen = 0
                    maxlen = 0
                    for i, (animcol, relicol) in enumerate(
                        zip(animalsProfessionsCol, self.relitable)
                    ):
                        """jede Zeile bei der Haupttabellenzeile der Kombitabellenzeile (noch) NICHT richtig entspricht
                        beide sind auf die gleiche richtig Länge vorher verlängert worden.
                        (irgendwie komisch von mir programmiert)
                        """
                        if i == 0:
                            """Zur richtigen Zeile kommt der Leerraum rein,
                            der später aufgefüllt wird durch die wirklichen
                            Inhalte der kombi.csv
                            """
                            lastlen = len(animcol)
                            if lastlen > maxlen:
                                maxlen = lastlen
                            for t, ac in enumerate(animcol[1:]):
                                """Spalte hinten dran und nächste usw.
                                entspricht Spalte in Kombitabelle und umgehert
                                genauso, also Äquivalenz!
                                """
                                self.maintable2subtable_Relation[0][
                                    len(self.relitable[0]) + t
                                ] = t
                                self.maintable2subtable_Relation[1][t] = (
                                    len(self.relitable[0]) + t
                                )
                            self.relitable[0] += list(animcol[1:]) + [""] * (
                                maxlen - len(animcol)
                            )
                        else:
                            """Zur richtigen Zeile kommt der Leerraum rein,
                            der später aufgefüllt wird durch die wirklichen
                            Inhalte der kombi.csv
                            """
                            self.relitable[i] += len(animcol[1:]) * [""] + [""] * (
                                maxlen - len(animcol)
                            )
                        if i == 0:
                            for u, heading in enumerate(self.relitable[0]):
                                for a in self.rowsOfcombi:
                                    if (
                                        u >= headingsAmount
                                        and u == headingsAmount + a - 1
                                    ):
                                        rowsAsNumbers.add(u)
                                        """ rowsAsNumbers müsste hier verzeigert sein
                                        Es kommen genau diese Spaltennummern hinzu,
                                        (die überzählig sind) die nicht mehr in der
                                        anzuzeigenden tabelle entahlten sind also
                                        zu hoch wären, weil es die dazu kommenden
                                        Spalten der kombi.csv sind.
                                        """
                                        if (
                                            len(self.tables.generatedSpaltenParameter)
                                            + self.tables.SpaltenVanillaAmount
                                            in self.tables.generatedSpaltenParameter
                                        ):
                                            raise ValueError
                                        x(
                                            "sss",
                                            len(self.tables.generatedSpaltenParameter),
                                        )
                                        into: list = []
                                        for elementParameter in self.tables.dataDict[3][
                                            a
                                        ]:
                                            into += [("kombination", elementParameter)]
                                        # try:
                                        #   self.tables.generatedSpaltenParameter[
                                        #       len(
                                        #           self.tables.generatedSpaltenParameter
                                        #       )
                                        #       + self.tables.SpaltenVanillaAmount
                                        #   ] |= [into]
                                        # except KeyError:
                                        #   self.tables.generatedSpaltenParameter[
                                        #       len(
                                        #           self.tables.generatedSpaltenParameter
                                        #       )
                                        #       + self.tables.SpaltenVanillaAmount
                                        #   ] = [into]
                                        self.tables.generatedSpaltenParameter[
                                            len(self.tables.generatedSpaltenParameter)
                                            + self.tables.SpaltenVanillaAmount
                                        ] = (into,)

            else:
                self.kombiTable = [[]]
                self.kombiTable_Kombis = [[]]
            x("idiot", self.tables.generatedSpaltenParameter)

            return (
                self.kombiTable,
                self.relitable,
                self.kombiTable_Kombis,
                self.maintable2subtable_Relation,
            )
    from lib4tables_concat import Concat

    class Maintable:
        def __init__(self, tables):
            # self.spaltegestirn = False
            self.tables = tables

        def createSpalteGestirn(self, relitable: list, rowsAsNumbers: set):
            """Fügt self.relitable eine Spalte hinzu, ob eine Zahl ein Mond oder eine Sonne ist
            Die Information muss dazu kommt aus moonNumber(i)[1]

            @type relitable: list
            @param relitable: Haupttabelle self.relitable
            @type rowsAsNumbers: set
            @param rowsAsNumbers: welche Spalten der neuen Tabelle nur betroffen sind
            @rtype:
            @return: nichts
            """
            self.relitable = relitable
            if rowsAsNumbers >= {64}:
                if len(self.relitable) > 0:
                    # self.tables.dataDict[0][len(self.relitable[0])] = [(), ()]
                    if (
                        len(self.tables.generatedSpaltenParameter)
                        + self.tables.SpaltenVanillaAmount
                        in self.tables.generatedSpaltenParameter
                    ):
                        raise ValueError
                    self.tables.generatedSpaltenParameter[
                        len(self.tables.generatedSpaltenParameter)
                        + self.tables.SpaltenVanillaAmount
                    ] = self.tables.dataDict[0][64]
                    rowsAsNumbers.add(len(self.relitable[0]))

                # moonNumber
                for i, line in enumerate(self.relitable):
                    if i == 0:
                        line += ["Gestirn"]
                    else:
                        if moonNumber(i)[1] != []:
                            text = "Mond"
                        else:
                            text = "Sonne"
                        if i % 2 == 0:
                            line += [text + ", Planet"]
                        else:
                            line += [text]

    def tableReducedInLinesByTypeSet(self, table: list, linesAllowed: set):
        """nur Zeilen aus dem set aus der Tabelle verwenden als Ausgabe der Tabelle

        @type table: list[list]
        @param table: Tabelle
        @type table: set[int]
        @param table: erlaubte Zeilen
        @rtype: list[list]
        @return: neue Tabelle mit nur den Zeilen aus linesAllowed
        """
        newTable: list = []
        for i, line in enumerate(table):
            if i in linesAllowed:
                newTable += [line]
        return newTable

