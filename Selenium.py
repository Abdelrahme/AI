from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriver
from webdriver_manager.firefox import GeckoDriverManager
import time
url='https://www.instagram.com/accounts/login/?source=auth_switcher'
class instagram():
    def __init__(self,email,password,browser):
        self.email=email
        self.password=password
        if browser =='chrome':
            self.driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser =='edge':
            self.driver=webdriver.Edge(executable_path=EdgeChromiumDriver().install())
        elif browser =='firfox':
            self.driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
            self.driver.get(url)
        time.sleep(10)
    def login(self):
        email_element=self.driver.find_element(By.ID,'username')
        email_element.send_keys(self.email)
        password_element=self.driver.find_element(By.ID,'password')
        password_element.send_keys(self.password)
        button_element=self.driver.find_element(By.__class__,'qF0y9Igw0EIwRSHeGOV_acqo5_4EzTmbkEs3CovQjjKUp7DhRcB')
        button_element.click()
        time.sleep(2)
instagram_login=instagram(email='__abdul___m',password='Boudy5563756',browser='firefox')
instagram_login.login()


