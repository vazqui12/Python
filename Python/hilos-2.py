import time
import threading
import requests

def realizar_peticion(url):
    response = requests.get(url)
    print(f"\n[+] URL[{url}]: {len(response.content)} bytes")

dominios = [
    "https://google.com",
    "https://github.com"
]

start_time = time.time()

hilos = []

for url in dominios:
    hilo = threading.Thread(target=realizar_peticion, args=(url,))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()

end_time = time.time()

print(f"\n[+] Tiempo total transucurrido: {round(end_time - start_time,2)} segundos")