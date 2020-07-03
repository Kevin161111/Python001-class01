"""  
使用 requests 或 Selenium 模拟登录石墨文档 https://shimo.im
"""

from selenium import webdriver
import time 

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im')
    time.sleep(1)
    # 获取登录按钮并点击
    btm1 = browser.find_element_by_xpath('//button[contains(@class,"login-button")]')
    btm1.click()

    # 输入注册的账户和密码
    browser.find_element_by_xpath('//input[contains(@name,"mobileOrEmail")]').send_keys('15055495@qq.com')
    browser.find_element_by_xpath('//input[contains(@name,"password")]').send_keys('test123test456')
    time.sleep(1)
    browser.find_element_by_xpath('//button[contains(@class,"sm-button submit")]').click()

    # 获取 cookies信息
    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    browser.close()