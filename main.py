from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login import login
from time import sleep

# set the Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')

# use Chrome to access the clock-punching website
driver = webdriver.Chrome(options=chrome_options)  # omit options if don't want to use headless mode; add options=chrome_options if you want to use headless mode
params = {
    # GPS location of Haining
    "latitude": 30.520463,
    "longitude": 120.727656,
    "accuracy": 100
}
driver.execute_cdp_cmd("Page.setGeolocationOverride", params)
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
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[5]/div/div/div[6]/span[1]/i')
buyi_button.click()
sleep(1)
print("\033[0;33m%s\033[0m" % '[36%] Automata processing to BY part...')  # 33m is yellow

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

shixishijian_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[8]/div/div/div[3]/span[1]/i')
shixishijian_button.click()
sleep(1)

diliweizhi_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[11]/div/input')
diliweizhi_button.click()
sleep(1)
print("\033[0;33m%s\033[0m" % '[66%] Accessing your location...')  # 33m is yellow

chengnuo_button = driver.find_element_by_xpath \
    ('/html/body/div[1]/div[1]/div/section/div[4]/ul/li[28]/div/div/div/span[1]/i')
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
