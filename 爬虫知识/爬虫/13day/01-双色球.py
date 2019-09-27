from selenium import webdriver

import requests

driver = webdriver.Chrome(executable_path='/home/sj/桌面/爬虫/chromedriver')
driver.get('http://kaijiang.500.com/#')
driver.find_element_by_id('lotTypeSelect').send_keys('双色球')
driver.find_element_by_id('selectLotQuery').send_keys('19002')

driver.find_element_by_id('searchBtn').click()






