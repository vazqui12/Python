import sys
print(f"\n[+] Nombre del script: {sys.argv[0]}")
print(f"\n[+] Total de argumentos: {len(sys.argv)}")
print(f"\n[+] Mostrando los argumentos: {' '.join(argument for argument in sys.argv)}")

print(f"\n[+] Mostrando las rutas de Python:\n")

for element in sys.path:
    print(element)

print(f"\n[+] Saliendo con codigo existoso 0")
sys.exit(0)