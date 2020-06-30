from selenium import webdriver
from time import sleep

#实例化浏览器
driver =webdriver.Chrome()
#打开项目
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.fullscreen_window()
driver.implicitly_wait(10)
sleep(5)
driver.quit()#关闭浏览器 