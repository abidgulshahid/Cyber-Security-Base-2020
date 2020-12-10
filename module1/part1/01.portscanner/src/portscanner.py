#!/usr/bin/env python3
import sys
import socket
 
 
def get_accessible_ports(address, min_port, max_port):
    found_ports = []
    add = socket.gethostbyname(address)
    for port in range(min_port,max_port+1):
        conn = socket.socket()
        r = conn.connect_ex((add,port))
        if r == 0: 
            found_ports.append((port))
            conn.close()
 
    return found_ports
 
 
 
def main(argv):
    address = sys.argv[1]
    min_port = int(sys.argv[2])
    max_port = int(sys.argv[3])
    ports = get_accessible_ports(address, min_port, max_port)
    if ports:
        for p in ports:
 
            print("Founded Ports: ",str(p))
    else:
        print ("All Ports are closed")
# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
    if len(sys.argv) != 4:
        print('usage: python %s address min_port max_port' % sys.argv[0])
    else:
        main(sys.argv)