#!/usr/bin/env python3

import argparse
import os
import socket
import sys

import confundo

parser = argparse.ArgumentParser("Parser")
parser.add_argument("host", help="Set Hostname")
parser.add_argument("port", help="Set Port Number", type=int)
parser.add_argument("file", help="Set File Directory")
args = parser.parse_args()

def sendFile(sock, fileName: str):
    with open(fileName, "rb") as f:
        data = f.read(confundo.INITIAL_SEQ)
        while data:
            total_sent = 0
            while total_sent < len(data):
                sent = sock.send(data[total_sent:])
                total_sent += sent
            
            data = f.read(confundo.INITIAL_SEQ)

def validate_port(portNumber):
    try:
        if portNumber < 1 or portNumber > 65535:
            raise Exception()
        return portNumber
    except Exception as error:
        sys.stderr.write("ERROR: This is NOT a valid port number.\n")
        sys.stderr.flush()
        sys.exit(1)
        
def start():
    try:
        with confundo.Socket() as sock:
            sock.settimeout(10)
            sock.connect((args.host, int(args.port)))

    except RuntimeError as e:
        sock.__exit__
        sys.stderr.write(f"ERROR: {e}\n")
        sys.exit(1)

if __name__ == '__main__':
    start()
