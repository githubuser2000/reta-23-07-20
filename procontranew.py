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
proPro, contraContra = {}, {}
for num in range(0, 50):
    if couldBePrimeNumberPrimzahlkreuz(num):
        primAmounts += 1
    if primCreativity(num) == 1 or num == 1:

        if couldBePrimeNumberPrimzahlkreuz_fuer_innen(num):
            print(str(num) + ": pro innen")
            list1 += [num]
            if num > 16:
                if keinePrimzahl1:
                    gegen = list2[weiter1b + 1]
                    weiter1b += 1
                else:
                    gegen = list1[weiter1a]
                    weiter1a += 1
                contraContra[num] = gegen
                print("gegen " + str(gegen))

            keinePrimzahl1 = False

        if couldBePrimeNumberPrimzahlkreuz_fuer_aussen(num):
            print(str(num) + ": pro außen")
            list2 += [num]
            if num > 16:
                if keinePrimzahl2:
                    pro = list1[weiter2b + 1]
                    weiter2b += 1
                else:
                    pro = list2[weiter2a]
                    weiter2a += 1
                proPro[num] = pro
                print("für " + str(pro))

            keinePrimzahl2 = False
    else:
        if couldBePrimeNumberPrimzahlkreuz_fuer_innen(num):
            keinePrimzahl1 = True
        elif couldBePrimeNumberPrimzahlkreuz_fuer_aussen(num):
            keinePrimzahl2 = True
        for couple in primMultiple(num):
            if couple[1] > 16 and primCreativity(couple[1]) == 1:
                flagX = True
            elif couple[0] > 16 and primCreativity(couple[0]) == 1:
                flagX = True
                couple = (couple[1], couple[0])
            else:
                flagX = False

            if flagX:
                if couldBePrimeNumberPrimzahlkreuz_fuer_innen(couple[1]):
                    print(
                        str(num)
                        + " gegen "
                        + str(int(couple[0]) * contraContra[couple[1]])
                    )
                elif couldBePrimeNumberPrimzahlkreuz_fuer_aussen(couple[1]):
                    print(str(num) + " pro " + str(int(couple[0]) * proPro[couple[1]]))
