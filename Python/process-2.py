import time
import multiprocessing
import requests

def realizar_peticion(url):
    response = requests.get(url)
    print(f"\n[+] URL[{url}]: {len(response.content)} bytes")

dominios = [
    "https://google.com",
    "https://github.com"
]

start_time = time.time()

procesos = []

for url in dominios:
    process = multiprocessing.Process(target=realizar_peticion, args=(url,))
    process.start()
    procesos.append(process)

for process in procesos:
    process.join()

end_time = time.time()

print(f"\n[+] Tiempo total transcurrido: {round(end_time - start_time,2)} segundos")