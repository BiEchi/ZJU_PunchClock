from selenium.webdriver.common.keys import Keys
import configparser
from sys import exit


class login:
    def __init__(self, driver=None):
        # local variable initialization
        self.driver = driver
        self.account = "example.19@intl.zju.edu.cn"
        self.password = "PasswordYouLike"
        self.timeout = 8

    def load_account_info(self):
        # load the config file
        config = configparser.ConfigParser()
        config.read("config.ini")
        # Use scratch
        self.account = config['identification_information']['account_config']
        self.password = config['identification_information']['password_config']
        # Use app
        # self.account = input("Please enter your account (INTL E-mail) e.g. Haob.88@intl.zju.edu.cn\n> ")
        # print("\033[0;32m%s\033[0m" % 'Your account is {}.'.format(self.account)) # 32m is green
        # self.password = input("Please enter your passwd e.g. Popu#7852\n> ")
        # print("\033[0;32m%s\033[0m" % 'Successfully typed in your Password.')  # 32m is green
        return

    def logging_in_process(self):
        print("\033[0;33m%s\033[0m" % 'Logging you in...')  # 33m is yellow

        try:
            # enter the account name
            account_input_box = self.driver.find_element_by_xpath(
                '//*[@id="username"]')
            account_input_box.send_keys(self.account)
            account_input_box.send_keys(Keys.ENTER)

            # enter the password and confirm
            password_input_box = self.driver.find_element_by_xpath(
                '//*[@id="password"]')
            password_input_box.send_keys(self.password)
            password_input_box.send_keys(Keys.ENTER)

            # click the YES button
            YES_button = self.driver.find_element_by_xpath('//*[@id="dl"]')
            YES_button.click()

        except:
            print("\033[0;31m%s\033[0m" % 'Something logging wrong but we will resume!')  # 31m is red

        return

    def login_caller(self):
        self.load_account_info()
        self.logging_in_process()
        return
