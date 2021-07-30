#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cProfile
import sys

import reta

cProfile.run("reta.Program(sys.argv)")
