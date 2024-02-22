import requests

url = 'http://github.com'

r = requests.get(url)

for request in r.history:
    print(f"\n[+] Hemos pasado por el dominio {request.url} con un codigo de estado {request.status_code}")

print(f"\n[+] URL final: {r.url} con el codigo de estado: {r.status_code}")