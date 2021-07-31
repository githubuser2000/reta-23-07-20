#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib4tables import (couldBePrimeNumberPrimzahlkreuz,
                        couldBePrimeNumberPrimzahlkreuz_fuer_aussen,
                        couldBePrimeNumberPrimzahlkreuz_fuer_innen,
                        primCreativity)

primAmounts = 0
flag1, flag2 = True, True
for num in range(0, 20):
    if couldBePrimeNumberPrimzahlkreuz(num):
        primAmounts += 1
    if num > 16:
        if primCreativity(num) == 1:

            if couldBePrimeNumberPrimzahlkreuz_fuer_innen(num):
                if flag1:
                    pass
                flag1 = False
            if couldBePrimeNumberPrimzahlkreuz_fuer_aussen(num):
                if flag2:
                    pass
                flag2 = False
        else:
            if couldBePrimeNumberPrimzahlkreuz_fuer_innen(num):
                flag1 = True
            if couldBePrimeNumberPrimzahlkreuz_fuer_aussen(num):
                flag2 = True
