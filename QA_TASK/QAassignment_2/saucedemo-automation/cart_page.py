from selenium.webdriver.common.by import By

class CartPage:
    URL = 'https://www.saucedemo.com/cart.html'

    checkout_button = (By.ID,'checkout')
    cart_header = (By.CLASS_NAME,'title')

    def __init__(self,driver):
        self.driver = driver
    
    def get_item_count(self):
        items = self.driver.find_elements(By.CLASS_NAME,'cart_item')
        return len(items)
    
    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()