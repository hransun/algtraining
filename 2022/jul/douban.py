import requests

url = 'https://book.douban.com/top250'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {}
header['user-agent'] = user_agent

response = requests.get(url,headers=header)
print(response.text)

from bs4 import BeautifulSoup as bs
bs_info = bs(response.text,'html.parser')
print(bs_info.find_all('div',attrs={'class':'pl2'})[0])