#!/usr/bin/env python3 

import os 

directorio_actual = os.getcwd()

print(f"\n[+] El directorio actual es: {directorio_actual}")

files = os.listdir(directorio_actual)

print(f"\n[+] Listando los archivos existentes del directorio {directorio_actual}: \n")

for file in files:
    print(f"-> {file}")

if not os.path.exists('mi_directorio'):
    os.mkdir("mi_directorio")

    print(f"\n[+] Creando directorio 'mi_directorio'\n")

    files = os.listdir(directorio_actual)

    for file in files:
        print(f"-> {file}")
    
print(f"\n[+] Existe el archivo 'mi_archivo.txt'? -> {os.path.exists('Ejercicio-1.py')}")

# key = 'SHELL'
value = os.getenv('SHELL')

print(f"\n[+] Valor de la variable de entorno Kitty: {value}")

print(f"\n[+]Ruta:{os.path}")