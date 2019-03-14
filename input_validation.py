#!/usr/bin/env python3
# Establish this as a Python 3 project and run it using python3 command in Linux/Mac shell
# Line 1 has no effect on Windows
# This code was intentionally written without using anything but standard python3 libraries
# Produced by Rob Saffell

# This needs to be refactored to remove global calls. - RMS

import sys
import requests
import json
from requests.auth import HTTPBasicAuth


url_list = []
url_target = []
url_count = 0
thread_count = False
user_id = False
output_tuple = False

def check_input():

    if ((len(sys.argv) == 1) or (sys.argv[1] == "-h") or (sys.argv[1] == "-help")):
        print("Arguments for this script:")
        print("FYI - Threads not yet implemented")
        print("Help (-h): No argument or -h = this banner")
        print("Threads (-t): Integer = Maximum number of threads to spawn. Optional, default = 1, max = 255")
        print("Output (-o): Return output as a tuple, by default output will print to console")
        print("Username:Password (-u): Username and Password in uuu@mail.com password format")
        print("All other arguments: Search terms")
        return False
    else:
        bad_args = ["*","^",";",",","|"]
        for arg_current in bad_args:
            arg_current = str(arg_current)
            if (any(arg_current in arg for arg in sys.argv)):
                print("An invalid character was detected in arguments")
                return False
            else:
                pass

    return args_list()

def args_list():
    global thread_count
    global url_list
    global user_id

    # Checking for specified arguments
    for arg_current in sys.argv:
        if arg_current == "-t":
            thread_count = True
        elif user_id == "p":
            password = arg_current
            user_id = True
        elif user_id == "u":
            user = arg_current
            user_id = "p"
        elif arg_current == "-u":
            user_id = "u"
        elif arg_current == "-o":
            output_tuple = True
        elif arg_current == "-h":
            sys.argv[1] = "-h"
            check_input()
        else:
            try:
                if (int(arg_current) > 0) and (int(arg_current)) < 256 and (thread_count == True):
                    thread_count = int(arg_current)
                    pass
            except:
                if arg_current == sys.argv[0]:
                    pass
                else:
                    url_list.append(arg_current)                 
                pass
    # Returns specified thread count to global, and stored the target url and search terms in url_list
    return api_url(thread_count, url_list, user, password)

check_input()
