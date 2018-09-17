#!/usr/bin/python

import sys
import os
import re

#print "adb"
output=os.popen("adb devices").read().split("\n")


adbCommand=''
for x in sys.argv[1:]:
	adbCommand+=" " + x

for line in output:
	if re.match(".*\s*device$", line):
		serial=re.sub(r'([^\s]*)\s*device$', r'\1', line)
		print serial
		fullAdbCommand="adb -s " + serial + " " + adbCommand
		print "adb cmd:" + fullAdbCommand
		os.popen(fullAdbCommand)
