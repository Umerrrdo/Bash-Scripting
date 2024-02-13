#!/bin/python3

import sys
import socket
from datetime import datetime

#The format for this script will be: python3 port-scanner.py <ip>

#Define target
if len(sys.argv) == 2:
    ip = sys.argv[1]
    target = ip.split(".")
    for oct in target:
        if int(oct) <= 0 or int(oct) > 255:
            print("Invalid IP address given")
            sys.exit()
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 port-scanner.py <ip>")
    sys.exit()

