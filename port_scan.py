#! /usr/bin/env python3
# Python Port Scanner written based on Gus Khawaja's Python Courses by Rob Saffell

import argparse
from socket import *

# Sets this as a Py3 project, parse incoming arguments, and 
# use the full socket libs
# Usage port_scan.py -a 192.168.1.2 -p 21,22,80,20000

def printBanner(connSock, tgtPort):
    try:
        #Send the data to the target
        if (tgtPort == 80):
            connSock.send('GET HTTP/1.1 \r\n')
        else:
            connSock.send('\r\n')
        
        #Receive banner responses in a 4096 byte receipt buffer
        results = connSock.recv(4096)
        #Print the banner
        print('[+] Banner: ' + str(results))
    except:
        print('[-] Banner not available.\n')


def connScan(tgtHost, tgtPort):
    try:
        # Create a socket object
        connSock = socket(AF_INET,SOCK_STREAM)
        # Try to connect with the target, report success
        connSock.connect((tgtHost, tgtPort))
        print('[+] %d tcp open'% tgtPort)
        printBanner(connSock, tgtPort)
    except:
        #Alert failure
        print('[+] %d tcp closed. '% tgtPort)
    finally:
        #Clean up the open socket
        connSock.close()
def portScan(tgtHost,tgtPorts):
    try:
        # Attempt IP resolution - either from DNS lookup to IP or IP lookup
        ipAddr = gethostbyname(tgtHost)

    except:
        # If resolution fails, print error and exit
        print('[-] Unknown Host')
        exit(0)
    
    try:
        # Attempt to resolve the IP to a Domain Name and Print that Name
        tgtName = gethostbyaddr(ipAddr)
        print('[+] --- Scan result for: ' + tgtName[0] + ' --- ')
    
    except:
        # If Name Resolution fails, use IP to reference target
        print('[+] --- Scan result for: ' + ipAddr + ' --- ')

    # Establish connection wait default timeout (seconds) 
    # for non-response
    setdefaulttimeout(10)

    # Loop through ports included in args
    for tgtPort in tgtPorts:
        connScan(ipAddr, int(tgtPort))

def main():
    parser = argparse.ArgumentParser('TCP Client Scanner')
    parser.add_argument('-a', '--address', type=str, help='The target IP address')
    parser.add_argument('-p', '--port', type=str, help='The port number to connect to')
    args = parser.parse_args()

    ipAddress = args.address
    portNumbers = args.port.split(',')

    portScan(ipAddress, portNumbers)

if __name__ == '__main__':
    main()
