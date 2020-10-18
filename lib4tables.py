#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


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
        if math.floor(oneResult) == oneResult:
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
