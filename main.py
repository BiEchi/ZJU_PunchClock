from selenium import webdriver

# use Chrome to access the clock-punching website
driver = webdriver.Chrome()
driver.get('https://healthreport.zju.edu.cn/ncov/wap/default/index')


# wait for next command
sleep(100)