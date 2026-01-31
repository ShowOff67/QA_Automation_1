from selenium.webdriver import Keys
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

# Open Ostad.app
driver.get("https://ostad.app/")
time.sleep(5)



# Handle popup if it appears (close 'X' button)
try:
    close_popup = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div/div/div/div/img')
    close_popup.click()
    print("Popup detected and closed.")
    time.sleep(2)
except Exception:
    print("No popup detected.")

time.sleep(2)

# search
search = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div/div/div[1]/div/button")
search.send_keys(" SQA " + Keys.ENTER)
time.sleep(2)

product = driver.find_element(By.XPATH, "/html/body/div/main/div/div/div/div/div[1]/div[2]/div[1]/a/div/div[2]/div[2]")
product.click()
time.sleep(3)

b_btn = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button/div/p")
b_btn.click()
time.sleep(3)

# Click Login button
login_btn = driver.find_element(By.ID, "nav_btn_login")
login_btn.click()
time.sleep(3)

# Enter phone number
phone_email_input = driver.find_element(By.XPATH, "//input[@placeholder='ফোন নাম্বার বা ইমেইল দিন']")
phone_email_input.send_keys("01313887478")
time.sleep(2)

# First submit (to go to password step)
first_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
first_submit.click()
time.sleep(4)

# Enter password
password_input = driver.find_element(By.XPATH, "//input[@placeholder='পাসওয়ার্ড দিন']")
password_input.send_keys("sadia1234")
time.sleep(2)

# Final login submit - using the same reliable method as first submit
try:
    final_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    final_submit.click()
    print("Final login submitted successfully.")
    time.sleep(5)
except Exception as e:
    print("Could not find final submit button with type='submit':", e)

print("Page title after login attempt:", driver.title)



# Keep browser open
# driver.quit()