import requests

url = 'https://httpbin.org/post'
my_file = {'archivo': open('example.txt','r')}

response = requests.post(url=url, files=my_file)

print(response.text)