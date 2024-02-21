#!/usr/bin/env python3

import socket

def start_server():
    
    host = 'localhost'
    port = 1234
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()

        with conn:
            print(f"\n[+] se ha conectado un cliente {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

start_server()