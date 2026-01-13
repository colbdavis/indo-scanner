#!/usr/bin/python3

# Python port scanner by CBD. 

# import socket
# import pyfiglet
import asyncio

ip = input("Insert the host you want to scan (Inser IP): \n")

last_port = int(input("At what extent you want to scan the ports? (Insert highest port you will scan):\n"))

async def port_check(target_ip: str, port: int, timeout: float = 1.0) -> bool:
    
    try:
        # Attempt to connect to the target IP and port
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(target_ip, port),
            timeout=timeout
        )
        # If connection succeeds, the port is open
        writer.close()
        await writer.wait_closed()
        return True
    except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
        # If connection fails or times out, the port is closed
        return False

#   def port_check(host, port):
#       s = socket.socket()

#       try:
#           s.connect((host, port))
#           s.timeout(1.5)
#       except:
#           return(False)
#       else:
#           return(True)
    
 
# banner = pyfiglet.figlet_format("IS NETWORK DOOR OPEN?") # Because the ports open on a machine are like the doors of a house, get it?
# print(banner)

print("Welcome to INDO (Is Network Door Open), a simple python port scanner!")


for port in range(1, last_port):
    try:
    # Your code that might raise an exception (e.g., a loop or asyncio operation)
        asyncio.run(port_check(ip, port))
    except KeyboardInterrupt:
        # Handle the KeyboardInterrupt (e.g., print a message and exit gracefully)
        print("\nScan interrupted by user. Exiting...")
        exit()