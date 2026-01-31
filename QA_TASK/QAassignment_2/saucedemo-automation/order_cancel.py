from selenium.webdriver.common.by import By

class OrderCancel:
    URL = 'https://www.saucedemo.com/checkout-step-one.html'

    cancel_button = (By.ID,'cancel')

    def __init__(self,driver):
        self.driver = driver
    
    def cancel_order(self):
        self.driver.find_element(*self.cancel_button).click()