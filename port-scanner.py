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

#add a baner
print("-"*50)
print("Scanning target " + target)
print("Time Started: "+str(datetime.now()))
print("-"*50)

try:
    for port in range(1,451):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result =  s.connect_ex((target,port))
        if result == 0:
            print(f'Port {port} is open.')
        s.close()
    print("\nScanning Succesful")

except KeyboardInterrupt:
    print()
    print("Exiting program")
    sys.exit()

except socket.gaierror:
    print("Hostname couldn't be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()

