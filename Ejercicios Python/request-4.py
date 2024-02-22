import requests

try: 
    response = requests.get('https://google.es', timeout=1)
    response.raise_for_status()

except requests.Timeout:
    print(f"\n[!] La peticion excedio el tiempo de espera")

except requests.HTTPError as http_error:
    print(f"\n[!] Error HTTP: {http_error}")

except requests.RequestException as err:
    print(f"\n[!] Error: {err}")

else:
    print(f"\n[+] No han habido errores")