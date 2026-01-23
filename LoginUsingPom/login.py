from selenium.webdriver.common.by import By
import time

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.find_element(By.XPATH, "//span[text()='Log In']").click()
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        # self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/div/form/div[6]/div/div/button").click()