import time
from urllib import response
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
'User-Agent' : ua.random
}

s = requests.Session()
login_url = 'https://accounts.douban.com/j/mobile/login/basic'
form_data = {
'ck':'',
'name':'hransun72@hotmail.com',
'password':'chetah',
'remember':'false',
'ticket':''
}

response = s.post(login_url,data = form_data, headers=headers)

url2 = 'https://www.douban.com/accounts'
response2 = s.get(url2,headers=headers)

with open('profile.html','w+') as f:
    f.write(response2.text)
