import requests
def get_url_name(myurl ):
    
    #url = 'https://book.douban.com/top250'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent

    response = requests.get(myurl,headers=header)
    print(response.text)

    from bs4 import BeautifulSoup as bs
    bs_info = bs(response.text,'html.parser')
    for tags in bs_info.find_all('div',attrs={'class':'pl2'}):
        for atag in tags.find_all('a'):
            print(atag.get('href'))
            print(atag.get('title'))

urls = tuple(f'https://book.douban.com/top250?start={ page * 25}' for page in range(10))
from time import sleep

if __name__ == '__main__':
    for page in urls:
        get_url_name(page)
        sleep(5)