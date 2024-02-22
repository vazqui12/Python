import requests

payload = {'key1':'value1', 'key2':'value2'}
headers = {'User-Agent':'my-app/1.0.0'}

response = requests.post("https://httpbin.org/post", data=payload, headers=headers)

print(f"\n[+] URL final: {response.url}\n")
print(response.text)
