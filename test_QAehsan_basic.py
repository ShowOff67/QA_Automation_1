from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

time.sleep(2)
driver.maximize_window()

# Open Google
print(driver.title)
driver.get("https://www.saucedemo.com/")
time.sleep(2)

user_name = driver.find_element(By.ID, "user-name" )
password = driver.find_element(By.ID,"password" )
login_button = driver.find_element(By.ID,"login-button" )

user_name.send_keys("standard_user")
time.sleep(2)
password.send_keys("secret_sauce")
time.sleep(2)
login_button.click()


# print the title of the page
print(driver.title)

time.sleep(2)

# Close the browser
driver.quit()
