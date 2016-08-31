#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "python ../../../store-listing-toolkit/populate-v2.py metadata -platform android -prj-path . -sheet 1oqexrvD9EjAonXGnclKRvyD9HtgomWhWKmj-yc3uzq8 -customized-metadata-path ../src/gplay/metadata"
print cmd
os.system(cmd)
