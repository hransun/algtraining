import requests
import lxml.etree

url ='https://book.douban.com/subject/35802030/?icn=index-topchart-subject'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
header = {'user-agent':user_agent}

response = requests.get(url,headers=header)
selector = lxml.etree.HTML(response.text)
name = selector.xpath('//*[@id="wrapper"]/h1/span/text()')
print(name)

mylist = [str(name),'haoran','4.5']
columns_name = ['one']

import pandas as pd
book1 = pd.DataFrame(columns=columns_name, data= mylist)
book1.to_csv('./book1.csv',encoding='gbk')
