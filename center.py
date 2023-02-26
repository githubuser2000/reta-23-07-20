#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import platform
import pprint
import re
import sys
from collections import OrderedDict

try:
    from collections import Callable
except ImportError:
    from typing import Callable

import html
from itertools import filterfalse
from typing import Optional

try:
    from orderedset import OrderedSet
except:
    OrderedSet = set

from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax

Primzahlkreuz_pro_contra_strs = (
    "Primzahlkreuz_pro_contra",
    "nachvollziehen_emotional_oder_geistig_durch_Primzahl-Kreuz-Algorithmus_(15)",
)
# try:
#    from numba import jit
# except:
#
#    def jit(nopython=None, parallel=True, cache=True):
#        def _jit(f):
#            return f
#
#        return _jit


# originalLinesRange = range(1028)  # Maximale Zeilenanzahl

infoLog = False
output = True
pp = pprint.PrettyPrinter(indent=4)

for arg in sys.argv:
    if arg == "-debug":
        infoLog = True

Multiplikationen = [("Multiplikationen", "")]
shellRowsAmount: int


def isZeilenAngabe(text):
    if len(text) > 0 and text[0] == "v":
        text = text[1:]
    a = []
    for g in text.split(","):
        a += [isZeilenAngabe_betweenKommas(g)]
    return all(a)


def isZeilenAngabe_betweenKommas(g):
    x = len(re.findall(r"[0-9]+\-[0-9]+", g))
    y = len(re.findall(r"[0-9]+\-[0-9]+\-[0-9]+", g))
    return (
        True
        if bool(re.match(r"^\-?[0-9-]+[\+0-9,]*$", g))  # len(g) > 0 and
        and g[-1] not in ["-", "+"]
        and (
            (x < 2 and y == 0)
            or (bool(re.match(r"^\-?[0-9]+[\+0-9,]*$", g)) and x == 0)
        )
        and "--" not in g
        and "++" not in g
        and "+-" not in g
        and "-+" not in g
        and ",+" not in g
        and "+," not in g
        and "-," not in g
        else False
    )


def retaPromptHilfe():
    readMe = "ReTaPromptReadme.md"
    place = os.path.join(
        os.getcwd(), os.path.dirname(__file__), os.path.basename("./" + readMe)
    )
    with open(place, encoding="utf-8") as f:
        markdownText = f.read()
    abDa = markdownText.find("+++", 2)
    pattern = r"{#.*}"
    markdownText = re.sub(pattern, "", markdownText)
    console = Console()
    md = Markdown(markdownText[abDa + 3 :])
    console.print(md)


def retaHilfe():
    readMe = "readme-reta.md"
    place = os.path.join(
        os.getcwd(), os.path.dirname(__file__), os.path.basename("./" + readMe)
    )
    with open(place, encoding="utf-8") as f:
        markdownText = f.read()
    console = Console()
    md = Markdown(markdownText)
    console.print(md)


def getTextWrapThings(maxLen=None) -> tuple:
    global shellRowsAmount
    if "Brython" not in sys.version.split():
        import html2text
        import pyphen
        # from hyphen import Hyphenator
        from textwrap2 import fill

        h_de = None
        # h_de = Hyphenator("de_DE")
        dic = pyphen.Pyphen(
            lang="de_DE"
        )  # Bibliothek für Worteilumbruch bei Zeilenumbruch

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

    else:
        html2text = None
        pyphen = None
        Hyphenator = None
        fill = None
        SiZe = os.get_terminal_size()
        ColumnsRowsAmount, shellRowsAmountStr = SiZe.columns, SiZe.lines
    shellRowsAmount = int(shellRowsAmountStr) if maxLen is None else int(maxLen)
    return shellRowsAmount, h_de, dic, fill


def x(text1, text):
    global output
    """Für mich, damit ich mal alle prints ausschalten kann zum vorführen,
    wenn ich noch beim Entwicklen war."""
    if infoLog and output:
        if type(text) is str:
            print(text1 + ": " + text)
        else:
            print(text1 + ": ", end="")
            pp.pprint(text)


def alxp(text):
    global output
    """Für mich, damit ich mal alle prints ausschalten kann zum vorführen,
    wenn ich noch beim Entwicklen war."""
    if infoLog and output:
        if type(text) is str:
            print(text)
        else:
            pp.pprint(text)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def cliout(text, color=False, stype=""):
    if output:
        if color and len(text) > 0:
            text = " ".join(text.split())
            # if stype == "html":
            #    text = text.replace("<tr","\n  <tr").replace("<td","\n    <td")
            console = Console(width=len(text))
            console.print(
                Syntax(text.strip(), stype, word_wrap=True, indent_guides=True), end=""
            )
        else:
            print(text)

    # class AlxList(list):
    # def __eq__(self, bla):
    # return hash(str(super())) == hash(str(bla))

    # def __gt__(self, bla):
    # return hash(str(super())) > hash(str(bla))

    # def __ge__(self, bla):
    # return hash(str(super())) >= hash(str(bla))

    # def __lt__(self, bla):
    # return hash(str(super())) < hash(str(bla))

    # def __le__(self, bla):
    # return hash(str(super())) <= hash(str(bla))


# def sort(array):
# less: list = []
# equal: list = []
# greater: list = []

# if len(array) > 1:
# pivot = array[0]
# pivot: list = list(pivot)
# pivot2: list = pivot
# for x in array:
# x = list(x)
# x2 = x
# if x2 < pivot2:
# less.append(x)
# elif x2 == pivot2:
# equal.append(x)
# elif x2 > pivot2:
# greater.append(x)
# # Don't forget to return something!
# return (
# sort(less) + equal + sort(greater)
# )  # Just use the + operator to join lists
# # Note that you want equal ^^^^^ not pivot
# else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
# return array


class DefaultOrderedDict(OrderedDict):
    # Source: http://stackoverflow.com/a/6190500/562769
    def __init__(self, default_factory=None, *a, **kw):
        if default_factory is not None and not isinstance(default_factory, Callable):
            raise TypeError("first argument must be callable")
        OrderedDict.__init__(self, *a, **kw)
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return OrderedDict.__getitem__(self, key)
        except KeyError:
            return self.__missing__(key)

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = value = self.default_factory()
        return value

    def __reduce__(self):
        if self.default_factory is None:
            args = tuple()
        else:
            args = (self.default_factory,)
        return type(self), args, None, None, self.items()

    def copy(self):
        return self.__copy__()

    def __copy__(self):
        return type(self)(self.default_factory, self)

    def __deepcopy__(self, memo):
        import copy

        return type(self)(self.default_factory, copy.deepcopy(self.items()))

    def __repr__(self):
        return "OrderedDefaultDict(%s, %s)" % (
            self.default_factory,
            OrderedDict.__repr__(self),
        )


def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = OrderedSet()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


# @jit(nopython=True, parallel=True, cache=True)
def BereichToNumbers(MehrereBereiche: str) -> set:

    Bereiche: list[str] = MehrereBereiche.split(",")
    dazu: set[int] = set()
    hinfort: set[int] = set()
    menge: Optional[set[int]]

    for EinBereich in Bereiche:
        if len(EinBereich) > 1 and EinBereich[0] == "-":
            EinBereich = EinBereich[1:]
            menge = hinfort
        elif len(EinBereich) > 0 and EinBereich[0] != "-":
            menge = dazu
        else:
            menge = None

        if menge is not None:
            if EinBereich.isdecimal():
                EinBereich = EinBereich + "-" + EinBereich
            BereichCouple: list[str] = EinBereich.split("-")
            if (
                len(BereichCouple) == 2
                and BereichCouple[0].isdecimal()
                and BereichCouple[0] != "0"
                and BereichCouple[1].isdecimal()
                and BereichCouple[1] != "0"
            ):
                for number in range(int(BereichCouple[0]), int(BereichCouple[1]) + 1):
                    menge |= {number}
    return dazu - hinfort


# @jit(nopython=True, parallel=True, cache=True)
def BereichToNumbers2(
    MehrereBereiche: str, vielfache=False, maxZahl: int = 1028
) -> set:
    if len(MehrereBereiche) > 0 and MehrereBereiche[0] == "v":
        MehrereBereiche = MehrereBereiche[1:]
        vielfache = True

    if not isZeilenAngabe(MehrereBereiche):
        return set()

    if not vielfache and maxZahl == 0:
        maxZahl = float("inf")

    Bereiche: list[str] = MehrereBereiche.split(",")
    dazu: set[int] = set()
    hinfort: set[int] = set()
    menge: Optional[set[int]]

    for EinBereich in Bereiche:
        BereichToNumbers2_EinBereich(EinBereich, dazu, hinfort, maxZahl, vielfache)
    # print(str(dazu - hinfort))
    return dazu - hinfort


def BereichToNumbers2_EinBereich(EinBereich, dazu, hinfort, maxZahl, vielfache):
    if len(EinBereich) > 1 and EinBereich[0] == "-":
        EinBereich = EinBereich[1:]
        menge = hinfort
    elif len(EinBereich) > 0 and EinBereich[0] != "-":
        menge = dazu
    else:
        menge = None
    around = []
    if menge is not None:
        BereichTuple2: list[str] = EinBereich.split("+")
        if EinBereich.isdecimal():
            EinBereich = EinBereich + "-" + EinBereich
        elif len(BereichTuple2) > 0 and BereichTuple2[0].isdecimal():
            EinBereich = BereichTuple2[0] + "-" + BereichTuple2[0]
            if len(BereichTuple2) > 1:
                EinBereich += "+" + "+".join(BereichTuple2[1:])
        BereichCouple: list[str] = EinBereich.split("-")

        BereichToNumbers2_EinBereich_Menge(
            BereichCouple, around, maxZahl, menge, vielfache
        )


def BereichToNumbers2_EinBereich_Menge(
    BereichCouple, around, maxZahl, menge, vielfache
):
    if (
        len(BereichCouple) == 2
        and BereichCouple[0].isdecimal()
        and BereichCouple[0] != "0"
        # and BereichCouple[1].isdecimal()
        # and BereichCouple[1] != "0"
    ):
        BereichPlusTuples = BereichCouple[1].split("+")
        if len(BereichPlusTuples) < 2:
            around = [0]
        else:
            richtig = True
            numList = []
            for t2 in BereichPlusTuples:
                if t2.isdecimal():
                    numList += [int(t2)]
                else:
                    richtig = False
            if richtig and len(numList) > 0:
                around = numList[1:]
                BereichCouple[1] = numList[0]
        if vielfache:
            BereichToNumbers2_EinBereich_Menge_vielfache(
                BereichCouple, around, maxZahl, menge
            )
        else:
            BereichToNumbers2_EinBereich_Menge_nichtVielfache(
                BereichCouple, around, maxZahl, menge
            )


def BereichToNumbers2_EinBereich_Menge_nichtVielfache(
    BereichCouple, around, maxZahl, menge
):
    for number in range(int(BereichCouple[0]), int(BereichCouple[1]) + 1):
        for a in around:
            c = number + a
            if c < maxZahl:
                menge |= {c}
            d = number - a
            if d > 0 and d < maxZahl:
                menge |= {d}


def BereichToNumbers2_EinBereich_Menge_vielfache(BereichCouple, around, maxZahl, menge):
    i = 0
    if len(around) == 0 or len(set(around) & {0}) == 1:
        while all([int(BereichCouple[0]) * i < maxZahl - a for a in around]):
            i += 1
            for number in range(int(BereichCouple[0]), int(BereichCouple[1]) + 1):
                for a in around:
                    c = number * i
                    if c <= maxZahl:
                        menge |= {c}
    else:
        while all([int(BereichCouple[0]) * i < maxZahl - a for a in around]):
            i += 1
            for number in range(int(BereichCouple[0]), int(BereichCouple[1]) + 1):
                for a in around:
                    c = (number * i) + a
                    if c <= maxZahl:
                        menge |= {c}
                    d = (number * i) - a
                    if d > 0 and d < maxZahl:
                        menge |= {d}
