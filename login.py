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
        # self.account = config['identification_information']['account_config']
        # self.password = config['identification_information']['password_config']
        # Use app
        self.account = input("Please enter your account (INTL E-mail) e.g. Haob.88@intl.zju.edu.cn\n> ")
        print("\033[0;32m%s\033[0m" % 'Your account is {}.'.format(self.account)) # 32m is green
        self.password = input("Please enter your passwd e.g. Popu#7852\n> ")
        print("\033[0;32m%s\033[0m" % 'Successfully typed in your Password.')  # 32m is green
        return

    def logging_in_process(self):
        print("\033[0;33m%s\033[0m" % 'Logging you in...')  # 33m is yellow

        try:
            # click the "INTL ID" button
            self.driver.implicitly_wait(self.timeout)
            INTL_ID_button_second = self.driver.find_element_by_xpath(
                '/html/body/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/a/img')
            INTL_ID_button_second.click()


            # enter the account name
            self.driver.implicitly_wait(self.timeout)
            account_input_box = self.driver.find_element_by_xpath(
                '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/input[1]')
            account_input_box.send_keys(self.account)
            account_input_box.send_keys(Keys.ENTER)

            # enter the password and confirm

            self.driver.implicitly_wait(self.timeout)
            password_input_box = self.driver.find_element_by_xpath(
                '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[2]/input')
            password_input_box.send_keys(self.password)
            password_input_box.send_keys(Keys.ENTER)

            # click the YES button
            self.driver.implicitly_wait(self.timeout)
            YES_button = self.driver.find_element_by_xpath('//*[@id="idSIButton9"]')
            YES_button.click()

        except:
            print("\033[0;31m%s\033[0m" % 'Wrong account or password!')  # 31m is red
            self.driver.close()
            exit(0)

        return

    def login_caller(self):
        self.load_account_info()
        self.logging_in_process()
        return
