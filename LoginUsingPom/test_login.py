from selenium import webdriver
from login import LoginPage
import time

driver = webdriver.Chrome()
driver.get("https://labsqajobs.qaharbor.com/")

# driver.fullscreen_window()
driver.maximize_window()

login = LoginPage(driver)
login.login("xoxase6826@rickix.com", "12345678")

time.sleep(2)