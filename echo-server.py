#!/usr/bin/env python3

import socket
import os

HOST = '' #Standart loopback inerface address (localhost)
PORT = 65432      # Port to listen on (non-privileged ports are > 1023)

f = open('task/server.log', 'w')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        f.write('Connected by')
        while True:
            data = conn.recv(1024)
            conn.sendall("OK:".encode('utf-8')+ data)
            if (data):
                print("OK:".encode('utf-8')+ data, file=f)

