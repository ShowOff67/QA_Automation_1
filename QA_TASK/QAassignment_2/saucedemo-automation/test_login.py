import pytest
from selenium import webdriver
from login_page import LoginPage
from product_page import ProductPage

@pytest.fixture
def driver():
    driver =webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)

    login_page.login('standard_user','secret_sauce')

    assert driver.current_url == ProductPage.EXPECTED_URL, \
        f"URL mismatch. Expected: {ProductPage.EXPECTED_URL}, GOT: {driver.current_url}"
    
    product_page = ProductPage(driver)

    assert product_page.is_login_successful(), \
        "Login was successful but the expected Product Page elements are missing."

    header_element = driver.find_element(*product_page.PRODUCT_TITLE)
    assert header_element.text == "Products", "The header text is not 'Products'."