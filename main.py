from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login import login
from time import sleep

# set the Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')

# use Chrome to access the clock-punching website
driver = webdriver.Chrome(options=None)  # omit options if don't want to use headless mode; add options=chrome_options if you want to use headless mode
driver.get('https://healthreport.zju.edu.cn/ncov/wap/default/index')

# call the submodule login
login_object = login(driver)
login_object.login_caller()

# fill in the form
driver.implicitly_wait(10)

jiezhong_button = driver.find_element_by_xpath\
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[4]/div/div/div[1]/span[1]/i')
jiezhong_button.click()
sleep(1)

buyi_button = driver.find_element_by_xpath\
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[5]/div/div/div[5]/span[1]/i')
buyi_button.click()
sleep(1)

yiwancheng_button = driver.find_element_by_xpath\
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[6]/div/div/div[2]/span[1]/i')
yiwancheng_button.click()
sleep(1)

fareqingjia_button = driver.find_element_by_xpath\
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[7]/div/div/div[2]/span[1]/i')
fareqingjia_button.click()
sleep(1)

farewai_button = driver.find_element_by_xpath\
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[8]/div/div/div[2]/span[1]/i')
farewai_button.click()
sleep(1)

jiankangma_button = driver.find_element_by_xpath\
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[13]/div/div/div[1]/span[1]/i')
jiankangma_button.click()
sleep(1)

# will show up after clicking "jiankangma" button
jiankangmayanse_button = driver.find_element_by_xpath\
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[14]/div/div/div[1]/span[1]/i')
jiankangmayanse_button.click()
sleep(1)

zaixiao_button = driver.find_element_by_xpath\
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[15]/div/div/div[1]/span[1]/i')
zaixiao_button.click()
sleep(1)

diliweizhi_button = driver.find_element_by_xpath\
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[19]/div/input')
diliweizhi_button.click()
sleep(1)

jiatingchengyuan_button = driver.find_element_by_xpath\
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[22]/div/div/div[2]/span[1]/i')
jiatingchengyuan_button.click()
sleep(1)

chengnuo_button = driver.find_element_by_xpath\
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[34]/div/div/div/span[1]/i')
chengnuo_button.click()
sleep(1)

submit_button = driver.find_element_by_xpath\
    ('/html/body/div[1]/div[1]/div/section/div[5]/div/a')
submit_button.click()
sleep(1)

confirm_button = driver.find_element_by_xpath\
    ('/html/body/div[4]/div/div[2]/div[2]')
confirm_button.click()
sleep(1)

OK_button = driver.find_element_by_xpath\
    ('/html/body/div[1]/div[2]/div/a')
OK_button.click()
sleep(2)

driver.close()
