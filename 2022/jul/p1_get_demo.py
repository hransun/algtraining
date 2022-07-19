import requests
r = requests.get('https://api.github.com/events')
r.status_code
r.headers['content-type']
#r.text
r.encoding
r.json()

payload = {'key1':'v1', 'key2':'v2'}
r = requests.get('http://httpbin.org/get', params=payload)
r.url

header = {'user-agent':'safari'}
r = requests.get('http://httpbin.org/get',headers=header)
r.headers