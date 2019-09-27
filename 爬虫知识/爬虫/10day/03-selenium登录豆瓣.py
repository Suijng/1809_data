from selenium import webdriver

import requests

driver = webdriver.Chrome(executable_path='/home/sj/桌面/爬虫/chromedriver')
driver.get('https://www.douban.com/')
driver.find_element_by_id('form_email').send_keys('1627765913@qq.com')
driver.find_element_by_id('form_password').send_keys('sj7845464@')

element = driver.page_source.find('captcha_field')
if element == -1:
    driver.find_element_by_class_name('bn-submit').click()
else:
    url = driver.find_element_by_xpath('//img[@class="captcha_image"]').get_attribute('src')
    html = requests.get(url)
    img = html.content
    with open('yzm.png', 'wb') as f:
        f.write(img)

    code = input('请输入验证码:')
    driver.find_element_by_id('captcha_field').send_keys(code)
    driver.find_element_by_class_name('bn-submit').click()
