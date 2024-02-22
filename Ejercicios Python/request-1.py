import requests

values = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
response = requests.get("https://httpbin.org/get", params=values)

print(f"\n[+] URL final: {response.url}\n")
print(response.text)
