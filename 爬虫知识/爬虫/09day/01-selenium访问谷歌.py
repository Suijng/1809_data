from selenium import webdriver

drive = webdriver.Chrome(executable_path='/home/sj/桌面/爬虫/chromedriver')

drive.get('http://www.baidu.com/')

drive.save_screenshot('baidu.png')




# drive = webdriver.PhantomJS(executable_path='/home/sj/桌面/爬虫/chromedriver')
#
# drive.get('http://www.baidu.com/')


