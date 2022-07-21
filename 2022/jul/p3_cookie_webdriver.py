from tokenize import cookie_re
from typing import final
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('https://www.douban.com')
    time.sleep(1)
    
    browser.switch_to.frame(browser.find_element(By.TAG_NAME,'iframe')[0])
    btn1= browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    btn1.click()
    
    browser.find_element_by_xpath('//*[@id="username"]').send_keys('15055495@qq.com')
    browser.find_element_by_id('password').send_keys('test123test123')
    time.sleep(1)
    browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()
    
    cookies = browser.get_cookie()
    print(cookies)
    time.sleep(3)
except Exception as e:
    print(e)
finally:
    browser.close()