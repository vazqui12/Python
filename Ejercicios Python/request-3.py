import requests

headers = {'User-Agent':'Se tensa'}

response = requests.get("https://google.es", headers=headers)

print(response.request.headers)
