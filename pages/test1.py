#coding:utf-8
from common.base import Base


from selenium import webdriver
import time
import json

driver = webdriver.Chrome()
driver.get('http://47.110.145.204:8284/#/login')
# 删除本次打开网页时的所有cookie
driver.delete_all_cookies()
with open('jsoncookie.json','r') as f:
    ListCookies = json.loads(f.read())
# 将jsoncookie.json里的cookie写入本次打开的浏览器中。
for cookie in ListCookies:
    driver.add_cookie({
        'domain': '47.110.145.204',
        'name': cookie['name'],
        'value': cookie['value'],
        'path': cookie['path'],
        'expires': None,
        'httpOnly':cookie['httpOnly'],
        'secure':cookie['secure']
    })
time.sleep(3)
driver.get('http://47.110.145.204:8284/#/index')
print('111111')
time.sleep(3)
driver.close()
