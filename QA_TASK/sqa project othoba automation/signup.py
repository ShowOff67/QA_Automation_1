from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

# Launch browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

time.sleep(2)
driver.maximize_window()

# Open Othoba
driver.get("https://othoba.com/")
time.sleep(3)

# Click Sign In
# sign_in = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[3]/div/div[2]/div[1]/a[1]")
# sign_in.click()
# time.sleep(3)

# Click Sign Up tab
sign_up = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[3]/div/div[2]/div[1]/a[2]")
sign_up.click()
time.sleep(3)

# Enter phone number
phone = driver.find_element(By.ID, "Phone")
phone.send_keys("01849896090")
time.sleep(2)

# Enter email
email = driver.find_element(By.ID, "Email")
email.send_keys("hasibulgreen@gmail.com")
time.sleep(2)

# Click Create button
create_btn = driver.find_element(By.XPATH, "/html/body/div[2]/main/main/div[2]/div/form/div[3]/div/div[1]/label")
create_btn.click()
time.sleep(2)


# First name
F_name = driver.find_element(By.ID, "FirstName")
F_name.send_keys("Hasibul")
time.sleep(2)

# last name
L_name = driver.find_element(By.ID, "LastName")
L_name.send_keys("Shanto")
time.sleep(2)


# Day
day = Select(driver.find_element(By.NAME, "DateOfBirthDay"))
day.select_by_value("1")
time.sleep(1)

# Month (May = 5)
month = Select(driver.find_element(By.NAME, "DateOfBirthMonth"))
month.select_by_value("5")
time.sleep(1)

# Year
year = Select(driver.find_element(By.NAME, "DateOfBirthYear"))
year.select_by_value("1999")
time.sleep(2)


# password
password = driver.find_element(By.ID, "Password")
password.send_keys("Hasibul212!@#")
time.sleep(2)

# confirm password
c_password = driver.find_element(By.ID, "ConfirmPassword")
c_password.send_keys("Hasibul212!@#")
time.sleep(2)

# captcha

# register
# reg = driver.find_element(By.ID, "register-button")
# reg.click()
# time.sleep(2)


time.sleep(5)
driver.quit()
