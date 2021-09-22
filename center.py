#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import platform
import pprint
import re
import sys

infoLog = False
output = True
pp = pprint.PrettyPrinter(indent=4)

for arg in sys.argv:
    if arg == "-debug":
        infoLog = True

Multiplikationen = [("Multiplikationen", "")]


def getTextWrapThings(maxLen=None) -> tuple:
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

        try:
            if platform.system() != "Windows":
                ColumnsRowsAmount, shellRowsAmountStr = (
                    os.popen("stty size", "r").read().split()
                )  # Wie viele Zeilen und Spalten hat die Shell ?
            else:
                ColumnsRowsAmount, shellRowsAmountStr = "80", "80"
        except Exception:
            ColumnsRowsAmount, shellRowsAmountStr = "80", "80"

    else:
        html2text = None
        pyphen = None
        Hyphenator = None
        fill = None
        ColumnsRowsAmount, shellRowsAmountStr = "50", "50"
    shellRowsAmount: int = int(shellRowsAmountStr) if maxLen is None else int(maxLen)
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


def cliout(text):
    if output:
        print(text)
