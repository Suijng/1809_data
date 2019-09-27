from selenium import webdriver

drive = webdriver.Chrome(executable_path='/home/sj/桌面/爬虫/chromedriver')

drive.get('https://www.douban.com/')

drive.find_element_by_id('form_email').send_keys('1627765913@qq.com')
drive.find_element_by_id('form_password').send_keys('sj7845464@')


drive.find_elements_by_class_name('bn-submit').click()


