#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import cProfile
import sys

import reta
import yappi

yappi.set_clock_type("cpu")  # Use set_clock_type("wall") for wall time
yappi.start()

reta.Program(sys.argv)


yappi.get_func_stats().print_all()
yappi.get_thread_stats().print_all()
