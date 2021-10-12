from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login import login
from time import sleep

# set the Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')

# use Chrome to access the clock-punching website
driver = webdriver.Chrome(options=chrome_options)  # omit options if don't want to use headless mode; add options=chrome_options if you want to use headless mode
driver.get('https://healthreport.zju.edu.cn/ncov/wap/default/index')
print("\033[0;32m%s\033[0m" % '[10%] Successfully started the automata.')  # 32m is green

# call the submodule login
login_object = login(driver)
login_object.login_caller()
print("\033[0;32m%s\033[0m" % '[20%] Successfully logged you in.')  # 32m is green

# fill in the form
driver.implicitly_wait(10)

jiezhong_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[4]/div/div/div[1]/span[1]/i')
jiezhong_button.click()
sleep(1)
print("\033[0;33m%s\033[0m" % '[30%] Automata processing to Vaccine part...')  # 33m is yellow

buyi_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[5]/div/div/div[5]/span[1]/i')
buyi_button.click()
sleep(1)
print("\033[0;33m%s\033[0m" % '[36%] Automata processing to BY part...')  # 33m is yellow

yiwancheng_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[6]/div/div/div[2]/span[1]/i')
yiwancheng_button.click()
sleep(1)
print("\033[0;33m%s\033[0m" % '[40%] Automata processing to YWC part...')  # 33m is yellow

fareqingjia_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[7]/div/div/div[2]/span[1]/i')
fareqingjia_button.click()
sleep(1)
print("\033[0;33m%s\033[0m" % '[44%] Automata processing to Fever part...')  # 33m is yellow

farewai_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[8]/div/div/div[2]/span[1]/i')
farewai_button.click()
sleep(1)
print("\033[0;33m%s\033[0m" % '[47%] Automata processing to FW part...')  # 33m is yellow

jiankangma_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[13]/div/div/div[1]/span[1]/i')
jiankangma_button.click()
sleep(1)
print("\033[0;33m%s\033[0m" % '[52%] Automata processing to Healthcare Code part...')  # 33m is yellow

# will show up after clicking "jiankangma" button
jiankangmayanse_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[14]/div/div/div[1]/span[1]/i')
jiankangmayanse_button.click()
sleep(1)
print("\033[0;33m%s\033[0m" % '[56%] Automata processing to Healthcare Code Color part...')  # 33m is yellow

zaixiao_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[15]/div/div/div[1]/span[1]/i')
zaixiao_button.click()
sleep(1)
print("\033[0;33m%s\033[0m" % '[61%] Automata processing to On Campus part...')  # 33m is yellow

diliweizhi_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[19]/div/input')
diliweizhi_button.click()
sleep(1)
print("\033[0;33m%s\033[0m" % '[66%] Accessing your location...')  # 33m is yellow

jiatingchengyuan_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[22]/div/div/div[2]/span[1]/i')
jiatingchengyuan_button.click()
sleep(1)
print("\033[0;33m%s\033[0m" % '[82%] Automata processing to Family Member part...')  # 33m is yellow

chengnuo_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[34]/div/div/div/span[1]/i')
chengnuo_button.click()
sleep(1)
print("\033[0;33m%s\033[0m" % '[86%] Automata processing to Integrity Guarantee part...')  # 33m is yellow

submit_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[5]/div/a')
submit_button.click()
sleep(1)
print("\033[0;32m%s\033[0m" % '[90%] Submitting your report...')  # 32m is green

try:
    confirm_button = driver.find_element_by_xpath \
        ('/html/body/div[4]/div/div[2]/div[2]')
    confirm_button.click()
except:
    print("\033[0;33m%s\033[0m" % "You've already punched the clock today! Please do not punch the clock more than 1 time.")  # 33m is yellow
    driver.close()
    exit(0)

sleep(1)
print("\033[0;32m%s\033[0m" % '[96%] Confirming your status...')  # 32m is green

OK_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[2]/div/a')
OK_button.click()
sleep(2)
print("\033[0;32m%s\033[0m" % '[100%] Successfully completed the punchclock program!')  # 32m is green

driver.close()
