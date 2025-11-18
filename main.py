from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
wait = WebDriverWait(driver, 10)

driver.maximize_window()
driver.get("https://www.saucedemo.com/")
sleep(1)

def logout():
    try:
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        sleep(0.5)
        driver.find_element(By.ID, "logout_sidebar_link").click()
    except:
        driver.refresh()
        sleep(1)
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        sleep(0.5)
        driver.find_element(By.ID, "logout_sidebar_link").click()

for user in usernames:
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    sleep(1)

    if not driver.find_elements(By.CSS_SELECTOR, "h3[data-test='error']"):
        logout()

driver.quit()
