from selenium.webdriver.common.by import By

class CheckoutStepOnePage:
    URL = 'https://www.saucedemo.com/checkout-step-one.html'

    first_name_input = (By.ID,'first-name')
    last_name_input = (By.ID,'last-name')
    postal_code_input = (By.ID,'postal-code')
    continue_button = (By.ID,'continue')

    def __init__(self,driver):
        self.driver = driver
    
    def fill_user_info(self, first, last, postal_code):
        self.driver.find_element(*self.first_name_input).send_keys(first)
        self.driver.find_element(*self.last_name_input).send_keys(last)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()