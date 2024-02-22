import requests

response = requests.get('https://httpbin.org/get')

data = response.json()
print(response.text)
print(data)

if 'headers' in data and 'User-Agent' in data['headers']:
    user_agent = data['headers']['User-Agent']
    print(f"\n[+] User-Agent: {user_agent}")
else:
    print(f"\n[!] No existe este campo en la respuesta\n")