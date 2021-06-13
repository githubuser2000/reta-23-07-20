#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from enum import Enum

from center import (alxp, cliout, getTextWrapThings, infoLog, output,
                    primzahlvielfachesgalaxie, re, x)


class OutputSyntax:
    def coloredBeginCol(self, num: int, rest: bool = False):
        return self.beginZeile

    def generateCell(
        self, num: int, dataDict: dict, content=None, zeile=None, tables=None
    ) -> str:
        return self.beginCell

    beginTable = ""
    endTable = ""
    beginCell = ""
    endCell = ""
    beginZeile = ""
    endZeile = ""


class csvSyntax(OutputSyntax):
    beginTable = ""
    endTable = ""
    beginCell = ""
    endCell = ""
    beginZeile = ""
    endZeile = ""


class markdownSyntax(OutputSyntax):

    beginTable = ""
    endTable = ""
    beginCell = "|"
    endCell = ""
    beginZeile = ""
    endZeile = ""


class bbCodeSyntax(OutputSyntax):
    def coloredBeginCol(self, num: int, rest: bool = False):
        num = int(num) if str(num).isdecimal() else 0
        numberType = primCreativity(num)

        if rest:
            # wenn der Fallm eintritt dass es leerer Text ist der frei ist
            return "[tr]"
            if num == 0:
                return "[tr]"
            elif num % 2 == 0:
                return "[tr]"
            else:
                return "[tr]"
        elif numberType == 1:
            if num % 2 == 0:
                return '[tr="background-color:#66ff66;color:#000000;"]'
            else:
                return '[tr="background-color:#009900;color:#ffffff;"]'
        elif numberType == 2 or num == 1:
            if num % 2 == 0:
                return '[tr="background-color:#ffff66;color:#000099;"]'
            else:
                return '[tr="background-color:#555500;color:#aaaaff;"]'
        elif numberType == 3:
            if num % 2 == 0:
                return '[tr="background-color:#9999ff;color:#202000;"]'
            else:
                return '[tr="background-color:#000099;color:#ffff66;"]'
        elif num == 0:
            return '[tr="background-color:#ff2222;color:#002222;"]'

    def generateCell(
        self, spalte: int, SpaltenParameter: dict, content=None, zeile=None, tables=None
    ) -> str:
        spalte = int(spalte)
        spalte += 2
        return "".join(
            (
                "[td",
                (
                    '="background-color:#000000;color:#ffffff"'
                    if content is not None and int(content) % 2 == 0
                    else '="background-color:#ffffff;color:#000000"'
                )
                if spalte == 0
                else '=""',
                "]",
            )
        )

    beginTable = "[table]"
    endTable = "[/table]"
    beginCell = "[td]"
    endCell = "[/td]"
    beginZeile = "[tr]"
    endZeile = "[/tr]"


class htmlSyntax(OutputSyntax):
    def __init__(self):
        self.zeile = 0

    def coloredBeginCol(self, num: int, rest: bool = False) -> str:
        num = int(num) if str(num).isdecimal() else 0
        numberType = primCreativity(num)
        self.zeile = num
        if rest:
            # wenn der Fallm eintritt dass es leerer Text ist der frei ist
            return "          <tr>\n"
            if num == 0:
                return "          <tr>\n"
            elif num % 2 == 0:
                return "          <tr>\n"
            else:
                return "          <tr>\n"
        elif numberType == 1:
            if num % 2 == 0:
                return (
                    '          <tr style="background-color:#66ff66;color:#000000;">\n'
                )
            else:
                return (
                    '          <tr style="background-color:#009900;color:#ffffff;">\n'
                )
        elif numberType == 2 or num == 1:
            if num % 2 == 0:
                return (
                    '          <tr style="background-color:#ffff66;color:#000099;">\n'
                )
            else:
                return (
                    '          <tr style="background-color:#555500;color:#aaaaff;">\n'
                )
        elif numberType == 3:
            if num % 2 == 0:
                return (
                    '          <tr style="background-color:#9999ff;color:#202000;">\n'
                )
            else:
                return (
                    '          <tr style="background-color:#000099;color:#ffff66;">\n'
                )
        elif num == 0:
            return '          <tr style="background-color:#ff2222;color:#002222;">\n'

    def generateCell(
        self, spalte: int, SpaltenParameter: dict, content=None, zeile=None, tables=None
    ) -> str:
        if zeile == "":
            zeile = 0
        # x("uzt", SpaltenParameter)
        # x("qay", spalte)
        spalte = int(spalte)
        if spalte == -2:
            tupleOfListsOfCouples = (
                [
                    ("zaehlung", ""),
                ],
            )
        elif spalte == -1:
            tupleOfListsOfCouples = (
                [
                    ("nummerierung", ""),
                ],
            )
        else:
            try:
                tupleOfListsOfCouples = SpaltenParameter[spalte]
            except:
                # x("NUM", SpaltenParameter)
                # x("NUM", spalte)
                if str(spalte).isdecimal():
                    raise ValueError
                tupleOfListsOfCouples = (("?", "?"),)
        things1: dict = {}
        # x("ayu", SpaltenParameter)
        # x("azu", tupleOfListsOfCouples)
        for c, couples in enumerate(tupleOfListsOfCouples):
            for paraNum in (0, 1):
                if len(couples[0]) > paraNum:
                    # x("azu" + str(paraNum), couples[0][paraNum])
                    if len(couples[0]) > paraNum:
                        # i = 0
                        para1o2name = couples[0][paraNum]
                        # while (
                        #    len(couples) > i + 1
                        #    and len(couples[i + 1]) > 0
                        #    and para1o2name.strip() == ""
                        # ):
                        #    i += 1
                        #    para1o2name = couples[i][paraNum]
                        if len(para1o2name.strip()) != 0 or True:
                            if paraNum == 1:
                                para1o2name = "".join(["p3_", str(c), "_", para1o2name])
                            try:
                                things1[paraNum] += [para1o2name]
                            except KeyError:
                                things1[paraNum]: list = [
                                    para1o2name,
                                ]
        things: dict = {}
        for key, values in things1.items():
            for i, el in enumerate(values):
                if el != "alles":
                    try:
                        things[key] += (
                            el,
                            ",",
                        )
                    except KeyError:
                        things[key] = (
                            el,
                            ",",
                        )
            things[key] = "".join(things[key])

        spalte += 2
        if len(things) < 2:
            return ""
        else:
            p4: str
            try:
                p4a = tables.generatedSpaltenParameter_Tags[spalte - 2]
                p4b: list = []
                for a in p4a:
                    p4b += [str(a.value)]
                p4 = ",".join(p4b)
            except KeyError:
                p4 = ""
            except:
                p4 = ""
            # x("nix", tables.generatedSpaltenParameter_Tags)
            # x("nüx", spalte - 2)
            # x("nöx2", p4)

            return "".join(
                (
                    '              <td class="',
                    "z_",
                    str(zeile),
                    " r_",
                    str(spalte),
                    " p1_",
                    things[0],
                    " p2_",
                    (things[1] if len(things) > 1 else ""),
                    " p4_",
                    p4,
                    '"',
                    ' style="background-color:#000000;color:#ffffff;display:none"'
                    if content is not None and int(content) % 2 == 0
                    else 'style="background-color:#ffffff;color:#000000;display:none"'
                    if spalte == 0
                    else 'style="display:none"',
                    "><label>\n",
                )
            )

    beginTable = "      <table border=0>"
    endTable = "        </table>\n"
    beginCell = "              <td><label>\n"
    endCell = "\n              </label></td>\n"
    # beginZeile = "          <tr>"
    beginZeile = ""
    endZeile = "          </tr>\n"


def moonNumber(num: int):
    """Hier wird der Zeilenumbruch umgesetzt

    @type num: int
    @param num: zu untersuchende Zahl
    @rtype: tuple(list[int],list[int])
    @return: () wenn keine Mondzahl, sonst 2 Listen mit gleicher Länge aus Elementen: Liste1: Basis der Mondzahl, Liste2: Exponent der Mondzahl
    """
    results: list = []
    exponent: list = []
    for i in range(2, num):
        oneResult = math.pow(num, 1 / i)
        """"sehr unsauber von mir gelöst!!!! , aber reicht für das was es soll
            vorher war 125 nicht mit dabei, bei sehr großen Zahlen wird dieser
            Algo wieder Mist bauen! """
        if round(oneResult) * 100000 == round(oneResult * 100000):
            results += [int(oneResult)]
            exponent += [i - 2]
    return results, exponent


def primFak(n: int) -> list:
    """Alle Primfaktoren einer Zahl als Liste mit mehrfachvorkommen, sofern ja

    @type n: int
    @param n: ein natürliche Zahl
    @rtype: list
    @return: alle Primfaktoren, ggf. mit Mehrfachvorkommen
    """
    faktoren: list = []
    z = n
    while z > 1:
        i = 2
        gefunden = False
        while i * i <= n and not gefunden:
            if z % i == 0:
                gefunden = True
                p = i
            else:
                i = i + 1
        if not gefunden:
            p = z
        faktoren += [p]
        z = z // p
    return faktoren


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def primCreativity(num: int):
    if num == 0:
        return 0
    fak = primRepeat(primFak(num))
    if len(fak) == 1 and fak[0][1] == 1:
        return 1
    if len(fak) == 1:
        return 3
    if len(fak) < 1:
        return 0
    primAmounts = []
    for (prim, primAmount) in fak:
        primAmounts += [primAmount]
    for primAmount in primAmounts:
        divisors = set(divisorGenerator(primAmount)) - {1}
        if len(divisors) == 0:
            try:
                del schnittmenge
            except NameError:
                pass
            break
        try:
            schnittmenge &= divisors
        except NameError:
            schnittmenge = divisors
    try:
        if len(schnittmenge) != 0:
            return 3
        else:
            return 2
    except NameError:
        return 2
    return None


# def getLogarithmOnlyAsPureInt(potenz: int, basis: int) -> int:
#    exponent = math.log(potenz) / math.log(basis)
#    if exponent == round(exponent):
#        return exponent
#    else:
#        return None


def primRepeat(n: list) -> list:
    """Primfaktoren werden zusammengefasst in Liste aus Primfaktor hoch n

    @type n:  list
    @param n: Primfaktoren
    @rtype: list[tuple(n1,n2)]
    @return: Liste aus geordneten Paaren mit Primfaktor hoch n
    """
    n.reverse()
    c = 1
    b = None
    d: list = []
    for a in n:
        if b == a:
            c += 1
        else:
            c = 1
        d += [[a, c]]
        b = a
    d.reverse()
    b = None
    f: list = []
    for e, g in d:
        if b != e:
            if g == 1:
                f += [(e, 1)]
            else:
                f += [(e, g)]
        b = e
    return f


def primMultiple(n: int) -> list:
    """Gibt Liste aus geordneten Paaren aus mit Primzahl und Vielfacher der Primzahl aus denen die Zahl n besteht

    @type n: int
    @param n: eine natürliche Zahl, die zu untersuchen ist
    @rtype: list[tuple(primzahl,vielfacher der Primzahl)] oder bool
    @return: Primzahl und dessen Vielfacher, das mehrmals, so viele Primzahlen wie es gibt, aus denen n besteht
    """
    multiples = [(1, n)]
    for prim in primRepeat(primFak(n)):
        multiples += [(prim[0], round(n / prim[0]))]
    return multiples


def isPrimMultiple(isIt: int, multiples1: list, dontReturnList=True):
    """Ist die Zahl der Vielfache in überhaupt irgendeiner Primzahl

    @type isIt: int
    @param isIt: die Zahl die zu untersuchen ist
    @type multiples1: list[int]
    @param multiple1: Liste an Vielfachern von denen einer zutreffen muss, bei [2,3] ist es True, wenn es das zweifache oder dreifache einer Primzahl ist
    @type dontReturnList: bool
    @param dontReturnList: wenn ja, dann wird nur ausgegeben ob es ein Vielfacher einer Primzahl ist, ansonsten die Liste für welche Vielfacher es zutrifft
    @rtype: list[bool] oder bool
    @return: True wenn Primzahlvielfacher, Liste aus True für ja für welche Multiplikatioren ja
    """
    areThey: list = []
    multiples2 = primMultiple(isIt)
    for multiple1 in multiples1:
        for multiple2 in multiples2:
            areThey += [True if multiple1 == multiple2[1] else False]
            if dontReturnList and areThey[-1]:
                return True
    if dontReturnList:
        return False
    return areThey


def couldBePrimeNumberPrimzahlkreuz(num: int) -> bool:
    Under24 = (1, 5, 7, 11, 13, 17, 19, 23)
    return num % 24 in Under24
