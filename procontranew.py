#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib4tables import (couldBePrimeNumberPrimzahlkreuz,
                        couldBePrimeNumberPrimzahlkreuz_fuer_aussen,
                        couldBePrimeNumberPrimzahlkreuz_fuer_innen,
                        primCreativity, primMultiple)

primAmounts = 0
keinePrimzahl1, keinePrimzahl2 = True, True
start1, start2 = 1, 5
list1, list2 = [], []
weiter1a, weiter1b, weiter2a, weiter2b = 0, 0, 0, 0
for num in range(0, 50):
    if couldBePrimeNumberPrimzahlkreuz(num):
        primAmounts += 1
    if primCreativity(num) == 1 or num == 1:

        if couldBePrimeNumberPrimzahlkreuz_fuer_innen(num):
            print(str(num) + ": pro innen")
            list1 += [num]
            if num > 16:
                if keinePrimzahl1:
                    print("gegen " + str(list2[weiter1b + 1]))
                    weiter1b += 1
                else:
                    print("gegen " + str(list1[weiter1a]))
                    weiter1a += 1
            keinePrimzahl1 = False

        if couldBePrimeNumberPrimzahlkreuz_fuer_aussen(num):
            print(str(num) + ": pro außen")
            list2 += [num]
            if num > 16:
                if keinePrimzahl2:
                    print("für " + str(list1[weiter2b + 1]))
                    weiter2b += 1
                else:
                    print("für " + str(list2[weiter2a]))
                    weiter2a += 1
            keinePrimzahl2 = False
    else:
        if couldBePrimeNumberPrimzahlkreuz_fuer_innen(num):
            keinePrimzahl1 = True
        elif couldBePrimeNumberPrimzahlkreuz_fuer_aussen(num):
            keinePrimzahl2 = True
        print(str(primMultiple(num)))
