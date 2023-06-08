#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(1, os.path.join(os.path.dirname(__file__), "..", "i18n"))
import os
import platform
import pprint
import re
import sys
from collections import OrderedDict

import i18n.words as i18n

try:
    from collections import Callable
except ImportError:
    from typing import Callable

from itertools import filterfalse
from typing import Optional

try:
    from orderedset import OrderedSet
except (ModuleNotFoundError, ImportError):
    OrderedSet = set

anfang = """Hauptprogramm ist reta oder reta.py
Bequemer ist retaPrompt, was es mit Voreinstellungen noch als rp und rpl gibt.

Bedienungsanleitung:
Es gibt 4 Hauptparameter.
**Wichtig: die Nebenparameter müssen direkt hinter dem richtigen Hauptparamter stehen, sonst wirken sie
nicht und dazwischen darf kein anderer Hauptparameter stehen!**
Hauptparameter beginnen mit einem Minus -.
Nebenparameter beginnen mit 2 Minus --.

# Hauptparameter
Besser die Readme aus Markdown mit einem Markdown-Leseprogramm lesen!

## -debug
    *    hat keine Nebenparameter, ist nur für mich als Programmierer relevant und interesssant

## -zeilen

    * --alles
    * --zeit=
        * "gestern"
            bedeutet Religionen 1-9
        * "heute"
            bedeutet nur Religion 10
        * "morgen"
            bedeutet Religionen > 10
        * "gestern,heute,morgen"
            bedeutet Religion 1-10 und höher als 10,
    * --zaehlung=
        * 1,2,3,4,5,...
    * --typ=
        * sonne,mond,planet,schwarzesonne
    * --vielfachevonzahlen=
        * 1,2,3,4,5,...
    * --primzahlvielfache=
        * 1,2,3,4,5,...
    * --vorhervonausschnitt=
        * 1-5,7-10,14,20
    * --vorhervonausschnittteiler
        * bewirkt, dass die Teiler aller Zahlen, die sich aus der Angabe von "--vorhervonausschnitt=" ergeben, zusätzlich dazu kommen
        * z.B. wird aus 12: 2,3,4,6,12
    * --nachtraeglichneuabzaehlung=
        * 3-6,8
        * Dafür werden die Ergebniszeilen neu gezählt. Wurden Zeilen "5 bis 7" zuvor bestimmt und wird nun Zeile 2 hiermit gewählt, wäre das Zeile 6.
    * --nachtraeglichneuabzaehlungvielfache=
        * 3-6,8
        * Dafür werden die Ergebniszeilen neu gezählt. Wurden Zeilen "5 bis 8" zuvor bestimmt und wird nun Zeile 2 hiermit gewählt, wäre das Zeile 6,8, denn bei Neuzählung der Zeilen "5 bis 8" ergeben sich Zeilen "1 bis 4". Davon ist jeder zweite Zeile 2 und 4. Zurückgerechnet auf Zeilen "5 bis 8" sind das Zeilen 6 und 8.
    * --potenzenvonzahlen=
        * 2,3
    * --oberesmaximum=
        * 2000,1500

## -spalten

    * --alles
    * --breite=
    * --breiten=
    """
print(anfang)

things: set = {}


for entry in i18n.paraNdataMatrix:
    position = entry[0][1] if len(entry[0]) > 1 else entry[0][0]
    if len(entry) > 1 and len(entry[1]) > 0 and type(entry[1]) in [list, tuple]:
        thing = entry[1][1] if len(entry[1]) > 1 else entry[1][0]
        if type(thing) is str and type(position) is str:
            try:
                things[position] += [thing]
            except KeyError:
                things[position] = [thing]
    else:
        try:
            things[position] += [list(entry[1])]
        except KeyError:
            things[position] = [list(entry[1])]
for key, value in things.items():
    hasEntries = True if len(value) > 0 and len(value[0]) > 0 else False
    print("    * --{}{} ".format(key, "=" if hasEntries else ""))

    # try:
    if hasEntries:
        print(
            "        * "
            + (
                ",".join([v for v in value if type(v) is str])
                if type(value[0]) is str
                # else (",".join([v2 for v1 in value for v2 in v1]))
                # else str(value)
                else ",".join([b for v in value for b in v])
            )
        )
    # except:
    #    print(value)
print()
print()
print("## -kombination")
print("""    * --galaxie=""")
print(
    "        * "
    + (",".join([v for b in i18n.kombiParaNdataMatrix.values() for v in b]))
)
print("""    * --universum=""")
print(
    "        * "
    + (",".join([v for b in i18n.kombiParaNdataMatrix2.values() for v in b]))
)
ende = """

## -ausgabe
    * --nocolor
    * --art=
        * (nur eins erlaubt)
        * shell,html,csv,markdown,bbcode
    * --onetable
    * --spaltenreihenfolgeundnurdiese=
        * 3,5,1
        * d.h. von z.B. 5 Spalten soll zuerst die 3., dann 5. und 1. angezeigt werden und die anderen nicht!
    * --keineleereninhalte
        * Das macht, dass Zeilen nicht ausgegeben werden, die nur ein Minus oder Fragezeichen oder sonst fast keine Information enthalten
    * --keineueberschriften
        * Überschriften werden nicht ausgegeben.
    * --keinenummerierung
        * Die Zeilennummer und die Zählungen mehrerer Zeilen fällt weg.


## Umkehrungen
    * statt 2-11
      *  -2-11
    * statt 7
      *  -7
    * statt --symbole
      *  --symbole-
    * statt --religionen=sternpolygon
      *  --religionen=-sternpolygon

## Die Plus Synax: gemeint sind Nachbarn
    * 7+1
      * ergibt
      * 6 und 8
      * Das bedeutet, dass beide Nachbarn der 7 verwendet werden
      * Bei Vielfachern wären das dann immer die Nachbarn der 7 also
      * 6,8,13,15,20,22, usw.
    * 9-11+3
      * Im Bereich 9 bis 11 wird der dritte Nachbar verwendet, also:
      * 9 bis 11 wären zunächst die Zahlen 9,10,11
      * Weil es nicht heißt
      * 9-11+0
      * sind es nicht diese Zahlen 9,10,11, sondern
      * statt 9 ist es die 6 und 12, wegen der +3 in der Syntax bei 9-11+3
      * statt 10 die 7 und 13
      * statt 11 die 8 und 14

      * Bei Vielfachen werden die Vielfacher von 9,10,11 gebildet und davon dann die Nachbarn vom Abstand +3 durch Subtraktion und Addition verwendet

    * 10+0+2+5
      * 10,12,8,5,15
      * Die 10 mit Abstand Null ist die 10 selbst.
      * Abstand 2 zur 10 ist 8 und 12
      * Abstand 5 zur 10 ist 5 und 15
    * v5
      * Bei (fast) sämtlichen solchen Zahlenangaben kann ein v davor geschrieben werden: Das führt dazu, dass Vielfacher, statt nur die Zahl, verwendet werden: in dem Beispiel v5 ist es damit statt der Zahl 5 nun auch die Zahlen 5,10,15,20,25, usw.

    * v Syntax dabei
      * 5,v20-22 meint Zeile 5 und außerdem alle Vielfacher von 20,21,22, also z.B. 40,42,44
      *  -20,v10 meint alle Vielfacher von 10 ohne die 20 dabei

### Beispiel (eine Zeile, nicht mehrere):
        `reta -zeilen --vorhervonausschnitt=1-9 -spalten --religionen=sternpolygon,gleichfoermigespolygon --galaxie=babylon --breite=50`

    * Bereichsangaben lassen sich mit Python Generatoren angeben, in geschweiften, runden oder eckigen Klammern, neben den anderen Bereichsangaben mit Komma getrennt.
        * in retaPrompt:
        `reta -zeilen --vorhervonausschnitt={2*n for n in range(2,5)},10 --oberesmaximum=1025 -spalten --Menschliches=motivation --breite=0 -ausgabe --spaltenreihenfolgeundnurdiese=[3*n for n in range(2)]`
        * in der Shell z.B. Bash:
        `reta -zeilen "--vorhervonausschnitt={2*n for n in range(2,5)},10" --oberesmaximum=1025 -spalten --Menschliches=motivation --breite=0 -ausgabe "--spaltenreihenfolgeundnurdiese=[3*n for n in range(2)]"`
        Ein Minus vor so einem Python Generator würde den Bereich abziehen: -[n for n in range(3)]
Besser die Readme aus Markdown mit einem Markdown-Leseprogramm lesen!"""
print(ende)
