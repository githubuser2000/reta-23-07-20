#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(1, os.path.join(os.path.dirname(__file__), "..", "i18n"))
import center
import retaPrompt
import words


class TestStringMethods(unittest.TestCase):
    def test_words(self):
        befehle2 = words.befehle2
        self.assertTrue(
            all(
                [
                    len(value) == 1 if len(key) == 1 else True
                    for (key, value) in befehle2.items()
                ]
            )
        )
        self.assertEqual(len(befehle2.keys()), len(set(befehle2.keys())))
        self.assertEqual(len(befehle2.values()), len(set(befehle2.values())))

    def test_rp(self):
        befehl = "reta -zeilen --vorhervonausschnitt=3-5 -spalten --grundstrukturen=paradigmen"
        sys.argv = befehl.split()
        # import retaPrompt

        center.output = False

        try:
            programm = retaPrompt.reta.Program(sys.argv)
        except SystemExit:
            pass
        self.assertTrue(len(programm.newTable) == 4)
        # print(programm.rowsRange)
        self.assertEqual(programm.finallyDisplayLines, {0, 3, 4, 5})
        # print(programm.finallyDisplayLines)
        # print(programm.numlen)
        # print(programm.newTable)


if __name__ == "__main__":
    unittest.main()
