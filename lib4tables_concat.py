#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import os
import sys
from collections import defaultdict
from copy import copy, deepcopy
from fractions import Fraction
from itertools import zip_longest

from center import (Multiplikationen, alxp, cliout, getTextWrapThings, infoLog,
                    output, re, x)
from lib4tables import (OutputSyntax, bbCodeSyntax,
                        couldBePrimeNumberPrimzahlkreuz,
                        couldBePrimeNumberPrimzahlkreuz_fuer_aussen,
                        couldBePrimeNumberPrimzahlkreuz_fuer_innen, csvSyntax,
                        divisorGenerator, htmlSyntax, isPrimMultiple,
                        markdownSyntax, math, moonNumber, multiples,
                        primCreativity, primFak, primMultiple, primRepeat)
from lib4tables_Enum import ST


class Concat:
    def __init__(self, tables):
        self.tables = tables
        self.ones = set()
        self.CSVsAlreadRead = {}
        self.CSVsSame = {1: (1,), 2: (2, 4), 3: (3, 5), 4: (2, 4), 5: (3, 5)}
        self.BruecheUni = set()
        self.BruecheGal = set()
        self.gebrRatMulSternUni = set()
        self.gebrRatDivSternUni = set()
        self.gebrRatMulGleichfUni = set()
        self.gebrRatDivGleichfUni = set()
        self.gebrRatMulSternGal = set()
        self.gebrRatDivSternGal = set()
        self.gebrRatMulGleichfGal = set()
        self.gebrRatDivGleichfGal = set()

    @property
    def gebrUnivSet(self):
        return self.puniverseprims

    @gebrUnivSet.setter
    def gebrUnivSet(self, value: set):
        self.gebrUniv = value

    @property
    def primUniversePrimsSet(self):
        return self.puniverseprims

    @primUniversePrimsSet.setter
    def primUniversePrimsSet(self, value: set):
        self.puniverseprims = value

    def concatLovePolygon(self, relitable: list, rowsAsNumbers: set) -> tuple:
        self.relitable = relitable
        if rowsAsNumbers >= {9}:
            rowsAsNumbers |= {len(self.relitable[0])}
            self.tables.generatedSpaltenParameter_Tags[
                len(rowsAsNumbers) - 1
            ] = frozenset({ST.sternPolygon, ST.galaxie, ST.gleichfoermigesPolygon})
            for i, cols in enumerate(deepcopy(self.relitable)):
                if self.relitable[i][8].strip() != "":
                    self.relitable[i] += [
                        "".join(
                            (
                                self.relitable[i][8],
                                " der eigenen Strukturgröße (",
                                self.relitable[i][4],
                                ") auf dich bei gleichförmigen Polygonen",
                            )
                        )
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
            ] = self.tables.dataDict[0][9]
            # x("bliu3", self.tables.generatedSpaltenParameter)
        return self.relitable, rowsAsNumbers

    def concatPrimCreativityType(self, relitable: list, rowsAsNumbers: set) -> tuple:
        self.relitable = relitable
        if rowsAsNumbers >= {64}:
            rowsAsNumbers |= {len(self.relitable[0])}
            self.tables.generatedSpaltenParameter_Tags[
                len(rowsAsNumbers) - 1
            ] = frozenset({ST.sternPolygon, ST.galaxie})
            for i, cols in enumerate(
                deepcopy(self.relitable[: self.tables.lastLineNumber + 1])
            ):
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
            # x("WIE", self.tables.dataDict[0][64])
            # x("JDG", self.tables.generatedSpaltenParameter)

            # x("idiot", self.tables.generatedSpaltenParameter)
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
                self.tables.generatedSpaltenParameter_Tags[len(rowsAsNumbers) - 1] = (
                    frozenset({ST.sternPolygon, ST.universum})
                    if rownum == 0
                    else frozenset({ST.gleichfoermigesPolygon, ST.universum})
                )
                for i, cols in enumerate(
                    deepcopy(self.relitable[: self.tables.lastLineNumber + 1])
                ):
                    moonTypesOf1Num = moonNumber(i)
                    if i == 0:
                        into = [rowheading]
                    else:
                        into = [
                            "[list]"
                            if self.tables.bbcodeOutputYes
                            else "<ul>"
                            if self.tables.htmlOutputYes
                            else "",
                            "" if len(moonTypesOf1Num[0]) > 0 else "kein Mond",
                        ]
                        for k, (basis, exponentMinus2) in enumerate(
                            zip(*moonTypesOf1Num)
                        ):
                            if k > 0:
                                into += [" | "]
                            if self.tables.htmlOutputYes:
                                into += ["<li>"]
                            elif self.tables.bbcodeOutputYes:
                                into += ["[*]"]
                            insert = re.sub(
                                r"<SG>",
                                self.relitable[i][4].strip(),
                                self.relitable[basis][rownum].rstrip(),
                            )
                            into += [
                                insert,
                                " - ",
                                self.relitable[exponentMinus2 + 2][10],
                                " | ",
                                "</li>" if self.tables.htmlOutputYes else "",
                                self.relitable[i][10],
                                " + ",
                                self.relitable[i][11],
                                ", ",
                                self.relitable[exponentMinus2 + 2][85],
                            ]
                    if self.tables.htmlOutputYes and i != 0:
                        into += ["</ul>"]
                    self.relitable[i] += ["".join(into)]
                assert not (
                    len(self.tables.generatedSpaltenParameter)
                    + self.tables.SpaltenVanillaAmount
                    in self.tables.generatedSpaltenParameter
                )

                self.tables.generatedSpaltenParameter[
                    len(self.tables.generatedSpaltenParameter)
                    + self.tables.SpaltenVanillaAmount
                ] = self.tables.dataDict[0][64]

        return self.relitable, rowsAsNumbers

    def concatVervielfacheZeile(self, relitable: list, rowsAsNumbers: set) -> tuple:
        self.relitable = relitable
        # reliCopy = deepcopy(relitable)
        spaltenToVervielfache: set = rowsAsNumbers & {90, 19}
        for s in spaltenToVervielfache:
            store = {}
            for z, zeileninhalt in enumerate(
                relitable[2 : self.tables.lastLineNumber + 1], 2
            ):
                content = zeileninhalt[s]
                if len(content.strip()) > 0:
                    store[(z, s)] = content  # interessant
            # #x("store", store)
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
            # x("iiii", store)
            for z, zeileninhalt in enumerate(
                relitable[2 : self.tables.lastLineNumber + 1], 2
            ):
                # alle spalten und zeilen
                xx = False

                if len(relitable[z][s].strip()) != 0:
                    if self.tables.htmlOutputYes:
                        relitable[z][s] = ["<li>", relitable[z][s], "</li>"]
                    elif self.tables.bbcodeOutputYes:
                        relitable[z][s] = ["[*]", relitable[z][s]]
                    else:
                        relitable[z][s] = [relitable[z][s], " | "]
                else:
                    relitable[z][s] = [relitable[z][s]]

                if z in multis:
                    for UrZeile in multis[z]:
                        if (
                            UrZeile != z
                            and "".join(relitable[z][s]) != store[(UrZeile, s)]
                            and "".join(relitable[z][s] + [" | "])
                            != store[(UrZeile, s)]
                            and "".join(["<li>"] + relitable[z][s] + ["</li>"])
                            != store[(UrZeile, s)]
                            and "".join(["[*]"] + relitable[z][s])
                            != store[(UrZeile, s)]
                        ):
                            if len(store[(UrZeile, s)]) != 0:
                                if self.tables.htmlOutputYes:
                                    relitable[z][s] += [
                                        "<li>",
                                        store[(UrZeile, s)],
                                        "</li>",
                                    ]
                                elif self.tables.bbcodeOutputYes:
                                    relitable[z][s] += ["[*]", store[(UrZeile, s)]]
                                else:
                                    xx = (
                                        True
                                        if not self.tables.bbcodeOutputYes
                                        else False
                                    )
                                    relitable[z][s] += [store[(UrZeile, s)], " | "]

                if self.tables.htmlOutputYes:
                    relitable[z][s] = ["<ul>"] + relitable[z][s] + ["</ul>"]
                elif self.tables.bbcodeOutputYes:
                    relitable[z][s] = ["[list]"] + relitable[z][s] + ["[/list]"]
                if xx:
                    relitable[z][s] = "".join(relitable[z][s][:-1])
                else:
                    relitable[z][s] = "".join(relitable[z][s])

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
            try:
                modalOperatorenEn = vorkommenVielfacher_B[i][distanceFromLine]["modalS"]
                vervielfachterEn = vorkommenVielfacher_B[i][distanceFromLine][
                    "vervielfachter"
                ]
                # x("ASD", vorkommenVielfacher_B[i][distanceFromLine]["modalS"][0][0])
                # x("DSF", self.relitable[1][97])
                for modalOperatoren, vervielfachter in zip(
                    modalOperatorenEn, vervielfachterEn
                ):
                    try:
                        intoItsContent = (
                            self.relitable[vervielfachter][concept[0]]
                            if abs(distanceFromLine) % 2 == 0
                            else self.relitable[vervielfachter][concept[1]]
                        )
                        # x("WSDRF", modalOperatoren[0] != self.relitable[1][97])

                        into[i] += [
                            "<li>"
                            if self.tables.htmlOutputYes
                            else "[*]"
                            if self.tables.bbcodeOutputYes
                            else ""
                        ]
                        into[i] += (
                            [
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
                                ),
                                modalOperatoren[0],
                                " ",
                                intoItsContent
                                if modalOperatoren[0] == self.relitable[1][97]
                                else intoItsContent.replace(
                                    "intrinsisch", "zuerst"
                                ).replace("extrinsisch", "als zweites"),
                                " ",
                                modalOperatoren[1],
                            ]
                            + (
                                (
                                    [
                                        ", nicht: ",
                                        ", ".join(modalOperatoren[2:]),
                                        " (das alles nicht): ",
                                        self.relitable[vervielfachter][concept[0]],
                                    ]
                                    if len(modalOperatoren) > 2
                                    else [""]
                                )
                                if abs(distanceFromLine) % 2 == 1
                                else [""]
                            )
                            + [
                                " | "
                                if not self.tables.htmlOutputYes
                                and not self.tables.bbcodeOutputYes
                                else ""
                            ]
                        )
                        into[i] += ["</li>" if self.tables.htmlOutputYes else ""]
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
            # x("SDF ", vorkommenVielfacher_B[i][distanceFromLine])

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
                    # #x("x4hh", couple)
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
                try:
                    vorkommenVielfacher_B[i][distanceFromLine] = {
                        "i_origS": Orginal_i_mehrere
                        + vorkommenVielfacher_B[i][distanceFromLine]["i_origS"],
                        "modalS": modalOperatorEnEn
                        + vorkommenVielfacher_B[i][distanceFromLine]["modalS"],
                        "vervielfachter": vervielFachter
                        + vorkommenVielfacher_B[i][distanceFromLine]["vervielfachter"],
                    }
                    # x("DGS ", vorkommenVielfacher_B[i][distanceFromLine])

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

        distances = (-4, -3, -2, -1, 0, 1, 2, 3, 4)
        conceptsRowsSetOfTuple2: tuple = tuple(conceptsRowsSetOfTuple)
        # #x("wer", conceptsRowsSetOfTuple2)
        reliTableCopy = deepcopy(self.relitable)
        for o, concept in enumerate(conceptsRowsSetOfTuple2):
            into: dict = {}
            einMalVorkommen = set()
            for i, cols in enumerate(reliTableCopy):
                into[i] = [""]
                if i == 0:
                    into[i] = ["Generiert: ", cols[concept[0]]]
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

            # #x("d5g", vorkommenVielfacher)
            vorkommenVielfacher_B: dict = {}
            for i, zeileninhalte in enumerate(
                reliTableCopy[1 : self.tables.lastLineNumber + 1], 1
            ):
                for distanceFromLine in distances:
                    prepareModalIntoTable(
                        distanceFromLine,
                        getModaloperatorsPerLineCells,
                        i,
                        storeModalNvervielfachter,
                        vorkommenVielfacher,
                        vorkommenVielfacher_B,
                    )

            for i, zeileninhalte in enumerate(
                reliTableCopy[1 : self.tables.lastLineNumber + 1], 1
            ):
                # #x("_ö_", vorkommenVielfacher_B)
                for distanceFromLine in distances:
                    ModalLogikIntoTable(
                        concept, distanceFromLine, i, into, vorkommenVielfacher_B
                    )
                # wenn i>0
                if into[i] != [""]:
                    into[i] += [
                        "alles nur bezogen auf die selbe Strukturgröße einer ",
                        zeileninhalte[4],
                    ]

            for w, cols in enumerate(reliTableCopy[: self.tables.lastLineNumber + 1]):
                if self.tables.htmlOutputYes and "<li>" in into[w]:
                    into[w] = ["<ul>"] + into[w] + ["</ul>"]
                elif self.tables.bbcodeOutputYes and "[*]" in into[w]:
                    into[w] = ["[list]"] + into[w] + ["[/list]"]
                self.relitable[w] += ["".join(into[w])]

            rowsAsNumbers |= {len(self.relitable[0]) - 1}
            self.tables.generatedSpaltenParameter_Tags[
                len(rowsAsNumbers) - 1
            ] = frozenset({ST.sternPolygon, ST.galaxie})
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
            # x("bliu2", self.tables.dataDict[1][conceptsRowsSetOfTuple2[o]])

        return self.relitable, rowsAsNumbers

    def convertSetOfPaarenToDictOfNumToPaareDiv(
        self, paareSet: set, gleichf=False
    ) -> defaultdict:
        """Macht aus einem Set aus Paaren eins von verschiedenen möglichen dicts mit key int und value liste aus paaren"""
        result: defaultdict = defaultdict(set)
        paareSet: tuple = tuple(paareSet)
        for paar in paareSet:
            paar = tuple(paar)
            div = paar[0] / paar[1] if not gleichf else paar[1] / paar[0]
            x("fsd", div)
            assert div == round(div)
            result[int(div)] |= {frozenset(paar)}
        # x("GHJ1A", dict(result))
        return result

    def convertSetOfPaarenToDictOfNumToPaareMul(
        self, paareSet: set, gleichf=False
    ) -> defaultdict:
        """Macht aus einem Set aus Paaren eins von verschiedenen möglichen dicts mit key int und value liste aus paaren"""
        result: defaultdict = defaultdict(set)

        for paar in tuple(paareSet):
            paar = tuple(paar)
            mul = paar[0] * paar[1]
            if gleichf:
                mul = 1 / mul
            mulr = round(mul)
            # x("jzd", [mul, mulr, gleichf])
            assert mul == mulr
            result[int(mulr)] |= {frozenset(paar)}
        # x("GHJ1B", dict(result))
        return result

    def convertFractionsToDictOfNumToPaareOfMulOfIntAndFraction(
        self, fracs: set, fracs2: set, gleichf=False
    ) -> defaultdict:
        result: defaultdict = defaultdict(set)
        if not gleichf:
            for frac in tuple(fracs):
                for zusatzMul in range(1, 1025):
                    paar = (frac, Fraction(frac.denominator) * zusatzMul)
                    mul = paar[0] * paar[1]
                    mulr = round(mul)
                    assert mulr == mul
                    if mul > 1024:
                        break
                    result[int(mul)] |= {frozenset(paar)}

            for frac in tuple(fracs):
                for zusatzMul in range(1024, 0, -1):
                    faktor = Fraction(frac.denominator) / zusatzMul
                    if (faktor in fracs2) or faktor.numerator == 1:
                        paar = (frac, faktor)
                        # x("GGG", paar)
                        mul = paar[0] * paar[1]
                        mulr = round(mul)
                        if mul > 1024:
                            break
                        if mulr == mul:
                            result[int(mul)] |= {frozenset(paar)}
            # x("IIL", result)

        else:
            for frac in tuple(fracs):
                for zusatzDiv in range(1, 1025):
                    # x("HDF1", frac)
                    paar = (frac, 1 / Fraction(frac.numerator) / zusatzDiv)
                    # x("HDF2", paar)
                    # x("HDF3", paar[0] * paar[1])
                    div = 1 / (paar[1] * paar[0])
                    # x("HDF4", div)
                    divr = round(div)
                    assert divr == div
                    if div > 1024:
                        break
                    result[int(divr)] |= {frozenset(paar)}

            for frac in tuple(fracs):
                for zusatzDiv in range(1, 1025):
                    faktor = (1 / frac) / zusatzDiv
                    if faktor in fracs2 or faktor.numerator == 1:
                        paar = (frac, faktor)
                        # x("SOV", paar)
                        mul = 1 / (paar[1] * paar[0])
                        mulr = round(mul)
                        assert mulr == mul
                        if 1 / mul > 1024:
                            break
                        result[int(mulr)] |= {frozenset(paar)}

        ##result2: defaultdict = defaultdict(list)
        # for key, value in result.items():
        #    result2[key] = list(value)

        # x("GHJ2", dict(result2))
        return result

    def combineDicts(self, a: defaultdict, b: defaultdict) -> defaultdict:
        e: defaultdict = defaultdict(set)

        for key, value in a.items():
            e[key] |= value
        for key, value in b.items():
            e[key] |= value

        for key, value in e.items():
            newValue = set()
            for v in value:
                newValue |= {tuple(v)}
            e[key] = newValue

        return e

    def concat1PrimzahlkreuzProContra(
        self,
        relitable: list,
        rowsAsNumbers: set,
        generatedBefehle: set,
        # htmlTagParaClassWoerter: list,
    ) -> tuple:
        """Fügt eine Spalte ein, in der Primzahlen mit Vielfachern
        auf dem Niveau des Universums nicht einfach nur aus einer
        CSV Tabelle geladen werden, sondern durch Primzahlen und
        deren Vielfachern generiert werden.

        @type relitable: list
        @param relitable: Haupttabelle self.relitable
        @return: relitable + weitere Tabelle daneben
        """
        self.relitable = relitable
        primAmounts = 0
        keinePrimzahl1, keinePrimzahl2 = True, True
        list1, list2 = [], []
        weiter1a, weiter1b, weiter2a, weiter2b = 0, 0, 0, 0
        proPro, contraContra = {}, {}

        if "primzahlkreuzprocontra" in generatedBefehle:
            dreli = deepcopy(self.relitable)
            headline: str = "Gegen / pro: Nach Rechenregeln auf Primzahlkreuz und Vielfachern von Primzahlen"

            for num, cols in zip_longest(
                range(0, self.tables.lastLineNumber + 1), dreli
            ):
                if num == 0:
                    into: list = [headline]
                else:
                    into: list = []
                if couldBePrimeNumberPrimzahlkreuz(num):
                    primAmounts += 1
                if primCreativity(num) == 1 or num == 1:

                    if couldBePrimeNumberPrimzahlkreuz_fuer_innen(num):
                        # print(str(num) + ": pro innen")
                        list1 += [num]
                        if num > 16:
                            if keinePrimzahl1:
                                gegen = list2[weiter1b + 1]
                                weiter1b += 1
                            else:
                                gegen = list1[weiter1a]
                                weiter1a += 1
                            contraContra[num] = gegen
                            into += ["gegen " + str(gegen)]
                        elif num in (11, 5):
                            if num == 5:
                                gegen = 2
                            elif num == 11:
                                gegen = 3
                            contraContra[num] = gegen
                            into += ["gegen " + str(gegen)]

                        keinePrimzahl1 = False

                    if num in (2, 3):
                        if num == 2:
                            pro = 3
                        elif num == 3:
                            pro = 2
                        proPro[num] = pro
                        into += ["pro " + str(pro)]

                    if couldBePrimeNumberPrimzahlkreuz_fuer_aussen(num):
                        # print(str(num) + ": pro außen")
                        list2 += [num]
                        if num > 16:
                            if keinePrimzahl2:
                                pro = list1[weiter2b + 1]
                                weiter2b += 1
                            else:
                                pro = list2[weiter2a]
                                weiter2a += 1
                            proPro[num] = pro
                            into += ["pro " + str(pro)]
                        elif num in (7, 13):
                            if num == 7:
                                pro = 2
                            elif num == 13:
                                pro = 3
                            proPro[num] = pro
                            into += ["pro " + str(pro)]

                        keinePrimzahl2 = False
                else:
                    if couldBePrimeNumberPrimzahlkreuz_fuer_innen(num):
                        keinePrimzahl1 = True
                    elif couldBePrimeNumberPrimzahlkreuz_fuer_aussen(num):
                        keinePrimzahl2 = True

                    menge: set = set()
                    for couple in primMultiple(num):
                        couple = list(couple)
                        couple.sort()
                        menge |= {tuple(couple)}
                    paare = list(menge)

                    for couple in paare:
                        if primCreativity(couple[1]) == 1:
                            flagX = True
                        elif primCreativity(couple[0]) == 1:
                            flagX = True
                            couple = (couple[1], couple[0])
                        else:
                            flagX = False

                        if flagX:
                            for firstOrSecond in (
                                (1, 0) if couple[0] != couple[1] else (1,)
                            ):
                                if couldBePrimeNumberPrimzahlkreuz_fuer_innen(
                                    couple[firstOrSecond]
                                ):
                                    try:
                                        gegen3 = int(
                                            couple[0 if firstOrSecond == 1 else 1]
                                            * contraContra[couple[firstOrSecond]]
                                        )
                                        contraContra[num] = gegen3
                                        into += ["gegen " + str(gegen3)]
                                    except KeyError:
                                        pass
                                elif (
                                    couldBePrimeNumberPrimzahlkreuz_fuer_aussen(
                                        couple[1]
                                    )
                                    or couple[0] % 2 == 0
                                    or couple[0] % 3 == 0
                                    or couple[1] % 2 == 0
                                    or couple[1] % 3 == 0
                                ):
                                    try:
                                        pro3 = (
                                            int(couple[0 if firstOrSecond == 1 else 0])
                                            * proPro[couple[firstOrSecond]]
                                        )
                                        proPro[num] = pro3
                                        into += ["pro " + str(pro3)]
                                    except KeyError:
                                        pass

                # if self.tables.lastLineNumber >= num:
                try:
                    # print(str(num))
                    text = cols[206]
                    if len(text) > 0:
                        into += [text]
                    self.relitable[num] += (
                        [" | ".join(tuple(set(into)))] if len(into) > 0 else [""]
                    )
                except (KeyError, TypeError):
                    pass

            rowsAsNumbers |= {len(self.relitable[0]) - 1, len(self.relitable[0])}
            self.tables.generatedSpaltenParameter_Tags[
                len(rowsAsNumbers) - 1
            ] = frozenset({ST.sternPolygon, ST.universum})
            self.tables.generatedSpaltenParameter_Tags[len(rowsAsNumbers)] = frozenset(
                {ST.sternPolygon, ST.universum}
            )

            assert not (
                len(self.tables.generatedSpaltenParameter)
                + self.tables.SpaltenVanillaAmount
                in self.tables.generatedSpaltenParameter
            )

            kette = [[("Bedeutung", "Primzahlkreuz_pro_contra")]]
            self.tables.generatedSpaltenParameter[
                len(self.tables.generatedSpaltenParameter)
                + self.tables.SpaltenVanillaAmount
            ] = kette
            self.tables.generatedSpaltenParameter[
                len(self.tables.generatedSpaltenParameter)
                + self.tables.SpaltenVanillaAmount
            ] = kette

            reverseContra: dict = {}
            for key, value in contraContra.items():
                try:
                    reverseContra[value] |= {key}
                except KeyError:
                    reverseContra[value] = {key}
            reversePro: dict = {}
            for key, value in proPro.items():
                try:
                    reversePro[value] |= {key}
                except KeyError:
                    reversePro[value] = {key}

            pro2: list
            contra2: list
            kette2: list
            for num, cols in enumerate(dreli[: self.tables.lastLineNumber + 1]):
                try:
                    pro2 = list(reversePro[num])
                except KeyError:
                    pro2 = []
                try:
                    contra2 = list(reverseContra[num])
                except KeyError:
                    contra2 = []

                if num == 0:
                    kette2 = [headline]
                elif contra2 != [] or pro2 != []:

                    dahinter1a = (
                        dreli[c][206] if c <= self.tables.lastLineNumber else ""
                        for c in pro2
                    )
                    dahinter1b = []
                    for a in dahinter1a:
                        if len(a) > 0:
                            dahinter1b += [a]
                    dahinter1: str = " , ".join(dahinter1b)

                    dahinter2a = (
                        dreli[c][206] if c <= self.tables.lastLineNumber else ""
                        for c in contra2
                    )
                    dahinter2b = []
                    for a in dahinter2a:
                        if len(a) > 0:
                            dahinter2b += [a]
                    dahinter2: str = ", ".join(dahinter2b)

                    dahinter1len: int = len(dahinter1)
                    dahinter2len: int = len(dahinter2)

                    kette2 = [
                        "pro dieser Zahl sind: "
                        if len(pro2) > 1
                        else "pro dieser Zahl ist "
                        if len(pro2) == 1
                        else "",
                        str(pro2)[1:-1],
                        " (" if dahinter1len > 0 else "",
                        dahinter1,
                        ")" if dahinter1len > 0 else "",
                        " | " if len(pro2) > 0 and len(contra2) > 0 else "",
                        " contra dieser Zahl sind: "
                        if len(contra2) > 1
                        else " contra dieser Zahl ist "
                        if len(contra2) == 1
                        else "",
                        str(contra2)[1:-1],
                        " (" if dahinter2len > 0 else "",
                        dahinter2,
                        ")" if dahinter2len > 0 else "",
                    ]
                else:
                    kette2 = [
                        "-",
                    ]

                self.relitable[num] += ["".join(kette2)]

        return self.relitable, rowsAsNumbers

    def concat1RowPrimUniverse2(
        self,
        relitable: list,
        rowsAsNumbers: set,
        generatedBefehle: set,
        htmlTagParaClassWoerter: list,
    ) -> tuple:
        """Fügt eine Spalte ein, in der Primzahlen mit Vielfachern
        auf dem Niveau des Universums nicht einfach nur aus einer
        CSV Tabelle geladen werden, sondern durch Primzahlen und
        deren Vielfachern generiert werden.

        @type relitable: list
        @param relitable: Haupttabelle self.relitable
        @return: relitable + weitere Tabelle daneben
        """
        self.relitable = relitable
        # x("TZJ", htmlTagParaClassWoerter)

        hardCodedCouple = (10, 42)
        transzendentalienNrezi = (5, 131)
        if len(generatedBefehle) > 0:
            # self.tables.primUniverseRowNum = len(self.relitable[0])
            # self.tables.generatedSpaltenParameter_Tags[len(rowsAsNumbers)] = frozenset(
            #    {ST.sternPolygon, ST.galaxie}
            # )
            forGeneratedSpaltenParameter_Tags: dict = {
                "primMotivSternGebr": (
                    (0, 0, frozenset({ST.sternPolygon, ST.galaxie}), 1),
                    (0, 1, frozenset({ST.sternPolygon, ST.galaxie, ST.universum}), 1),
                    (0, 2, frozenset({ST.sternPolygon, ST.galaxie, ST.universum}), 1),
                ),
                "primStrukSternGebr": (
                    (0, 1, frozenset({ST.sternPolygon, ST.galaxie, ST.universum}), 1),
                    (0, 2, frozenset({ST.sternPolygon, ST.galaxie, ST.universum}), 1),
                    (0, 3, frozenset({ST.sternPolygon, ST.universum}), 1),
                ),
                "primMotivGleichfGebr": (
                    (1, 0, frozenset({ST.gleichfoermigesPolygon, ST.galaxie}), 1),
                    (
                        1,
                        1,
                        frozenset(
                            {ST.gleichfoermigesPolygon, ST.galaxie, ST.universum}
                        ),
                        1,
                    ),
                    (
                        1,
                        2,
                        frozenset(
                            {ST.gleichfoermigesPolygon, ST.galaxie, ST.universum}
                        ),
                        1,
                    ),
                ),
                "primStrukGleichfGebr": (
                    (
                        1,
                        1,
                        frozenset(
                            {ST.gleichfoermigesPolygon, ST.galaxie, ST.universum}
                        ),
                        1,
                    ),
                    (
                        1,
                        2,
                        frozenset(
                            {ST.gleichfoermigesPolygon, ST.galaxie, ST.universum}
                        ),
                        1,
                    ),
                    (1, 3, frozenset({ST.gleichfoermigesPolygon, ST.universum}), 1),
                ),
                "primMotivStern": (
                    (0, 0, frozenset({ST.sternPolygon, ST.galaxie}), 0),
                    (0, 1, frozenset({ST.sternPolygon, ST.galaxie, ST.universum}), 0),
                    (0, 2, frozenset({ST.sternPolygon, ST.galaxie, ST.universum}), 0),
                ),
                "primStrukStern": (
                    (0, 1, frozenset({ST.sternPolygon, ST.galaxie, ST.universum}), 0),
                    (0, 2, frozenset({ST.sternPolygon, ST.galaxie, ST.universum}), 0),
                    (0, 3, frozenset({ST.sternPolygon, ST.universum}), 0),
                ),
                "primMotivGleichf": (
                    (1, 0, frozenset({ST.gleichfoermigesPolygon, ST.galaxie}), 0),
                    (
                        1,
                        1,
                        frozenset(
                            {ST.gleichfoermigesPolygon, ST.galaxie, ST.universum}
                        ),
                        0,
                    ),
                    (
                        1,
                        2,
                        frozenset(
                            {ST.gleichfoermigesPolygon, ST.galaxie, ST.universum}
                        ),
                        0,
                    ),
                ),
                "primStrukGleichf": (
                    (
                        1,
                        1,
                        frozenset(
                            {ST.gleichfoermigesPolygon, ST.galaxie, ST.universum}
                        ),
                        0,
                    ),
                    (
                        1,
                        2,
                        frozenset(
                            {ST.gleichfoermigesPolygon, ST.galaxie, ST.universum}
                        ),
                        0,
                    ),
                    (1, 3, frozenset({ST.gleichfoermigesPolygon, ST.universum}), 0),
                ),
            }
            uni_ = (5, 131)
            gal_ = (10, 42)
            GalOrUni_nOrInvers = {
                0: (gal_, gal_),
                1: (gal_, uni_),
                2: (uni_, gal_),
                3: (uni_, uni_),
            }

            self.gebrRatAllCombis = self.findAllBruecheAndTheirCombinations()
            kombis2: dict = {"mul": {}, "div": {}}
            kombis1 = {"stern": deepcopy(kombis2), "gleichf": deepcopy(kombis2)}
            # self.gebrRatAllCombis = {
            alleFractionErgebnisse2: dict = {
                "UniUni": deepcopy(kombis1),
                "UniGal": deepcopy(kombis1),
                "GalUni": deepcopy(kombis1),
                "GalGal": deepcopy(kombis1),
            }

            for KeyGalUniUniGal, ValueSternOrGleichf in self.gebrRatAllCombis.items():
                for KeySternOrGleichf, ValueMulOrDiv in ValueSternOrGleichf.items():
                    for KeyMulOrDiv, Couples in ValueMulOrDiv.items():

                        alleFractionErgebnisse2[KeyGalUniUniGal][KeySternOrGleichf][
                            KeyMulOrDiv
                        ] = (
                            self.combineDicts(
                                self.convertSetOfPaarenToDictOfNumToPaareMul(
                                    Couples,
                                    True if KeySternOrGleichf == "gleichf" else False,
                                ),
                                self.convertFractionsToDictOfNumToPaareOfMulOfIntAndFraction(
                                    self.BruecheUni
                                    if KeyGalUniUniGal[:3] == "Uni"
                                    else self.BruecheGal,
                                    self.BruecheUni
                                    if KeyGalUniUniGal[3:] == "Uni"
                                    else self.BruecheGal,
                                    True if KeySternOrGleichf == "gleichf" else False,
                                ),
                            )
                            if KeyMulOrDiv == "mul"
                            else self.combineDicts(
                                self.convertSetOfPaarenToDictOfNumToPaareDiv(
                                    Couples,
                                    True if KeySternOrGleichf == "gleichf" else False,
                                ),
                                defaultdict(set),
                            )
                        )

            # hier geht es um die html class Parameter und um Tagging ob Galaxie oder Polygon
            koord2tag, koord2ParameterA, koord2Parameter = {}, {}, {}

            for name, mehrereEinraege in forGeneratedSpaltenParameter_Tags.items():
                for drei in mehrereEinraege:
                    try:
                        koord2tag[(drei[0], drei[1], drei[3])] |= {drei[2]}
                    except KeyError:
                        koord2tag[(drei[0], drei[1], drei[3])] = {drei[2]}
                for befehl in generatedBefehle:
                    # x("BSA", [befehl, name])
                    if (
                        name == befehl
                    ):  # ob der Befehl des Users mit den jeweils vorhandenen übereinstimmt
                        for drei in mehrereEinraege:
                            # x("VGA", drei)
                            try:
                                koord2ParameterA[(drei[0], drei[1], drei[3])] |= {
                                    befehl
                                }
                            except KeyError:
                                koord2ParameterA[(drei[0], drei[1], drei[3])] = {befehl}

            for key, value in koord2tag.items():
                assert len(value) == 1
            for key, value in koord2ParameterA.items():
                koord2Parameter[key] = list(value)

            # stern vs gleichf:
            self.transzendentalien: dict = {
                "Sternpolygone": [],
                "gleichförmige Polygone": [],
            }

            relitableCopy = deepcopy(self.relitable[: self.tables.lastLineNumber + 1])
            kombisNamen: tuple = (
                "Motiv -> Motiv",
                "Motiv -> Strukur",
                "Struktur -> Motiv",
                "Struktur -> Strukur",
            )
            kombisNamen2: tuple = (
                "GalGal",
                "GalUni",
                "UniGal",
                "UniUni",
            )

            # self.rolle = []
            self.motivation: dict = {"Sternpolygone": [], "gleichförmige Polygone": []}
            # self.ziel = []
            for zwei, (polytype, polytypename, transzType) in enumerate(
                zip(
                    hardCodedCouple,
                    ["Sternpolygone", "gleichförmige Polygone"],
                    transzendentalienNrezi,
                )
            ):
                for cols in self.relitable:
                    # self.rolle += [cols[19]]
                    self.transzendentalien[polytypename] += [cols[transzType]]
                    self.motivation[polytypename] += [cols[polytype]]
                    # self.ziel += [cols[11]]

            for brr, ganzOrGebr in enumerate(
                ["", ", mit Faktoren aus gebrochen-rationalen Zahlen"]
            ):
                for zwei, (
                    polytype,
                    polytypename,
                    transzType,
                    sternOrGleichf,
                ) in enumerate(
                    zip(
                        hardCodedCouple,
                        ["Sternpolygone", "gleichförmige Polygone"],
                        transzendentalienNrezi,
                        kombis1.keys(),
                    )
                ):
                    kombi_ = []

                    # alle Kombis die von strukur oder motiven also 2x2 möglich sind
                    for i, cols in enumerate(self.relitable):
                        kombi_ += [
                            (
                                (
                                    self.motivation[polytypename][i],
                                    self.motivation[polytypename][i],
                                ),
                                (
                                    self.motivation[polytypename][i],
                                    self.transzendentalien[polytypename][i],
                                ),
                                (
                                    self.transzendentalien[polytypename][i],
                                    self.motivation[polytypename][i],
                                ),
                                (
                                    self.transzendentalien[polytypename][i],
                                    self.transzendentalien[polytypename][i],
                                ),
                            )
                        ]
                    kombis: tuple = tuple(kombi_)
                    # alle 2x2 kombis von motiven und struktur

                    for nullBisDrei, (kombiUeberschrift, GalUniKombis) in enumerate(
                        zip(kombisNamen, kombisNamen2)
                    ):
                        tag: frozenset = list(koord2tag[(zwei, nullBisDrei, brr)])[0]

                        self.tables.generatedSpaltenParameter_Tags[
                            len(rowsAsNumbers)
                        ] = tag
                        rowsAsNumbers |= {
                            len(self.relitable[0]),
                        }
                        # x("HJM", len(self.relitable[0]))
                        if (zwei, nullBisDrei, brr) in koord2Parameter:
                            for i, cols in enumerate(relitableCopy):
                                if i == 0:
                                    into = [
                                        "generierte Multiplikationen ",
                                        polytypename,
                                        " ",
                                        kombiUeberschrift,
                                        ganzOrGebr,
                                    ]
                                    # x("GSJ", "".join(into))
                                else:
                                    into = []
                                    if self.tables.htmlOutputYes:
                                        into += ["<ul>"]
                                    elif self.tables.bbcodeOutputYes:
                                        into += ["[list]"]
                                    if brr == 0:
                                        multipless = multiples(i)
                                        for k, multi in enumerate(multipless):
                                            if (
                                                k > 0
                                                and not self.tables.htmlOutputYes
                                                and not self.tables.bbcodeOutputYes
                                            ):
                                                into += [", außerdem: "]
                                            into += [
                                                "<li>"
                                                if self.tables.htmlOutputYes
                                                else "[*]"
                                                if self.tables.bbcodeOutputYes
                                                else "",
                                                "(",
                                                kombis[multi[0]][nullBisDrei][0]
                                                if len(
                                                    kombis[multi[0]][nullBisDrei][
                                                        0
                                                    ].strip()
                                                )
                                                > 3
                                                else "...",
                                                ") * (",
                                                kombis[multi[1]][nullBisDrei][1]
                                                if len(
                                                    kombis[multi[1]][nullBisDrei][
                                                        1
                                                    ].strip()
                                                )
                                                > 3
                                                else "...",
                                                ")",
                                                "</li>"
                                                if self.tables.htmlOutputYes
                                                else "",
                                            ]
                                    elif brr == 1:
                                        multipless = alleFractionErgebnisse2[
                                            GalUniKombis
                                        ][sternOrGleichf]["mul"]
                                        # x("HFG", multipless.items())
                                        for k, multi in enumerate(
                                            zip_longest(
                                                multipless[i],
                                                fillvalue="",
                                            )
                                        ):
                                            multi = multi[0]
                                            try:
                                                multi[0]
                                                multi[1]
                                            except:
                                                continue

                                            # alxp("BBB")

                                            # x("HIX", [multi1, multi2])
                                            von = self.spalteMetaKonkretTheorieAbstrakt_getGebrRatUnivStrukturalie(
                                                multi[0],
                                                GalOrUni_nOrInvers[nullBisDrei][zwei],
                                                self.readOneCSVAndReturn(
                                                    2 if nullBisDrei in (2, 3) else 3
                                                ),
                                                False
                                                if nullBisDrei in (2, 3)
                                                else True,
                                            )
                                            # alxp("BBB2")
                                            bis = self.spalteMetaKonkretTheorieAbstrakt_getGebrRatUnivStrukturalie(
                                                multi[1],
                                                GalOrUni_nOrInvers[nullBisDrei][zwei],
                                                self.readOneCSVAndReturn(
                                                    2 if nullBisDrei in (1, 3) else 3
                                                ),
                                                False
                                                if nullBisDrei in (1, 3)
                                                else True,
                                            )

                                            if von is not None and bis is not None:
                                                von = von.strip()
                                                bis = bis.strip()
                                                if len(von) > 3 and len(bis) > 3:
                                                    if (
                                                        k > 0
                                                        and not self.tables.htmlOutputYes
                                                        and not self.tables.bbcodeOutputYes
                                                        and len(into) > 0
                                                    ):
                                                        into += ["| außerdem: "]
                                                    into += [
                                                        "<li>"
                                                        if self.tables.htmlOutputYes
                                                        else "[*]"
                                                        if self.tables.bbcodeOutputYes
                                                        else "" '"',
                                                        von,
                                                        # self.CSVsAlreadRead[place][
                                                        #    multi[0].numerator - 1
                                                        # ][multi[0].denominator - 1],
                                                        '"',
                                                        "<br>"
                                                        if self.tables.htmlOutputYes
                                                        and (
                                                            len(von) > 30
                                                            or len(bis) > 30
                                                        )
                                                        else " ",
                                                        " (",
                                                        str(multi[0]),
                                                        ")",
                                                        "*",
                                                        "(",
                                                        str(multi[1]),
                                                        ")",
                                                        "<br>"
                                                        if self.tables.htmlOutputYes
                                                        and (
                                                            len(von) > 30
                                                            or len(bis) > 30
                                                        )
                                                        else " ",
                                                        ' "',
                                                        bis,
                                                        # self.CSVsAlreadRead[place][
                                                        #    multi[1].numerator - 1
                                                        # ][multi[1].denominator - 1],
                                                        '"',
                                                        "</li>"
                                                        if self.tables.htmlOutputYes
                                                        else "",
                                                    ]
                                    if self.tables.htmlOutputYes:
                                        into += ["</ul>"]
                                    elif self.tables.bbcodeOutputYes:
                                        into += ["[/list]"]

                                self.relitable[i] += ["".join(into)]

                            if (
                                len(self.tables.generatedSpaltenParameter)
                                + self.tables.SpaltenVanillaAmount
                                in self.tables.generatedSpaltenParameter
                            ):
                                raise ValueError
                            kette = (
                                [
                                    (
                                        "Multiplikationen",
                                        htmlTagParaClassWoerter[para][0][0][0][1],
                                    )
                                ]
                                for para in koord2Parameter[(zwei, nullBisDrei, brr)]
                            )
                            if (
                                "primMotivStern"
                                in koord2Parameter[(zwei, nullBisDrei, brr)]
                            ):
                                kette = list(kette) + [
                                    [("Wichtigstes_zum_verstehen", "Viertwichtigste")]
                                ]

                            self.tables.generatedSpaltenParameter[
                                len(self.tables.generatedSpaltenParameter)
                                + self.tables.SpaltenVanillaAmount
                            ] = tuple(kette)

        return self.relitable, rowsAsNumbers

    def spalteMetaKontretTheorieAbstrakt_etc_1(
        self, relitable: list, rowsAsNumbers: set, geordnetePaare: set
    ):
        self.relitable = relitable
        self.rowsAsNumbers = rowsAsNumbers
        if len(geordnetePaare) > 0:
            self.gebrUnivTable4metaKonkret = self.readOneCSVAndReturn(2)
        for paar in tuple(geordnetePaare):
            self.spalteMetaKontretTheorieAbstrakt_etc(
                relitable,
                rowsAsNumbers,
                paar[0],
                1 if paar[1] == 0 else 2 if paar[1] == 1 else 3,
            )
        return self.relitable, self.rowsAsNumbers

    def spalteMetaKonkretAbstrakt_isGanzZahlig(self, zahl, spaltenWahl) -> bool:
        zahl = (1 / zahl) if spaltenWahl else zahl
        zahl %= 1
        if zahl < 0.00001 or zahl > 0.99999:
            return True
        else:
            return False

    def spalteMetaKontretTheorieAbstrakt_etc(
        self,
        relitable: list,
        rowsAsNumbers: set,
        metavariable: int = 2,
        lower1greater2both3: int = 3,
    ) -> tuple:
        """
        1. nächste Zeile wird Anzeigezeile
        2. Diese Zeile erhält die Tags
        3. Vorwörternamen in Struktur: z.B. Meta-
        4. for alle Strukturalien und inverse Strukturalien
        5. ob diese beiden oder eins der beiden
        6. Überschriften und Tags: Schritt 1. und 2. in Schleife noch mal. <s>Dann ist doch das erste bei beiden schon eins zu viel!</s>
        7. Haupttabelle erhält schon direkt die Überschriften
        <s>8. Da waren 3 Zeilen Unsinn Code</s>

        9. for zeile 2 bis Unten und mit i++
        9. a) Vorwörter werden bestimmt
        9. a) 1. startet mit (zahl1,zahl1) und die eine wird dann immer größer und die andere kleiner
        9. a) 2. Fkt switching verdoppelt und halbiert (wenn Zahl 2) und wählt die spalte, ob strukturalie oder reziproke strukturalie
        9. a) 3. Fkt makeVorwort macht die Wiederholungen eines solchen Vorwortes
        9. a) 4.

        9. b) Text kommt in Zelle
        9. b) 1. wenn Ursprungszelle etwas enthält
        9. b) 2. Vorwörter, dann Transzendentalie, dann Zahl dazu in Klammern
        9. b) 3. das insofern in Schleife, dass mehreres Sowas in eine Zelle kann mit "|" dazwischen

        10. HTML Paramter werden aus dem dataDict genommen, damit sie für die html ausgabe genutzt werden können.

        Wie mache ich gebr rat univ rein?
        1. bei (zahl1,noch mal zahl1) bzw. (i,i) msste ich schauen, wenn ein wert None werden würde, weil er nicht mehr ganzzahlig wäre
        2. dann ein if für diesen fall und else wie gehabt.
        3. im if fall die komma zahl bestimmen
        4. die kommazahl als rationalen bruch maximal vereinfachen mit rational zahl lib von python
        5. Vorwörter weiter spinnen lassen, aber schauen, dass es richtig gemacht wird
        5. a) dafür brauche ich eine iterator variable extra noch mal zur Kommazahl
        6. aus dem rechteck der großen tabelle mit den richtigen koordinaten das universum-wort raus nehmen

        Alle Schleifen ineinander noch mal
        for zeilen in 4 spalten aus 2 echten spalten, also beim zweiten mal verdreht, so dass es 4 sind
        darin

        for nur meta nur konkret oder beides auf ein mal
        darin funktion mainpart und funktion html parameter; mainpart:

        for relitable zeile 2, d.h. der nummer 2, d.h. überschrift und nummer 1 wird ausgelassen
        darin fkt 1. vorwortbehandlung 2. fkt insert texte; 1. vorwortbehandlung:

        wiederhole bis beides None ist, also meta hochzählen und konkret runter zählen
        2. fkt insert:

        for sammlung von variablen: hochzähl- und runterzählvariable, spalte - entweder strukturalie oder reziproke davon, und vorwörter

        darin if bedingungen: ob spalte strukturalie oder reziproke strukturalie
        """

        self.relitable = relitable
        # rowsAsNumbers |= {
        #    len(self.relitable[0]),
        # }
        # self.tables.generatedSpaltenParameter_Tags[len(rowsAsNumbers) - 1] = frozenset(
        #    {ST.sternPolygon, ST.universum}
        # )
        """bis hier hin waren es die Vorinitialisierungen von Variablen"""

        # def switching(metavariable: int, lower1greater2both3: int, row: int):
        def switching(newCol: int, moreAndLess: tuple) -> tuple:
            """2 neue Koordinaten der Tabelle durch 3 Parameter, d.h. einer, newCol, gilt für beide
            Immer eine halbierung und dopplung oder verdreifachung und ..., etc.
            und wechsel der Spalte von den 2 Spalten"""
            # x("MORE", moreAndLess)
            spaltenWahl: int
            newCol, spaltenWahl = (
                (self.transzendentalienSpalten[0], 0)
                if newCol == self.transzendentalienSpalten[1]
                else (self.transzendentalienSpalten[1], 1)
            )
            try:
                mulresult = moreAndLess[0] * metavariable
            except:
                pass
            a = (
                mulresult
                if not moreAndLess[0] is None and mulresult < len(relitable)
                # würde zu früh abbrechen and len((relitable[moreAndLess[0] * metavariable][newCol]).strip()) > 3
                else None
            )
            if (
                moreAndLess[1] is not None
                and moreAndLess[1] < 100
                and moreAndLess[1] > 0.01
            ):
                divresult = moreAndLess[1] / metavariable
                # alxp("a " + str(divresult))

                if (
                    newCol == self.transzendentalienSpalten[ifInvers]
                    and type(moreAndLess[1]) is not Fraction
                ):
                    moreAndLess = (moreAndLess[0], Fraction(1, moreAndLess[1]))

                b = (
                    Fraction(metavariable, moreAndLess[1])
                    if self.spalteMetaKonkretAbstrakt_isGanzZahlig(
                        moreAndLess[1], False
                    )
                    else Fraction(1, moreAndLess[1]) / Fraction(metavariable)
                )

                # b = (
                #    (
                #        int(divresult)
                #        if self.spalteMetaKonkretAbstrakt_isGanzZahlig(divresult, False)
                #        else (
                #            Fraction(metavariable, moreAndLess[1])
                #            # Fraction(1, moreAndLess[1]) * Fraction(metavariable)
                #            if self.spalteMetaKonkretAbstrakt_isGanzZahlig(
                #                moreAndLess[1], False
                #            )
                #            # else Fraction(moreAndLess[1] * metavariable)
                #            else Fraction(1, moreAndLess[1]) / Fraction(metavariable)
                #        )
                #    )
                #    if newCol != self.transzendentalienSpalten[ifInvers]
                #    and not self.spalteMetaKonkretAbstrakt_isGanzZahlig(
                #        moreAndLess[1], True
                #    )
                #    else Fraction(moreAndLess[1], metavariable)
                # )

            else:
                # alxp("c1 None")
                b = None
            # alxp("b " + str(b))
            # if newCol == self.transzendentalienSpalten[ifInvers]:
            #    b = 11

            if b is not None:
                if Fraction(b) in self.gebrRatEtwaSchonMalDabeiGewesen:
                    # alxp("c2 None")
                    b = None
                else:
                    self.gebrRatEtwaSchonMalDabeiGewesen |= {Fraction(b)}

            moreAndLess = (a, b)

            return newCol, moreAndLess

        metaOrWhat = {
            2: (("Meta-Thema: ", "Konkretes: "), ("Meta-", "Konkret-")),
            3: (("Theorie-Thema: ", "Praxis: "), ("Theorie-", "Praxis-")),
            4: (
                ("Management-Thema: ", "Veränderungs-Thema: "),
                ("Management-", "Veränderung-"),
            ),
            5: (
                ("Ganzheitlich-Thema: ", "darüber-hinausgehend-: "),
                ("ganzheitlich-", "darüber-hinausgehend-"),
            ),
            6: (
                ("Unternehmung: ", "Wert-Thema: "),
                ("unternehmend-", "Wert-"),
            ),
            7: (
                ("Beherrschung: ", "Richtung-Thema: "),
                ("beherrschend-", "Richtung-"),
            ),
        }

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
        self.struktAndInversSpalten: tuple = (5, 131)

        for ifInvers, self.transzendentalienSpalten in enumerate(
            (
                self.struktAndInversSpalten,
                (self.struktAndInversSpalten[1], self.struktAndInversSpalten[0]),
            )
        ):
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
                rowsAsNumbers = self.spalteMetaKonkretTheorieAbstrakt_mainPart(
                    bothRows,
                    ifInvers,
                    makeVorwort,
                    metaOrWhat,
                    metavariable,
                    relitable,
                    rowsAsNumbers,
                    switching,
                    self.transzendentalienSpalten,
                )

                self.spalteMetaKonkretTheorieAbstrakt_SetHtmlParameters(
                    lower1greater2both3, metavariable
                )

        # x("r_wt", self.tables.generatedSpaltenParameter)
        return self.relitable, rowsAsNumbers

    def spalteMetaKonkretTheorieAbstrakt_SetHtmlParameters(
        self, lower1greater2both3, metavariable
    ):
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

    def spalteMetaKonkretTheorieAbstrakt_mainPart(
        self,
        bothRows,
        ifInvers,
        makeVorwort,
        metaOrWhat,
        metavariable,
        relitable,
        rowsAsNumbers,
        switching,
        transzendentalienSpalten,
    ):
        rowsAsNumbers = self.spalteMetaKonkretAbstrakt_UeberschriftenUndTags(
            bothRows, ifInvers, metavariable, rowsAsNumbers
        )

        self.transzendentalienSpalten = transzendentalienSpalten
        # for i, row in enumerate(relitable[2:], 2):
        #    moreAndLess = (i, i)  # 1. wert "*2" und 2. "/3"
        #    neue2KoordNeue2Vorwoerter: list = []
        for i, row in enumerate(relitable[2 : self.tables.lastLineNumber + 1], 2):
            self.gebrRatEtwaSchonMalDabeiGewesen = set()
            moreAndLess = (i, i)  # 1. wert "*2" und 2. "/3"
            neue2KoordNeue2Vorwoerter: list = []
            # alxp("new while")
            newCol = self.transzendentalienSpalten[0]
            neue2KoordNeue2Vorwoerter = (
                self.spalteMetaKonkretTheorieAbstrakt_VorwortBehandlungWieVorwortMeta(
                    makeVorwort,
                    metaOrWhat,
                    metavariable,
                    moreAndLess,
                    neue2KoordNeue2Vorwoerter,
                    newCol,
                    switching,
                )
            )

            self.spalteMetaKonkretTheorieAbstrakt_mainPart_InsertingText(
                bothRows,
                i,
                ifInvers,
                neue2KoordNeue2Vorwoerter,
                relitable,
                self.transzendentalienSpalten,
            )
        return rowsAsNumbers

    def spalteMetaKonkretTheorieAbstrakt_VorwortBehandlungWieVorwortMeta(
        self,
        makeVorwort,
        metaOrWhat,
        metavariable,
        moreAndLess,
        neue2KoordNeue2Vorwoerter,
        newCol,
        switching,
    ):
        while not (moreAndLess[0] is None and moreAndLess[1] is None):
            newCol, moreAndLess = switching(newCol, moreAndLess)
            # if type(moreAndLess[1]) is Fraction and moreAndLess[1] is not None:
            #    gebrStrukWort = (
            #        self.spalteMetaKonkretTheorieAbstrakt_getGebrRatUnivStrukturalie(
            #            moreAndLess[1]
            #        )
            #    )
            #    if gebrStrukWort is None or len(gebrStrukWort.strip()) < 4:
            #        moreAndLess = (moreAndLess[0], None)
            #        if moreAndLess[0] is None and moreAndLess[1] is None:
            #            break
            vorworte2 = metaOrWhat[metavariable][
                0 if len(neue2KoordNeue2Vorwoerter) == 0 else 1
            ]
            vorwort1: str = makeVorwort(
                len(neue2KoordNeue2Vorwoerter) + 1, vorworte2, 1
            )
            vorwort2: str = makeVorwort(
                len(neue2KoordNeue2Vorwoerter) + 1, vorworte2, 2
            )
            neue2KoordNeue2Vorwoerter += [(moreAndLess, newCol, vorwort1, vorwort2)]
        return neue2KoordNeue2Vorwoerter

    def spalteMetaKonkretTheorieAbstrakt_mainPart_InsertingText(
        self,
        bothRows,
        i,
        ifInvers,
        neue2KoordNeue2Vorwoerter,
        relitable,
        transzendentalienSpalten,
    ):
        intoList = []
        thema = ""
        self.transzendentalienSpalten = transzendentalienSpalten

        for vier in neue2KoordNeue2Vorwoerter[:-1]:
            if (
                bothRows == 0  # bei meta aber nicht bei konkret
                and not vier[0][0] is None
                and len(relitable[vier[0][0]][vier[1]].strip()) > 3
                # and False
            ):
                intoList += [
                    "<li>"
                    if self.tables.htmlOutputYes
                    else "[*]"
                    if self.tables.bbcodeOutputYes
                    else "",
                    vier[bothRows + 2],
                    thema,
                    relitable[vier[0][0]][vier[1]],
                    " (",
                    "1/"
                    if vier[1] != self.transzendentalienSpalten[ifInvers]
                    and vier[0][1] != 1
                    else "",
                    str(vier[0][0]),
                    ")",
                    "</li>"
                    if self.tables.htmlOutputYes
                    else " | "
                    if not self.tables.bbcodeOutputYes
                    else "",
                ]
            elif (
                bothRows == 1  # bei konkret aber nicht meta
                and not vier[0][1] is None
                and not type(vier[0][1]) is Fraction
                and len(relitable[vier[0][1]][vier[1]].strip()) > 3
                # and False
            ):
                intoList += [
                    "<li>"
                    if self.tables.htmlOutputYes
                    else "[*]"
                    if self.tables.bbcodeOutputYes
                    else "",
                    vier[bothRows + 2],
                    thema,
                    relitable[vier[0][1]][vier[1]],
                    " (",
                    "1/"
                    if vier[1] != self.transzendentalienSpalten[ifInvers]
                    and vier[0][1] != 1
                    else "",
                    str(vier[0][1]),
                    ")",
                    "</li>"
                    if self.tables.htmlOutputYes
                    else " | "
                    if not self.tables.bbcodeOutputYes
                    else "",
                ]
            elif (
                bothRows == 1  # bei konkret aber nicht meta
                and not vier[0][1] is None
                and type(vier[0][1]) is Fraction
                # and False
                # and self.struktAndInversSpalten == transzendentalienSpalten
            ):

                # alxp("CCC")
                gebrStrukWort = (
                    self.spalteMetaKonkretTheorieAbstrakt_getGebrRatUnivStrukturalie(
                        vier[0][1],
                        self.struktAndInversSpalten,
                        self.gebrUnivTable4metaKonkret,
                    )
                )
                if gebrStrukWort is not None:
                    if len(gebrStrukWort.strip()) > 3:
                        # sys.stderr.write("gebrRatMulStern")
                        intoList += [
                            "<li>"
                            if self.tables.htmlOutputYes
                            else ""
                            if not self.tables.bbcodeOutputYes
                            else "[*]",
                            vier[bothRows + 2],
                            thema,
                            gebrStrukWort,
                            "(",
                            str(vier[0][1].numerator),
                            ("/" + str(vier[0][1].denominator))
                            if vier[0][1].denominator > 1
                            else "",
                            ")",
                            "</li>"
                            if self.tables.htmlOutputYes
                            else " | "
                            if not self.tables.bbcodeOutputYes
                            else "",
                        ]
                    else:
                        pass
                else:
                    pass
                    # sys.stderr.write("gebrRatDivStern")
                    # vier[0][1] = None
                    # vier[0] = (vier[0][0], None)
                    # intoList = [None]
            thema = "Thema: "
        # alxp(intoList)
        self.relitable[i] += [
            "".join(
                (
                    ["<ul>"]
                    if self.tables.htmlOutputYes
                    else [""]
                    if not self.tables.bbcodeOutputYes
                    else ["[list]"]
                )
                + intoList
                + (
                    ["</ul>"]
                    if self.tables.htmlOutputYes
                    else [""]
                    if not self.tables.bbcodeOutputYes
                    else ["[/list]"]
                )
            )
        ]

    def getAllBrueche(self, gebrUnivTable4metaKonkret):
        menge = set()
        for i, a in enumerate(gebrUnivTable4metaKonkret[1:]):
            for k, b in enumerate(a[1:]):
                b = b.strip()
                if len(b) > 3:
                    frac = Fraction(i + 2, k + 2)
                    if frac.denominator != 1 and frac.numerator != 1:
                        menge |= {frac}
        return menge

    def readOneCSVAndReturn(self, wahl) -> list:
        place = self.readConcatCSV_choseCsvFile(wahl)
        if place in self.CSVsAlreadRead:
            return self.CSVsAlreadRead[place]
        else:
            with open(place, mode="r") as csv_file:
                gebrRatTable = list(csv.reader(csv_file, delimiter=";"))
            self.CSVsAlreadRead[place] = gebrRatTable
            if wahl in (2, 4):
                self.BruecheUni = tuple(self.getAllBrueche(gebrRatTable))

            if wahl in (3, 5):
                self.BruecheGal = tuple(self.getAllBrueche(gebrRatTable))

            return gebrRatTable

    def findAllBruecheAndTheirCombinations(self):
        self.readOneCSVAndReturn(2)
        self.readOneCSVAndReturn(3)
        kombis2 = {"mul": set(), "div": set()}
        kombis1 = {"stern": deepcopy(kombis2), "gleichf": deepcopy(kombis2)}
        gebrRatAllCombis = {
            "UniUni": deepcopy(kombis1),
            "UniGal": deepcopy(kombis1),
            "GalUni": deepcopy(kombis1),
            "GalGal": deepcopy(kombis1),
        }

        for brueche1, brueche2, GalOrUni1, GalOrUni2 in zip(
            (self.BruecheGal, self.BruecheGal, self.BruecheUni, self.BruecheUni),
            (self.BruecheGal, self.BruecheUni, self.BruecheGal, self.BruecheUni),
            ("Gal", "Gal", "Uni", "Uni"),
            ("Gal", "Uni", "Gal", "Uni"),
        ):
            # x("DSK", GalOrUni1 + GalOrUni2)
            for BruecheUn in brueche1:
                for BruecheUn2 in brueche2:
                    if BruecheUn != BruecheUn2:

                        couple = {frozenset({BruecheUn, BruecheUn2})}
                        if round(BruecheUn * BruecheUn2) == (BruecheUn * BruecheUn2):
                            gebrRatAllCombis[GalOrUni1 + GalOrUni2]["stern"][
                                "mul"
                            ] |= deepcopy(couple)
                            """
                            x(
                                "SDUG",
                                (
                                    list(list(couple)[0])[0] * list(list(couple)[0])[1],
                                    GalOrUni1 + GalOrUni2,
                                ),
                            )"""
                        if round(BruecheUn / BruecheUn2) == (BruecheUn / BruecheUn2):
                            gebrRatAllCombis[GalOrUni1 + GalOrUni2]["stern"][
                                "div"
                            ] |= deepcopy(couple)

                        if round(1 / (BruecheUn * BruecheUn2)) == (
                            1 / (BruecheUn * BruecheUn2)
                        ):
                            gebrRatAllCombis[GalOrUni1 + GalOrUni2]["gleichf"][
                                "mul"
                            ] |= deepcopy(couple)
                            # x("SDZ", couple)
                        if round(1 / (BruecheUn / BruecheUn2)) == (
                            1 / (BruecheUn / BruecheUn2)
                        ):
                            gebrRatAllCombis[GalOrUni1 + GalOrUni2]["gleichf"][
                                "div"
                            ] |= deepcopy(couple)
        """
        for a in gebrRatAllCombis["UniUni"]["stern"]["mul"]:
            a = list(a)
            a = a[0] * a[1]
            x("FGD", a)
            assert a == round(a)
        """

        # x("XCGH2", gebrRatAllCombis["UniUni"]["stern"]["mul"])
        return gebrRatAllCombis

    def spalteMetaKonkretTheorieAbstrakt_getGebrRatUnivStrukturalie(
        self,
        koord: Fraction,
        n_and_invers_spalten,
        gebrTable4metaKonkretAndMore,
        isGalaxie=False,
    ) -> str:
        if koord.denominator == 0 or koord.numerator == 0:
            return ""
        elif koord.denominator > 100 or koord.numerator > 100:
            return None
        elif koord.numerator == 1:
            if (
                len(self.relitable[koord.denominator][n_and_invers_spalten[1]].strip())
                > 3
            ):
                strukname = (
                    (
                        self.relitable[koord.denominator][n_and_invers_spalten[1]],
                        " (1/",
                        str(koord.denominator),
                        ")",
                        "; "
                        if len(self.relitable[koord.denominator][201]) > 2
                        and not self.tables.htmlOutputYes
                        else "",
                        "<br>"
                        if len(self.relitable[koord.denominator][201]) > 2
                        and self.tables.htmlOutputYes
                        else "",
                        self.relitable[koord.denominator][201],
                    )
                    if not isGalaxie
                    else (self.relitable[koord.denominator][n_and_invers_spalten[1]],)
                )
                return "".join(strukname)
            else:
                return ""
        elif koord.denominator == 1:
            if (
                len(self.relitable[koord.numerator][n_and_invers_spalten[0]].strip())
                > 3
            ):
                strukname = (
                    (
                        self.relitable[koord.numerator][n_and_invers_spalten[0]],
                        " (",
                        str(koord.numerator),
                        ")",
                        "; "
                        if len(self.relitable[koord.numerator][198]) > 2
                        and not self.tables.htmlOutputYes
                        else "",
                        "<br>"
                        if len(self.relitable[koord.numerator][198]) > 2
                        and self.tables.htmlOutputYes
                        else "",
                        self.relitable[koord.numerator][198],
                    )
                    if not isGalaxie
                    else (self.relitable[koord.numerator][n_and_invers_spalten[0]],)
                )
                return "".join(strukname)
            else:
                return ""
        else:
            try:
                return gebrTable4metaKonkretAndMore[koord.numerator - 1][
                    koord.denominator - 1
                ]
            except (KeyError, IndexError):
                return ""

    def spalteMetaKonkretAbstrakt_UeberschriftenUndTags(
        self, bothRows, ifInvers, metavariable, rowsAsNumbers
    ):
        rowsAsNumbers |= {len(self.relitable[0])}
        self.tables.generatedSpaltenParameter_Tags[len(rowsAsNumbers) - 1] = frozenset(
            {ST.sternPolygon, ST.universum}
        )
        self.relitable[1] += [""]
        if bothRows == 0:
            if metavariable == 2:
                self.relitable[0] += ["Meta"]
            if metavariable == 3:
                self.relitable[0] += ["Theorie"]
            if metavariable == 4:
                self.relitable[0] += ["Management"]
            if metavariable == 5:
                self.relitable[0] += ["ganzheitlich"]
            if metavariable == 6:
                self.relitable[0] += ["Verwertung, Unternehmung, Geschäft"]
            if metavariable == 7:
                self.relitable[0] += ["regieren, beherrschen"]
        if bothRows == 1:
            if metavariable == 2:
                self.relitable[0] += ["Konkretes"]
            if metavariable == 3:
                self.relitable[0] += ["Praxis"]
            if metavariable == 4:
                self.relitable[0] += ["verändernd"]
            if metavariable == 5:
                self.relitable[0] += ["darüber hinaus gehend"]
            if metavariable == 6:
                self.relitable[0] += ["wertvoll"]
            if metavariable == 7:
                self.relitable[0] += ["Richtung"]
        self.relitable[0][-1] += " für 1/n statt n" if ifInvers == 1 else " für n"
        return rowsAsNumbers

    def spalteFuerGegenInnenAussenSeitlichPrim(
        self, relitable: list, rowsAsNumbers: set
    ) -> tuple:
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
                return "für außen"
            else:
                return ""

        self.relitable = relitable
        # extraSpalten = (5, 10, 42, 131, 138)
        extraSpalten = self.ones
        # x("OnEs", self.ones)
        spaltenNamen = {
            5: "Transzendentalien, Strukturalien, Universum n",
            10: "Galaxie n",
            42: "Galaxie 1/n",
            131: "Transzendentalien, Strukturalien, Universum 1/n",
            138: "Dagegen-Gegen-Transzendentalien, Gegen-Strukturalien, Universum n",
            202: "neutrale Gegen-Transzendentalien, Gegen-Strukturalien, Universum n",
            None: "Richtung-Richtung",
        }
        tags = [
            frozenset({ST.sternPolygon, ST.universum}),
            frozenset({ST.sternPolygon, ST.galaxie}),
            frozenset({ST.gleichfoermigesPolygon, ST.galaxie}),
            frozenset({ST.gleichfoermigesPolygon, ST.universum}),
            frozenset({ST.sternPolygon, ST.universum}),
            frozenset({ST.sternPolygon, ST.universum}),
            frozenset({ST.sternPolygon, ST.universum}),
        ]

        for r, kk in enumerate(extraSpalten):
            rowsAsNumbers |= {
                len(self.relitable[0]) + r,
            }
            self.tables.generatedSpaltenParameter_Tags[len(rowsAsNumbers) - 1] = tags[r]

        vergangenheit: list = []
        for kkk, kk in enumerate(extraSpalten):
            self.primAmounts = 0
            self.oldPrimAmounts = 0
            self.lastPrimAnswers: dict = {}
            for i, cols in enumerate(relitable[: self.tables.lastLineNumber + 1]):
                into = (
                    [""]
                    if i != 0
                    else ["Primzahlwirkung (7, Richtung) ", spaltenNamen[kk]]
                )

                self.oldPrimAmounts = self.primAmounts
                if couldBePrimeNumberPrimzahlkreuz(i):
                    self.primAmounts += 1
                if primCreativity(i) == 1:
                    into = [PrimAnswer(i)]
                    self.lastPrimAnswers[i] = "".join(into)

                elif i > 1:
                    for couple in primRepeat(tuple(primFak(i))):
                        if couple[1] == 1:
                            into += [PrimAnswer2(couple[0]), " + "]
                        elif kk is not None:
                            into += [
                                str(relitable[couple[1]][kk]),
                                " * ",
                                PrimAnswer2(couple[0]),
                                " + ",
                            ]
                        else:
                            into += [
                                "[",
                                str(vergangenheit[couple[1]]),
                                "] * letztendlich: ",
                                PrimAnswer2(couple[0]),
                                " + ",
                            ]
                    into = into[:-1]
                elif i == 1:
                    into = [PrimAnswer(1)]
                into = ["".join(into)]
                if kk is None:
                    vergangenheit += into
                self.relitable[i] += into

        for r, kk in enumerate(extraSpalten):
            self.tables.generatedSpaltenParameter[
                len(self.tables.generatedSpaltenParameter)
                + self.tables.SpaltenVanillaAmount
            ] = self.tables.dataDict[4][(extraSpalten[r],)]
            # x("HFT", self.tables.dataDict[4][(extraSpalten[r],)])

        return self.relitable, rowsAsNumbers

    def readConcatCsv_tabelleDazuColchange(
        self,
        zeilenNr: int,
        tabelleDazuCol: list,
        concatTable: int,
        ifTransponiert=False,
    ) -> list:
        tabelleDazuColNeu: list = []

        for i, cell in enumerate(tabelleDazuCol, 1):
            gebrRatZahl = (
                Fraction(zeilenNr, i) if not ifTransponiert else Fraction(i, zeilenNr)
            )

            # alxp("AAA")
            cellNeu = self.spalteMetaKonkretTheorieAbstrakt_getGebrRatUnivStrukturalie(
                gebrRatZahl,
                self.struktAndInversSpalten,
                self.gebrUnivTable4metaKonkret,
                concatTable in (3, 5),
            )
            tabelleDazuColNeu += [cellNeu if cellNeu is not None else ""]

        return tabelleDazuColNeu

    def readConcatCsv(
        self,
        relitable: list,
        rowsAsNumbers: set,
        concatTableSelection: set,
        concatTable: int = 1,
    ) -> tuple:
        """Fügt eine Tabelle neben der self.relitable an
        momentan ist es noch fix auf primnumbers.csv
        aber das wird gerade geändert

        @type relitable: list
        @param relitable: Haupttabelle self.relitable
        @type rowsAsNumbers: set
        @param rowsAsNumbers: welche Spalten der neuen Tabelle dazu kommen sollen
        @rtype: list[list]
        @return: relitable + weitere Tabelle daneben
        """
        global folder

        if concatTable in (2, 4):
            self.struktAndInversSpalten: tuple = (5, 131)

            self.gebrUnivTable4metaKonkret = self.readOneCSVAndReturn(2)

        elif concatTable in (3, 5):
            self.struktAndInversSpalten: tuple = (10, 42)
            self.gebrUnivTable4metaKonkret = self.readOneCSVAndReturn(3)

        def transpose(matrix):
            t = []
            x: int
            y: int
            for x in range(len(matrix[0])):
                t += [[]]
                for y in range(len(matrix)):
                    t[x] += [matrix[y][x]]
            return t

        self.relitable = relitable
        concatCSVspalten: set = set()
        if len(concatTableSelection) > 0 and concatTable in range(1, 6):
            tableToAdd = self.readOneCSVAndReturn(concatTable)
            tableToAdd = self.readConcatCsv_ChangeTableToAddToTable(
                concatTable, tableToAdd, transpose
            )
            if concatTable == 1:
                tableToAdd2 = [["Primzahlvielfache, nicht generiert"]]
                for t, zeile in enumerate(tableToAdd[1:], 1):
                    zeileNeu = []
                    for zelle in zeile:
                        if len(zelle.strip()) > 3:
                            zeileNeu += [
                                (
                                    "<li>"
                                    if self.tables.htmlOutputYes
                                    else ""
                                    if not self.tables.bbcodeOutputYes
                                    else "[*]"
                                )
                                + zelle
                                + ("</li>" if self.tables.htmlOutputYes else "")
                            ]
                    zeileNeu = [
                        (
                            ""
                            if self.tables.htmlOutputYes or self.tables.bbcodeOutputYes
                            else " | "
                        ).join(
                            (
                                ["<ul>"]
                                if self.tables.htmlOutputYes
                                else [""]
                                if not self.tables.bbcodeOutputYes
                                else ["[list]"]
                            )
                            + zeileNeu
                            + (
                                ["</ul>"]
                                if self.tables.htmlOutputYes
                                else [""]
                                if not self.tables.bbcodeOutputYes
                                else ["[/list]"]
                            )
                        )
                    ]
                    tableToAdd2 += [zeileNeu]
                tableToAdd = tableToAdd2

            self.relitable, tableToAdd = self.tables.fillBoth(
                self.relitable, tableToAdd
            )
            lastlen = 0
            maxlen = 0
            for i, (tabelleDazuCol, relicol) in enumerate(
                zip(tableToAdd, self.relitable)
            ):

                lastlen = len(tabelleDazuCol)
                if lastlen > maxlen:
                    maxlen = lastlen
                dazu = list(tabelleDazuCol) + [""] * (maxlen - len(tabelleDazuCol))

                if concatTable in (2, 3) and i != 0:
                    dazu = self.readConcatCsv_tabelleDazuColchange(i, dazu, concatTable)
                elif concatTable in (4, 5) and i != 0:
                    dazu = self.readConcatCsv_tabelleDazuColchange(
                        i, dazu, concatTable, True
                    )

                self.relitable[i] += dazu
                if i == 0:
                    for u, heading in enumerate(dazu):
                        # x("SBm", [concatTable, u, headingsAmount])
                        self.readConcatCsv_LoopBody(
                            concatCSVspalten,
                            concatTable,
                            concatTableSelection,
                            dazu,
                            heading,
                            rowsAsNumbers,
                            u,
                        )

        return self.relitable, rowsAsNumbers, concatCSVspalten

    def readConcatCSV_choseCsvFile(self, concatTable):
        place = os.path.join(
            os.getcwd(),
            os.path.dirname(__file__),
            os.path.basename(
                "./primenumbers.csv"
                if concatTable == 1
                else "./gebrochen-rational-universum.csv"
                if concatTable in (2, 4)
                else "./gebrochen-rational-galaxie.csv"
                if concatTable in (3, 5)
                else None
            ),
        )
        return place

    def readConcatCsv_ChangeTableToAddToTable(self, concatTable, tableToAdd, transpose):
        if concatTable in (4, 5):
            tableToAdd = transpose(tableToAdd)
        if concatTable in range(2, 6):
            tableToAdd = [
                [
                    (
                        ("n/" + str(n + 1))
                        if concatTable in (2, 3)
                        else (str(n + 1) + "/n")
                        if concatTable in (4, 5)
                        else "Fehler"
                    )
                    + (
                        " Universum"
                        if concatTable in (2, 4)
                        else " Galaxie"
                        if concatTable in (3, 5)
                        else "Fehler"
                    )
                    for n in range(len(tableToAdd[0]))
                ]
            ] + tableToAdd
        return tableToAdd

    def readConcatCsv_LoopBody(
        self,
        concatCSVspalten,
        concatTable,
        concatTableSelection,
        dazu,
        heading,
        rowsAsNumbers,
        u,
    ):
        if (u + 2 in concatTableSelection and concatTable in range(2, 6)) or (
            concatTable == 1  # and int(heading) in concatTableSelection
        ):
            if concatTable not in range(2, 6) or u + 1 != len(dazu):
                delta = 1 if concatTable in range(2, 6) else 0
                selectedSpalten = u + len(self.relitable[0]) - len(dazu) + delta
                rowsAsNumbers.add(selectedSpalten)
                concatCSVspalten.add(selectedSpalten)
                if (
                    len(self.tables.generatedSpaltenParameter)
                    + self.tables.SpaltenVanillaAmount
                    in self.tables.generatedSpaltenParameter
                ):
                    raise ValueError

                self.readConcatCsv_SetHtmlParamaters(concatTable, heading, u)

    def readConcatCsv_SetHtmlParamaters(self, concatTable, heading, u):
        if concatTable in range(2, 6):
            self.tables.generatedSpaltenParameter[
                len(self.tables.generatedSpaltenParameter)
                + self.tables.SpaltenVanillaAmount
            ] = self.tables.dataDict[5 + ((concatTable - 2) % 2)][u + 2]
            # x("nnn", self.tables.dataDict[5 + ((concatTable - 2) % 2)][u + 2])
            # x("nnn", u)
        if concatTable == 1:
            intoHtmlPara = (
                [
                    (
                        "Multiplikationen",
                        "Nicht_generiert",
                    )
                ],
            )

            # x("EDS", self.tables.dataDict[2][int(heading)])
            self.tables.generatedSpaltenParameter[
                len(self.tables.generatedSpaltenParameter)
                + self.tables.SpaltenVanillaAmount
                # ] = self.tables.dataDict[2][int(heading)]
            ] = intoHtmlPara
