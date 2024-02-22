import requests

cookies = dict(cookies_are='working')
response = requests.get('https://httpbin.org/cookies', cookies=cookies)

print(response.text)
