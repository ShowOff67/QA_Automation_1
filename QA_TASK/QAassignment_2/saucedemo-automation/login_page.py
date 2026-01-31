from selenium.webdriver.common.by import By
class LoginPage:
    URL = 'https://www.saucedemo.com/'
    USER_NAME = (By.ID,'user-name')
    PASSWORD = (By.ID,'password')
    LOGIN_BUTTON = (By.ID,'login-button')

    def __init__(self,driver):
        self.driver = driver
        self.driver.get(self.URL)
    
    def login(self,user_name,password):
        self.driver.find_element(*self.USER_NAME).send_keys(user_name)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()