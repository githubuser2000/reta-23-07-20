#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib4tables import (couldBePrimeNumberPrimzahlkreuz,
                        couldBePrimeNumberPrimzahlkreuz_fuer_aussen,
                        couldBePrimeNumberPrimzahlkreuz_fuer_innen,
                        primCreativity)

primAmounts = 0
for num in range(0, 20):
    if couldBePrimeNumberPrimzahlkreuz(num):
        primAmounts += 1
    if primCreativity(num) == 1:
        if couldBePrimeNumberPrimzahlkreuz_fuer_innen(num):
            pass
        if couldBePrimeNumberPrimzahlkreuz_fuer_aussen(num):
            pass
