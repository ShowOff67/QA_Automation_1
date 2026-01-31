from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

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
sign_in = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[3]/div/div[2]/div[1]/a[1]")
sign_in.click()
time.sleep(3)


# Enter phone number
phone = driver.find_element(By.XPATH, "/html/body/div[2]/main/main/div[2]/div/div[2]/div/div/div[1]/form/div[1]/input")
phone.send_keys("01849896090")
time.sleep(2)

# Enter email
# email = driver.find_element(By.ID, "Email")
# email.send_keys("hasibulgreen@gmail.com")
# time.sleep(2)

# password
password = driver.find_element(By.XPATH, "/html/body/div[2]/main/main/div[2]/div/div[2]/div/div/div[1]/form/div[2]/input")
password.send_keys("Hasibul212!@#")
time.sleep(2)

# remember
rem = driver.find_element(By.XPATH, "/html/body/div[2]/main/main/div[2]/div/div[2]/div/div/div[1]/form/div[3]/input")
rem.click()
time.sleep(2)

# Click Create button
create_btn = driver.find_element(By.XPATH, "/html/body/div[2]/main/main/div[2]/div/div[2]/div/div/div[1]/form/div[4]/input")
create_btn.click()
time.sleep(2)




# searching product

search = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[3]/div/div[1]/div/div/form/div[2]/input")
search.send_keys("olevs 2859g" + Keys.ENTER)

time.sleep(2)



product = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/figure/distributed-cache/a/img[1]")
product.click()
time.sleep(2)


# add to cart
cart = driver.find_element(By.ID, "add-to-cart-button-620019")
cart.click()
time.sleep(2)



time.sleep(5)
driver.quit()
