import requests

response = requests.get('https://httpbin.org/basic-auth/foo/bar', auth=('foo','bar'))

print(response.text)
