#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import os
from copy import copy, deepcopy

from center import (alxp, cliout, getTextWrapThings, infoLog, output,
                    primzahlvielfachesgalaxie, re, x)
from lib4tables import (OutputSyntax, bbCodeSyntax,
                        couldBePrimeNumberPrimzahlkreuz, csvSyntax,
                        divisorGenerator, htmlSyntax, isPrimMultiple,
                        markdownSyntax, math, moonNumber, primCreativity,
                        primFak, primMultiple, primRepeat)


class Concat:
    def __init__(self, tables):
        self.tables = tables

    @property
    def primUniversePrimsSet(self):
        return self.puniverseprims

    @primUniversePrimsSet.setter
    def primUniversePrimsSet(self, value: set):
        self.puniverseprims = value

    def concatLovePolygon(self, relitable: list, rowsAsNumbers: set) -> tuple:
        self.relitable = relitable
        if rowsAsNumbers >= {8}:
            rowsAsNumbers |= {len(self.relitable[0])}
            for i, cols in enumerate(deepcopy(self.relitable)):
                if self.relitable[i][8].strip() != "":
                    self.relitable[i] += [
                        self.relitable[i][8]
                        + " der eigenen Strukturgröße ("
                        + self.relitable[i][4]
                        + ") auf dich bei gleichförmigen Polygonen"
                    ]
                else:
                    self.relitable[i] += [""]
            if (
                len(self.tables.generatedSpaltenParameter)
                + self.tables.SpaltenVanillaAmount
                in self.tables.generatedSpaltenParameter
            ):
                raise ValueError
            self.tables.generatedSpaltenParameter[
                len(self.tables.generatedSpaltenParameter)
                + self.tables.SpaltenVanillaAmount
            ] = self.tables.dataDict[0][8]
            x("idiot", self.tables.generatedSpaltenParameter)
        return self.relitable, rowsAsNumbers

    def concatPrimCreativityType(self, relitable: list, rowsAsNumbers: set) -> tuple:
        self.relitable = relitable
        if rowsAsNumbers >= {64}:
            rowsAsNumbers |= {len(self.relitable[0])}
            for i, cols in enumerate(deepcopy(self.relitable)):
                primCreativityType = primCreativity(i)
                self.relitable[i] += [
                    "Evolutions-Züchtungs-Kreativität"
                    if i == 0
                    else (
                        "0. Primzahl 1"
                        if primCreativityType == 0
                        else (
                            "1. Primzahl und Sonnenzahl"
                            if primCreativityType == 1
                            else (
                                "2. Sonnenzahl, aber keine Primzahl"
                                if primCreativityType == 2
                                else "3. Mondzahl"
                            )
                        )
                    )
                ]

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
            x("WIE", self.tables.dataDict[0][64])

            x("idiot", self.tables.generatedSpaltenParameter)
        return self.relitable, rowsAsNumbers

    def concatMondExponzierenLogarithmusTyp(
        self, relitable: list, rowsAsNumbers: set
    ) -> tuple:
        self.relitable = relitable
        if rowsAsNumbers >= {64}:
            hardcodedCouple = (44, 56)
            for rownum, rowheading in zip(
                hardcodedCouple,
                [
                    "Mond-Typ eines Sternpolygons",
                    "Mond-Typ eines gleichförmigen Polygons",
                ],
            ):
                rowsAsNumbers |= {len(self.relitable[0])}
                for i, cols in enumerate(deepcopy(self.relitable)):
                    moonTypesOf1Num = moonNumber(i)
                    if i == 0:
                        into = rowheading
                    else:
                        into = "" if len(moonTypesOf1Num[0]) > 0 else "kein Mond"
                        for k, (basis, exponentMinus2) in enumerate(
                            zip(*moonTypesOf1Num)
                        ):
                            if k > 0:
                                into += " | "
                            insert = re.sub(
                                r"<SG>",
                                self.relitable[i][4].strip(),
                                self.relitable[basis][rownum].rstrip(),
                            )
                            into += (
                                insert + " - " + self.relitable[exponentMinus2 + 2][10]
                            )
                            into += " | "
                            into += (
                                self.relitable[i][10] + " + " + self.relitable[i][11]
                            )
                            into += ", " + self.relitable[exponentMinus2 + 2][85]
                    self.relitable[i] += [into]
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
                x("WIE2", self.tables.dataDict[0][64])

                x("idiot", self.tables.generatedSpaltenParameter)
        return self.relitable, rowsAsNumbers

    def concatRowsOfConcepts(
        self, relitable: list, conceptsRowsSetOfTuple: set, rowsAsNumbers: set
    ) -> tuple:
        self.relitable: list = relitable
        return self.relitable, rowsAsNumbers
        self.concepts: list = []
        couplesNums = []
        for i, paar in enumerate(conceptsRowsSetOfTuple):
            first = []
            second = []
            self.concepts += [(first, second)]
            for cols in self.relitable:
                first += [cols[paar[0]]]
                second += [cols[paar[1]]]
            rowsAsNumbers |= {len(self.relitable[0]) + i}
            couplesNums += [paar]
        for o, concept in enumerate(self.concepts):
            for i, (cols, row1, row2) in enumerate(
                zip(deepcopy(self.relitable), concept[0], concept[1])
            ):
                if i == 0:
                    into = "Generiert: " + row1
                else:
                    # d.h. into füll wegen zip nur die Bereiche, die Bedacht
                    # sind und alles andere sind nicht ein mal leere Strings,
                    # sondern garn nichts: schlecht !
                    into = ""
                    # i muss hier i > irgendwas sein weil mir sonst alles um die Ohren fliegt
                    # i ist die Zeile
                    if row1.strip() != "":
                        into += "sehr: " + row1 + "| "
                    if i > 2 and concept[0][i - 2].strip() != "":
                        into += "ganz gut: " + concept[0][i - 2] + "| "
                    if len(concept[0]) > i + 2 and concept[0][i + 2].strip() != "":
                        into += "ganz gut: " + concept[0][i + 2] + "| "
                    if i > 4 and concept[0][i - 4].strip() != "":
                        into += "noch etwas: " + concept[0][i - 4] + "| "
                    if len(concept[0]) > i + 4 and concept[0][i + 4].strip() != "":
                        into += "noch etwas: " + concept[0][i + 4] + "| "
                    if i > 1 and concept[1][i - 1].strip() != "":
                        into += concept[1][i - 1] + "| "
                    if i > 3 and concept[1][i - 3].strip() != "":
                        into += "ein wenig: " + concept[1][i - 3] + "| "
                    if len(concept[1]) > i + 3 and concept[1][i + 3].strip() != "":
                        into += "ein wenig: " + concept[1][i + 3] + "| "
                    if len(concept[1]) > i + 1 and concept[1][i + 1].strip() != "":
                        into += concept[1][i + 1] + "| "
                    if into != "":
                        into += "alles zur selben Strukturgröße einer " + cols[4]
                # einzeln, bis es eine ganze neue Spalte ist
                self.relitable[i] += [into]
            x(
                "ddd",
                len(self.tables.generatedSpaltenParameter)
                + self.tables.SpaltenVanillaAmount,
            )
            if (
                len(self.tables.generatedSpaltenParameter)
                + self.tables.SpaltenVanillaAmount
                in self.tables.generatedSpaltenParameter
            ):
                raise ValueError
            self.tables.generatedSpaltenParameter[
                len(self.tables.generatedSpaltenParameter)
                + self.tables.SpaltenVanillaAmount
            ] = self.tables.dataDict[1][couplesNums[o]]

            x("idiot", self.tables.generatedSpaltenParameter)
        return self.relitable, rowsAsNumbers

    def concatVervielfacheZeile(self, relitable: list, rowsAsNumbers: set) -> tuple:
        self.relitable = relitable
        # reliCopy = deepcopy(relitable)
        spaltenToVervielfache: set = rowsAsNumbers & {90, 19}
        for s in spaltenToVervielfache:
            store = {}
            for z, zeileninhalt in enumerate(relitable[2:], 2):
                content = zeileninhalt[s]
                if len(content.strip()) > 0:
                    store[(z, s)] = content  # interessant
            # x("store", store)
            multis = {}
            for (coords, content) in store.items():
                vielfacher = 1
                ergebnis = vielfacher * coords[0]
                # multis[ergebnis] = [coords[0]]
                try:
                    multis[ergebnis] += [coords[0]]  # interessant
                    # spalten wo was hin soll = ursprungszeile1,2,3,...
                except (IndexError, KeyError):
                    multis[ergebnis] = [coords[0]]  # interessant

                while ergebnis < len(relitable):
                    vielfacher += 1
                    ergebnis = vielfacher * coords[0]
                    try:
                        multis[ergebnis] += [coords[0]]  # interessant
                        # spalten wo was hin soll = ursprungszeile1,2,3,...
                    except (IndexError, KeyError):
                        multis[ergebnis] = [coords[0]]  # interessant
            x("iiii", store)
            for z, zeileninhalt in enumerate(relitable[2:], 2):
                # alle spalten und zeilen
                xx = False
                if len(relitable[z][s].strip()) != 0:
                    relitable[z][s] += " | "
                if z in multis:
                    for UrZeile in multis[z]:
                        # x("etr", str(UrZeile))
                        # x("etr", s)
                        if (
                            UrZeile != z
                            and relitable[z][s] != store[(UrZeile, s)]
                            and relitable[z][s] + " | " != store[(UrZeile, s)]
                        ):
                            # if (z == 12):
                            #    x("jjjj", store[(UrZeile, s)])
                            if len(store[(UrZeile, s)]) != 0:
                                relitable[z][s] += store[(UrZeile, s)] + " | "
                            xx = True
                            # Zelleninhalt +=
                if xx:
                    relitable[z][s] = relitable[z][s][:-3]

        return self.relitable, rowsAsNumbers

    def concatModallogik(
        self, relitable: list, conceptsRowsSetOfTuple: set, rowsAsNumbers: set
    ) -> tuple:
        """setzt die Modallogik um, d.h. Kombination von 2 bisher Programmierten
        Funktionen: 1. vielfache von Primzahlen oder natürlichen Zahlen
        (zweiteres programmiere ich später) bilden
        und die andere Funtion 2. +- 1 +- 2 und Bedeutungsveränderung

        @type relitable: list
        @param relitable: Haupttabelle self.relitable
        @return: relitable + weitere Tabelle daneben
        """

        def getModaloperatorsPerLineCells(lineWeAreAt: int) -> tuple:
            """Gibt ein Tuple aus Strings aus, dass die richtigen Modaloperatoren
            pro Zeile ausgibt
            @type int
            @param Zeile
            @return: Tupel aus Modaloperatoren
            """

            def getModaloperatorsPerLineCoordinates(lineWeAreAt: int) -> tuple:
                modalMainOperatorZeile: int = lineWeAreAt
                amountModaloperators: int = lineWeAreAt - 1
                modalOpElseOperatorsZeilenBegin: int = lineWeAreAt + 1
                modalOpElseOperatorsZeilenEnd: int = (
                    lineWeAreAt + amountModaloperators + 1
                )
                return (
                    modalMainOperatorZeile,
                    modalOpElseOperatorsZeilenBegin,
                    modalOpElseOperatorsZeilenEnd,
                )

            coords = getModaloperatorsPerLineCoordinates(lineWeAreAt)
            modaloperators: list = []
            try:
                # modaloperators += [self.relitable[coords[0]][10]]
                modaloperators += [
                    self.relitable[coords[0]][97],
                    self.relitable[coords[0]][98],
                ]
            except:
                pass
            for coord in range(coords[1], coords[2]):
                try:
                    # modaloperators += [self.relitable[coord][42]]
                    modaloperators += [self.relitable[coord][42]]
                except IndexError:
                    pass
            return tuple(modaloperators)

        def ModalLogikIntoTable(
            concept, distanceFromLine, i, into, vorkommenVielfacher_B
        ):
            # i_with_a_distance = i + distanceFromLine
            try:
                modalOperatorenEn = vorkommenVielfacher_B[i][distanceFromLine]["modalS"]
                vervielfachterEn = vorkommenVielfacher_B[i][distanceFromLine][
                    "vervielfachter"
                ]
                for modalOperatoren, vervielfachter in zip(
                    modalOperatorenEn, vervielfachterEn
                ):
                    try:
                        # x("_ü1_", modalOperatoren)
                        # x("_ü2_", vervielfachter)
                        # x("_ü6_", concept[1])
                        x(
                            "_ü3_",
                            self.relitable[vervielfachter][concept[1]],
                        )
                        # x("_ü4_", modalOperatoren[0])
                        # x("_ü5_", modalOperatoren[1:])
                        into[i] += (
                            (
                                "mittelstark überdurchschnittlich: "
                                if abs(distanceFromLine) == 2
                                else (
                                    "überdurchschnittlich: "
                                    if abs(distanceFromLine) == 1
                                    else (
                                        "mittelleicht überdurchschnittlich: "
                                        if abs(distanceFromLine) == 3
                                        else (
                                            "sehr: "
                                            if abs(distanceFromLine) == 0 != ""
                                            else "sehr leicht überdurchschnittlich: "
                                        )
                                    )
                                )
                            )
                            + (
                                # ""
                                # if abs(distanceFromLine) % 2 == 1
                                # else
                                (modalOperatoren[0] + " ")
                            )
                            + (
                                (self.relitable[vervielfachter][concept[0]])
                                if (abs(distanceFromLine) % 2 == 0)
                                else self.relitable[vervielfachter][concept[1]]
                            )
                            + " "
                            + modalOperatoren[1]
                            + (
                                (
                                    ", nicht: "
                                    + ", ".join(modalOperatoren[2:])
                                    + " (das alles nicht): "
                                    + self.relitable[vervielfachter][concept[0]]
                                    if len(modalOperatoren) > 2
                                    else ""
                                )
                                if abs(distanceFromLine) % 2 == 1
                                else ""
                            )
                            + " | "
                        )
                    except (IndexError, KeyError):
                        pass
            except (IndexError, KeyError):
                pass

        def storeModalNvervielfachter(
            Orginal_i_mehrere,
            distanceFromLine,
            i,
            modalOperatorEnEn,
            vervielFachter,
            vorkommenVielfacher_B,
        ):
            vorkommenVielfacher_B[i][distanceFromLine] = {
                "i_origS": Orginal_i_mehrere,
                "modalS": modalOperatorEnEn,
                "vervielfachter": vervielFachter,
            }

        def prepareModalIntoTable(
            distanceFromLine,
            getModaloperatorsPerLineCells,
            i,
            storeModalNvervielfachter,
            vorkommenVielfacher,
            vorkommenVielfacher_B,
        ):
            i_with_a_distance = i + distanceFromLine
            try:
                modalOperatorEnEn: list = []
                Orginal_i_mehrere: list = []
                # vorkommenZeilenBegriffe: list = []
                vervielFachter: list = []
                # Ein Couple besteht aus der Zahl, ggf. Primzahl mit ihrem Vielfacher danach
                for couple in vorkommenVielfacher[i_with_a_distance]:
                    # x("x4hh", couple)
                    vorkommen, vielfacher = couple[0], couple[1]
                    modalOperatorEnEn += [(getModaloperatorsPerLineCells(vielfacher))]
                    # vorkommenZeilenBegriffe += [
                    #    vorkommen * vielfacher
                    # ]
                    vervielFachter += [vorkommen]
                    Orginal_i_mehrere += [i_with_a_distance]
                """
                Was ist hier drin gespeichert?
                    erster Parameter: das i von allen Distanzen -4 bis 4 mit 0
                    zweiter Paramter: Ob: ModalOperator oder was war Orignal i von dem das hier der Vielfacher ist
                    dahinter: liste von der Sache
                """
                # x("r6hh1 ", i)
                # x("r6hh2 ", modalOperatorEnEn)
                # x("r6hh3 ", Orginal_i_mehrere)
                try:
                    vorkommenVielfacher_B[i][distanceFromLine] = {
                        "i_origS": Orginal_i_mehrere
                        + vorkommenVielfacher_B[i][distanceFromLine]["i_origS"],
                        "modalS": modalOperatorEnEn
                        + vorkommenVielfacher_B[i][distanceFromLine]["modalS"],
                        "vervielfachter": vervielFachter
                        + vorkommenVielfacher_B[i][distanceFromLine]["vervielfachter"],
                    }

                except (IndexError, KeyError):
                    try:
                        storeModalNvervielfachter(
                            Orginal_i_mehrere,
                            distanceFromLine,
                            i,
                            modalOperatorEnEn,
                            vervielFachter,
                            vorkommenVielfacher_B,
                        )
                    except (IndexError, KeyError):
                        vorkommenVielfacher_B[i] = {}
                        storeModalNvervielfachter(
                            Orginal_i_mehrere,
                            distanceFromLine,
                            i,
                            modalOperatorEnEn,
                            vervielFachter,
                            vorkommenVielfacher_B,
                        )
                del vervielFachter
            except (IndexError, KeyError):
                pass

        def vorkommenNvielfacherPerItsProduct(
            einVorkommen, ergebnis, vielfacher, vorkommenVielfacher
        ):
            try:
                vorkommenVielfacher[ergebnis] += [
                    (
                        einVorkommen,
                        vielfacher,
                    )
                ]
            except (IndexError, KeyError):
                vorkommenVielfacher[ergebnis] = [
                    (
                        einVorkommen,
                        vielfacher,
                    )
                ]

        self.relitable = relitable
        if True:
            distances = (-4, -3, -2, -1, 0, 1, 2, 3, 4)
            conceptsRowsSetOfTuple2: tuple = tuple(conceptsRowsSetOfTuple)
            # x("wer", conceptsRowsSetOfTuple2)
            reliTableCopy = deepcopy(self.relitable)
            for o, concept in enumerate(conceptsRowsSetOfTuple2):
                into: dict = {}
                einMalVorkommen = set()
                for i, cols in enumerate(reliTableCopy):
                    into[i] = ""
                    if i == 0:
                        into[i] = "Generiert: " + cols[concept[0]]
                    elif cols[concept[0]].strip() != "":
                        einMalVorkommen |= {i}

                vorkommenVielfacher: dict = {}
                einMalVorkommen = tuple(einMalVorkommen)

                for (
                    einVorkommen
                ) in (
                    einMalVorkommen
                ):  # d.h. so ein Wort wie weise oder gut kommt in vor in der csv
                    vielfacher = 1
                    ergebnis = vielfacher * einVorkommen
                    vorkommenNvielfacherPerItsProduct(
                        einVorkommen, ergebnis, vielfacher, vorkommenVielfacher
                    )
                    while ergebnis < len(reliTableCopy):
                        vielfacher += 1
                        ergebnis = vielfacher * einVorkommen
                        vorkommenNvielfacherPerItsProduct(
                            einVorkommen, ergebnis, vielfacher, vorkommenVielfacher
                        )

                # x("d5g", vorkommenVielfacher)
                vorkommenVielfacher_B: dict = {}
                for i, zeileninhalte in enumerate(reliTableCopy[1:], 1):
                    for distanceFromLine in distances:
                        prepareModalIntoTable(
                            distanceFromLine,
                            getModaloperatorsPerLineCells,
                            i,
                            storeModalNvervielfachter,
                            vorkommenVielfacher,
                            vorkommenVielfacher_B,
                        )

                for i, zeileninhalte in enumerate(reliTableCopy[1:], 1):
                    # x("_ö_", vorkommenVielfacher_B)
                    for distanceFromLine in distances:
                        ModalLogikIntoTable(
                            concept, distanceFromLine, i, into, vorkommenVielfacher_B
                        )
                    # wenn i>0
                    if into[i] != "":
                        into[i] += (
                            "alles nur bezogen auf die selbe Strukturgröße einer "
                            + zeileninhalte[4]
                        )
                for w, cols in enumerate(reliTableCopy):
                    self.relitable[w] += [into[w]]

                rowsAsNumbers |= {len(self.relitable[0]) - 1}
                if (
                    len(self.tables.generatedSpaltenParameter)
                    + self.tables.SpaltenVanillaAmount
                    in self.tables.generatedSpaltenParameter
                ):
                    raise ValueError
                self.tables.generatedSpaltenParameter[
                    len(self.tables.generatedSpaltenParameter)
                    + self.tables.SpaltenVanillaAmount
                ] = self.tables.dataDict[1][conceptsRowsSetOfTuple2[o]]

        return self.relitable, rowsAsNumbers

    def concat1RowPrimUniverse(self, relitable: list, rowsAsNumbers: set) -> tuple:
        """Fügt eine Spalte ein, in der Primzahlen mit Vielfachern
        auf dem Niveau des Universums nicht einfach nur aus einer
        CSV Tabelle geladen werden, sondern durch Primzahlen und
        deren Vielfachern generiert werden.

        @type relitable: list
        @param relitable: Haupttabelle self.relitable
        @return: relitable + weitere Tabelle daneben
        """
        global originalLinesRange
        self.relitable = relitable
        hardCodedCouple = (10, 42)
        if len(self.tables.primUniversePrimsSet) > 0:
            self.tables.primUniverseRowNum = len(self.relitable[0])
            rowsAsNumbers |= {
                len(self.relitable[0]),
                len(self.relitable[0]) + 1,
            }
            for polytype, polytypename in zip(
                hardCodedCouple, ["Sternpolygone", "gleichförmiges Polygone"]
            ):
                self.transzendentalien = []
                self.rolle = []
                self.motivation = []
                self.ziel = []
                for cols in self.relitable:
                    self.motivation += [cols[polytype]]
                    self.rolle += [cols[19]]
                    self.transzendentalien += [cols[5]]
                    self.ziel += [cols[11]]
                relitableCopy = deepcopy(self.relitable)

                for i, cols in enumerate(relitableCopy):
                    primMultiples = primMultiple(i)
                    into = (
                        "" if i != 0 else "generierte Multiplikationen " + polytypename
                    )
                    for k, multi in enumerate(primMultiples[1:]):
                        if k > 0:
                            into += ", außerdem: "
                        into += (
                            "("
                            + (
                                self.transzendentalien[multi[0]]
                                if self.transzendentalien[multi[0]].strip() != ""
                                else "..."
                            )
                            + " UND "
                            + (
                                self.rolle[multi[0]]
                                if self.rolle[multi[0]].strip() != ""
                                else "..."
                            )
                            + ") * ("
                            + (
                                self.motivation[multi[1]]
                                if self.motivation[multi[1]].strip() != ""
                                else "..."
                            )
                            + (
                                " UND "
                                + (
                                    self.ziel[multi[1]]
                                    if self.ziel[multi[1]].strip() != ""
                                    else "..."
                                )
                                if polytype == 10
                                else ""
                            )
                            + ")"
                        )
                    self.relitable[i] += [into]

                if (
                    len(self.tables.generatedSpaltenParameter)
                    + self.tables.SpaltenVanillaAmount
                    in self.tables.generatedSpaltenParameter
                ):
                    raise ValueError
                x(
                    "doofi 1",
                    len(self.tables.generatedSpaltenParameter)
                    + self.tables.SpaltenVanillaAmount,
                )
                x("doofi 2", tuple(self.tables.dataDict[1].keys())[0])
                x("doofi 3", primzahlvielfachesgalaxie)
                self.tables.generatedSpaltenParameter[
                    len(self.tables.generatedSpaltenParameter)
                    + self.tables.SpaltenVanillaAmount
                ] = ([primzahlvielfachesgalaxie],)

                x("idiot", self.tables.generatedSpaltenParameter)

        if (
            len(self.tables.primUniversePrimsSet) > 0
            or rowsAsNumbers >= {5}
            or rowsAsNumbers >= {135}
        ):
            self.relitable, rowsAsNumbers = self.spalteFuerGegenInnenAussenSeitlichPrim(
                self.relitable, rowsAsNumbers
            )
            x("idiot__", self.tables.generatedSpaltenParameter)

        return self.relitable, rowsAsNumbers

    def spalteMetaKontretTheorieAbstrakt_etc_1(
        self, relitable: list, rowsAsNumbers: set, geordnetePaare: set
    ):
        self.relitable = relitable
        self.rowsAsNumbers = rowsAsNumbers
        for paar in tuple(geordnetePaare):
            self.spalteMetaKontretTheorieAbstrakt_etc(
                relitable,
                rowsAsNumbers,
                paar[0],
                1 if paar[1] == 0 else 2 if paar[1] == 1 else 3,
            )
        return self.relitable, self.rowsAsNumbers

    def spalteMetaKontretTheorieAbstrakt_etc(
        self,
        relitable: list,
        rowsAsNumbers: set,
        metavariable: int = 2,
        lower1greater2both3: int = 3,
    ) -> tuple:

        self.relitable = relitable
        rowsAsNumbers |= {
            len(self.relitable[0]),
        }
        transzendentalienSpalten: tuple = (5, 131)
        newCol = transzendentalienSpalten[0]
        """bis hier hin waren es die Vorinitialisierungen von Variablen"""

        # def switching(metavariable: int, lower1greater2both3: int, row: int):
        def switching(newCol: int, moreAndLess: tuple) -> tuple:
            """2 neue Koordinaten der Tabelle durch 3 Parameter, d.h. einer, newCol, gilt für beide
            Immer eine halbierung und dopplung oder verdreifachung und ..., etc.
            und wechsel der Spalte von den 2 Spalten"""
            x("MORE", moreAndLess)
            newCol = (
                transzendentalienSpalten[0]
                if newCol == transzendentalienSpalten[1]
                else transzendentalienSpalten[0]
            )
            a = (
                moreAndLess[0] * metavariable
                if not moreAndLess[0] is None
                and moreAndLess[0] * metavariable < len(relitable)
                and len((relitable[moreAndLess[0] * metavariable][newCol]).strip()) > 3
                else None
            )
            b = (
                int(moreAndLess[1] / metavariable)
                if not moreAndLess[1] is None
                and moreAndLess[1] / metavariable
                == round(moreAndLess[1] / metavariable)
                and len((relitable[int(moreAndLess[1] / metavariable)][newCol]).strip())
                > 3
                else None
            )
            moreAndLess = (a, b)
            x("MORE", metavariable)
            x("MORE", moreAndLess)
            return newCol, moreAndLess

        metaOrWhat = {2: (("Meta-Thema: ", "konkretes: "), ("Meta-", "konkret-"))}

        def makeVorwort(
            wiederholungen: int, vorworte2: tuple, less1ormore2: int
        ) -> str:
            return (
                vorworte2[less1ormore2 - 1] * wiederholungen
                if wiederholungen > 1
                else vorworte2[less1ormore2 - 1]
            )

        """Haupt-Teil, das davor waren Vorbereitungen
        das große Durchiterieren beginnt durch die Tabelle mit anschließendem erweitern dieser, um Spalten"""
        for bothRows in (
            [0, 1]
            if lower1greater2both3 == 3
            else [
                0,
            ]
            if lower1greater2both3 == 1
            else [
                1,
            ]
            if lower1greater2both3 == 2
            else []
        ):
            rowsAsNumbers |= {len(self.relitable[0])}
            for i, row in enumerate(relitable[:2]):
                self.relitable[i] += [""]
            for i, row in enumerate(relitable[2:], 2):
                moreAndLess = (i, i)  # 1. wert "*2" und 2. "/3"
                neue2KoordNeue2Vorwoerter: list = []
                alxp("new while")
                while moreAndLess != (None, None):
                    newCol, moreAndLess = switching(newCol, moreAndLess)
                    vorworte2 = metaOrWhat[metavariable][
                        0 if len(neue2KoordNeue2Vorwoerter) == 0 else 1
                    ]
                    wort1: str = makeVorwort(
                        len(neue2KoordNeue2Vorwoerter) + 1, vorworte2, 1
                    )
                    wort2: str = makeVorwort(
                        len(neue2KoordNeue2Vorwoerter) + 1, vorworte2, 2
                    )
                    neue2KoordNeue2Vorwoerter += [(moreAndLess, newCol, wort1, wort2)]

                intoList = []
                for vier in neue2KoordNeue2Vorwoerter:
                    alxp(vier)
                    if not vier[0][0] is None and not vier[1] is None:
                        alxp(relitable[vier[0][0]][vier[1]])
                    if not vier[0][1] is None and not vier[1] is None:
                        alxp(relitable[vier[0][1]][vier[1]])
                    intoList += [vier[bothRows + 2]] + (
                        [relitable[vier[0][0]][vier[1]]]
                        if bothRows == 0 and not vier[0][0] is None
                        else [relitable[vier[0][1]][vier[1]]]
                        if bothRows == 1 and not vier[0][1] is None
                        else [
                            relitable[vier[0][0]][vier[1]],
                            relitable[vier[0][1]][vier[1]],
                        ]
                        if not vier[0][0] is None and not vier[0][1] is None
                        else [""]
                    )
                alxp(intoList)
                self.relitable[i] += [" | ".join(intoList)[3:-3]]
            """bevor ich das programmiere, erst Parameter dafür festlegen!!!"""
            if lower1greater2both3 != 3:
                self.tables.generatedSpaltenParameter[
                    len(self.tables.generatedSpaltenParameter)
                    + self.tables.SpaltenVanillaAmount
                ] = self.tables.dataDict[4][(metavariable, lower1greater2both3 - 1)]
            else:
                for both in (
                    0,
                    1,
                ):
                    self.tables.generatedSpaltenParameter[
                        len(self.tables.generatedSpaltenParameter)
                        + self.tables.SpaltenVanillaAmount
                    ] = self.tables.dataDict[4][(metavariable, both)]

        x("r_wt", self.tables.generatedSpaltenParameter)
        return self.relitable, rowsAsNumbers

    def spalteFuerGegenInnenAussenSeitlichPrim(
        self, relitable: list, rowsAsNumbers: set
    ) -> tuple:

        self.relitable = relitable
        self.primAmounts = 0
        self.oldPrimAmounts = 0
        self.lastPrimAnswers: dict = {}

        rowsAsNumbers |= {
            len(self.relitable[0]),
        }

        def PrimAnswer2(i: int) -> str:
            return self.lastPrimAnswers[i]

        def PrimAnswer(i: int) -> str:
            if i > 3:
                if self.primAmounts != self.oldPrimAmounts:
                    if self.primAmounts % 2 == 0:
                        return "für innen"
                    else:
                        return "für außen"
                else:
                    return ""
            elif i == 2:
                return "für seitlich"
            elif i == 3:
                return "gegen seitlich"
            elif i == 1:
                return "alle Richtungen möglich"
            else:
                return ""

        for i, cols in enumerate(relitable):
            # primMultiples = primMultiple(i)
            into = "" if i != 0 else "Primzahlwirkung "

            self.oldPrimAmounts = self.primAmounts
            if couldBePrimeNumberPrimzahlkreuz(i):
                self.primAmounts += 1
            if primCreativity(i) == 1:
                into = PrimAnswer(i)
                self.lastPrimAnswers[i] = into
            elif i > 1:
                for couple in primRepeat(primFak(i)):
                    if couple[1] == 1:
                        into += PrimAnswer2(couple[0]) + " + "
                    else:
                        into += str(couple[1]) + " * " + PrimAnswer2(couple[0]) + " + "
                into = into[:-3]
            elif i == 1:
                into = PrimAnswer(1)
            self.relitable[i] += [into]
        self.tables.generatedSpaltenParameter[
            len(self.tables.generatedSpaltenParameter)
            + self.tables.SpaltenVanillaAmount
        ] = (self.tables.dataDict[0][5][0], [primzahlvielfachesgalaxie])
        x("rewt", self.tables.generatedSpaltenParameter)
        return self.relitable, rowsAsNumbers

    def readConcatCsv(self, relitable: list, rowsAsNumbers: set) -> tuple:
        """Fügt eine Tabelle neben der self.relitable an
        momentan ist es noch fix auf primnumbers.csv

        @type relitable: list
        @param relitable: Haupttabelle self.relitable
        @type rowsAsNumbers: set
        @param rowsAsNumbers: welche Spalten der neuen Tabelle dazu kommen sollen
        @rtype: list[list]
        @return: relitable + weitere Tabelle daneben
        """
        global folder
        place = os.path.join(
            os.getcwd(),
            os.path.dirname(__file__),
            os.path.basename("./primenumbers.csv"),
        )
        self.relitable = relitable
        headingsAmount = len(self.relitable[0])
        self.tables.SpaltenVanillaAmount = len(rowsAsNumbers)
        if len(self.puniverseprims) > 0:
            with open(place, mode="r") as csv_file:
                self.relitable, primUniverseLine = self.tables.fillBoth(
                    self.relitable, list(csv.reader(csv_file, delimiter=";"))
                )
                lastlen = 0
                maxlen = 0
                for i, (primcol, relicol) in enumerate(
                    zip(primUniverseLine, self.relitable)
                ):
                    lastlen = len(primcol)
                    if lastlen > maxlen:
                        maxlen = lastlen

                    self.relitable[i] += list(primcol) + [""] * (maxlen - len(primcol))
                    if i == 0:
                        for u, heading in enumerate(self.relitable[0]):
                            if (
                                heading.isdecimal()
                                and int(heading) in self.puniverseprims
                                and u >= headingsAmount
                            ):
                                rowsAsNumbers.add(u)
                                heading = int(heading)
                                if (
                                    len(self.tables.generatedSpaltenParameter)
                                    + self.tables.SpaltenVanillaAmount
                                    in self.tables.generatedSpaltenParameter
                                ):
                                    raise ValueError
                                alxp("XYZ")
                                x("zzz2", self.tables.generatedSpaltenParameter)
                                self.tables.generatedSpaltenParameter[
                                    len(self.tables.generatedSpaltenParameter)
                                    + self.tables.SpaltenVanillaAmount
                                ] = self.tables.dataDict[2][heading]
                                x("zzz", self.tables.generatedSpaltenParameter)

            self.concatRowsAmount = len(primcol)
        return self.relitable, rowsAsNumbers
