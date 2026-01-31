from selenium.webdriver.common.by import By

class ProductPage:
    EXPECTED_URL = 'https://www.saucedemo.com/inventory.html'
    PRODUCT_TITLE = (By.CLASS_NAME,'title')
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, 'button[id^="add-to-cart-"]')
    CART_ICON = (By.CLASS_NAME, 'shopping_cart_link')
    menu_button = (By.ID,'react-burger-menu-btn')
    logout_link = (By.ID,'logout_sidebar_link')

    def __init__(self,driver):
        self.driver = driver
    
    def is_login_successful(self):
        url_check = self.driver.current_url == self.EXPECTED_URL

        try:
            header_element = self.driver.find_element(*self.PRODUCT_TITLE)
            element_check = header_element.is_displayed() and header_element.text == 'Products'
        except Exception:
            element_check = False
        return url_check and element_check
    
    def add_first_item_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTONS).click() 

    def add_item_by_name(self, product_name):
        xpath = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button[contains(@id, 'add-to-cart')]"
        self.driver.find_element(By.XPATH, xpath).click()

    def click_cart_icon(self):
        self.driver.find_element(*self.CART_ICON).click()

    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.logout_link).click()