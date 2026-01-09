#!/usr/bin/python3

# Python port scanner by CBD. 

import socket
import pyfiglet

def port_check(host, port):
    s = socket.socket()

    try:
        s.connect((host, port))
        s.timeout(1.5)
    except:
        return(False)
    else:
        return(True)
    
 
banner = pyfiglet.figlet_format("IS NETWORK DOOR OPEN?") # Because the ports open on a machine are like the doors of a house, get it?
print(banner)

print("Welcome to INDO (Is Network Door Open), a simple python port scanner!")

ip = input("Insert the host you want to scan (Inser IP): \n")

last_port = int(input("At what extent you want to scan the ports? (Insert highest port you will scan):\n")

for i in range(1, last_port):
    port_check(IP, i)


