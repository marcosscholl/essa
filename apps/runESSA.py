#!/usr/bin/env python
import sys, os
os.system("valgrind --tool=massif --log-file='/tmp/logfileEssaMassif.out' essa01.py")
