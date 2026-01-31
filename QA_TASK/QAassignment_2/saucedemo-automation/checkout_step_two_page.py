from selenium.webdriver.common.by import By

class CheckoutStepTwoPage:
    URL = 'https://www.saucedemo.com/checkout-step-two.html'
    
    FINISH_BUTTON = (By.ID, 'finish')
    ITEM_TOTAL = (By.CLASS_NAME, 'summary_subtotal_label')
    TAX_LABEL = (By.CLASS_NAME, 'summary_tax_label')
    GRAND_TOTAL = (By.CLASS_NAME, 'summary_total_label')
    
    SUCCESS_HEADER = (By.CLASS_NAME, 'complete-header')
    SUCCESS_TEXT = (By.CLASS_NAME, 'complete-text')
    
    def __init__(self, driver):
        self.driver = driver

    def get_price_total(self):
        total_text = self.driver.find_element(*self.GRAND_TOTAL).text
        return float(total_text.replace('Total: $', ''))

    def click_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()