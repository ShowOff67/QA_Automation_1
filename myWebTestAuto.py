from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options to maximize window
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Start the Chrome browser with Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the URL
driver.get("https://showoffchat-ai.netlify.app")

# Wait for the page to load completely
time.sleep(3)

# Step 1: Perform chatting - Send 3-4 messages
# Wait for the chat input field to be visible
chat_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "userInput"))
)

# Wait for the send button (Ask button) to be clickable
ask_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-ask"))
)

# Function to send a message and wait for the reply
def send_message(message):
    chat_box.clear()  # Clear the chat input field before sending a new message
    chat_box.send_keys(message)
    ask_button.click()
    time.sleep(3)  # Wait for the reply (adjust time as necessary)

# Send 3-4 chat messages
send_message("Hello! How are you?")
send_message("What's your name?")
send_message("Tell me a joke.")
send_message("That's all for now.")

# Step 2: Check multiple themes
themes = ["default", "red-vibrance", "dark-glow"]

for theme in themes:
    # Change the theme
    # Wait for the theme dropdown button to be clickable and click it
    theme_dropdown_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "themeDropdownBtn"))
    )
    theme_dropdown_button.click()
    time.sleep(1)  # Wait for dropdown to open

    # Select the new theme based on the loop
    theme_element = driver.find_element(By.XPATH, f"//a[@data-theme='{theme}']")
    theme_element.click()
    time.sleep(2)  # Wait for theme to change

    # Check if the theme is "dark-glow"
    if theme == "dark-glow":
        print("Changing glow types in Dark Glow theme...")

        # Select different glow types in the Dark Glow theme
        glow_buttons = [
            ("Mix Glow", "//button[@data-glow-type='gradient']"),
            ("Purple Glow", "//button[@data-glow-type='purple']"),
            ("Orange Glow", "//button[@data-glow-type='orange']"),
            ("White Glow", "//button[@data-glow-type='white']")
        ]

        for glow_name, glow_xpath in glow_buttons:
            glow_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, glow_xpath))
            )
            glow_button.click()
            print(f"Selected {glow_name} glow")
            time.sleep(2)  # Wait for glow effect to change

    # After changing theme and glow effects, send another chat message
    send_message(f"Testing theme: {theme.capitalize()}!")

# Step 3: Change the background video 4-5 times
# Open the theme dropdown again to access the video option
theme_dropdown_button.click()
time.sleep(1)

# Click "Change Background Video" multiple times (4-5)
for i in range(4):
    try:
        # Wait for the "Change Background Video" button to become clickable
        change_video_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "changeBackgroundVideoBtn"))
        )
        change_video_button.click()
        print(f"Changing background video ({i+1})...")
        time.sleep(2)  # Wait for the video change
    except Exception as e:
        print(f"Error occurred while changing the background video: {e}")
        break  # Exit loop if an error occurs (e.g., button is no longer clickable)

# Step 4: Final chat after video changes
send_message("Background video changes are complete!")

# Step 5: Close the browser
driver.quit()
