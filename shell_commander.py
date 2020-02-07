#!/usr/bin/env python3
# Expected behavior - run command from shell with any number of arguments
__author__ = "xenon-manta"

import sys
from subprocess import call

if len(sys.argv) < 2:
    exit()

argsIn = sys.argv[::-1]
argsOut = ""

def grunt (argsIn,argsOut):
    try:
        val = argsIn.pop()
        argsOut = argsOut + val + " "
    except:  
        return argsOut
    return grunt(argsIn, argsOut)

command = str(grunt(argsIn[:-1],""))

try:
    retcode = call(command, shell=True)
    if retcode < 0:
        print(sys.stderr, "Child was terminated by signal", -retcode)
    else:
        print(sys.stderr, "Child returned", retcode)
except OSError as e:
    print(sys.stderr, "Execution failed:", e)