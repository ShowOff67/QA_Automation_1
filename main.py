from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

chromium_path = r"C:\Users\ShowOff\AppData\Local\Chromium\Application\chrome.exe"

usernames = [
    "standard_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
]
password = "secret_sauce"

options = Options()
options.binary_location = chromium_path

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
sleep(1)

def logout():
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    sleep(0.5)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    sleep(1)

for user in usernames:
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    sleep(1)

    if not driver.find_elements(By.CSS_SELECTOR, "h3[data-test='error']"):
        logout()

driver.quit()
