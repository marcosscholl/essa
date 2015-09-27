#!/usr/bin/env python
import sys, os
#arg = raw_input('Enter ESSA main file name: ').split()
os.system("valgrind --tool=massif --log-file='/tmp/logfileEssaMassif.out' python /home/scholl/Dropbox/Spyder/essa/apps/SistemaDefesa.py")