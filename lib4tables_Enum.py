#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ST(Enum):
    """Spalten Tag"""

    sternPolygon = 0
    gleichfoermigesPolygon = 1
    keinPolygon = 2
    galaxie = 3
    universum = 4


tableTags = {
    {ST.sternPolygon, ST.galaxie,}: {
        0,
        1,
        2,
        3,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        17,
        18,
        19,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        38,
        39,
        40,
        41,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        54,
        55,
        56,
        57,
        59,
        60,
        61,
        62,
        63,
        64,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        78,
        79,
        82,
        83,
        85,
        86,
        88,
        89,
        90,
        91,
        92,
    },
    {ST.universum, ST.sternPolygon}: {4, 5, 65, 77, 80, 81, 93},
    {ST.galaxie, ST.gleichfoermigesPolygon}: {16, 37, 42, 58},
    {ST.universum, ST.gleichfoermigesPolygon, ST.sternPolygon}: {
        20,
        21,
    },
    {ST.galaxie, ST.gleichfoermigesPolygon, ST.sternPolygon}: {52, 53, 87},
    {ST.galaxie, ST.universum, ST.sternPolygon}: {75, 76, 84},
}

# 65 = michael commons hauptspalte
# 82 Organisationen wie SOZ
# 93 = Galaxie Dreierstrukur * Zweierstruktur
