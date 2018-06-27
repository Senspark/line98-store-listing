#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = 'fastlane supply -j ../../Google_Play_Android_Developer.json -p com.senspark.lines98 --skip_upload_apk true --skip_upload_images true --skip_upload_screenshots true'
print cmd
os.system(cmd)
