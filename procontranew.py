#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib4tables import (couldBePrimeNumberPrimzahlkreuz,
                        couldBePrimeNumberPrimzahlkreuz_fuer_aussen,
                        couldBePrimeNumberPrimzahlkreuz_fuer_innen,
                        primCreativity)

primAmounts = 0
flag1, flag2 = True, True
start1, start2 = 1, 5
list1, list2 = [], []
for num in range(0, 50):
    if couldBePrimeNumberPrimzahlkreuz(num):
        primAmounts += 1
    if primCreativity(num) == 1:

        if couldBePrimeNumberPrimzahlkreuz_fuer_innen(num):
            print(str(num) + ": pro innen")
            list1 += [num]
            if num > 16:
                if flag1:
                    pass
            flag1 = False
        elif not couldBePrimeNumberPrimzahlkreuz_fuer_aussen(num):
            flag1 = True

        if couldBePrimeNumberPrimzahlkreuz_fuer_aussen(num):
            print(str(num) + ": pro außen")
            list1 += [num]
            if num > 16:
                if flag2:
                    pass
            flag2 = False
        elif not couldBePrimeNumberPrimzahlkreuz_fuer_innen(num):
            flag2 = True
