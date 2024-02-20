import requests

with requests.Session() as session:
    session.auth = ('foo','bar')
    response1 = session.get('https://httpbin.org/basic-auth/foo/bar')
    print(response1.text)

    response2 = session.get('https://httpbin.org/basic-auth/foo/bar')
    print(response2.text)

