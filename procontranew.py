#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib4tables import (couldBePrimeNumberPrimzahlkreuz,
                        couldBePrimeNumberPrimzahlkreuz_fuer_aussen,
                        couldBePrimeNumberPrimzahlkreuz_fuer_innen,
                        primCreativity)

primAmounts = 0
keinePrimzahl1, keinePrimzahl2 = True, True
start1, start2 = 1, 5
list1, list2 = [], []
weiter1a, weiter1b, weiter2a, weiter2b = 0, 0, 0, 0
for num in range(0, 50):
    if couldBePrimeNumberPrimzahlkreuz(num):
        primAmounts += 1
    if primCreativity(num) == 1:

        if couldBePrimeNumberPrimzahlkreuz_fuer_innen(num):
            print(str(num) + ": pro innen")
            list1 += [num]
            if num > 16:
                if keinePrimzahl1:
                    pass
                else:
                    weiter1a += 1
            keinePrimzahl1 = False
        elif not couldBePrimeNumberPrimzahlkreuz_fuer_aussen(num):
            keinePrimzahl1 = True

        if couldBePrimeNumberPrimzahlkreuz_fuer_aussen(num):
            print(str(num) + ": pro außen")
            list1 += [num]
            if num > 16:
                if keinePrimzahl2:
                    pass
            keinePrimzahl2 = False
        elif not couldBePrimeNumberPrimzahlkreuz_fuer_innen(num):
            keinePrimzahl2 = True
