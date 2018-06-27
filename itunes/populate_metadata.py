#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "python ../../../store-listing-toolkit/populate-v3.py metadata -platform iOS -prj-path . -sheet 175xgn3mdWMbjSkPBz2sir1z_YndHM0A1ia5efnJ4_Tg -customized-metadata-path ../src/itunes/metadata"
print cmd
os.system(cmd)
