from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time


url = 'https://www.facebook.com/login.php'
class FacebookLogin():
    def __init__(self, email, password, browser):

        self.email = email
        self.password = password

        if browser == 'Chrome':
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        self.driver.get(url)
        time.sleep(1)

    def login(self):
        email_element = self.driver.find_element(By.ID,'email')
        email_element.send_keys(self.email)

        password_element = self.driver.find_element(By.ID,'pass')
        password_element.send_keys(self.password)

        login_button = self.driver.find_element(By.ID,'loginbutton')
        login_button.click()

        time.sleep(2)

fb_login = FacebookLogin(email='', password='', browser='Chrome')
fb_login.login()