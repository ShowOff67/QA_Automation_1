import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 

@pytest.fixture
def driver():
    chrome_options = Options()
    
    chrome_options.add_experimental_option(
        "prefs", 
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver_instance = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver_instance.implicitly_wait(10)
    yield driver_instance
    driver_instance.quit()