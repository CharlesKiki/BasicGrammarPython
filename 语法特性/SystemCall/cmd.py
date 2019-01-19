#!/usr/bin/env python
'''
    功能：
        This file can call system command.
'''
import os
import re

with os.popen('who', 'r') as f:
    for eachLine in f:
        print(re.split('\s\s+|\t', eachLine.rstrip()))
