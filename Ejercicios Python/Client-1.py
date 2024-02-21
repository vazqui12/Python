#!/usr/bin/env python3

import socket

def start_client():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 1234))
        s.sendall(b"Hola Server")
        data = s.recv(1024)

    print(f"\n[+] Mensaje recibido del server: {data.decode()}")

start_client()
