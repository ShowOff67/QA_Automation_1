import pytest
from login_page import LoginPage
from product_page import ProductPage

@pytest.mark.smoke
def test_user_logout(driver):
    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')
    
    products_page = ProductPage(driver)
    products_page.logout()

    assert driver.current_url == LoginPage.URL, \
        f"Logout failed! Expected URL: {LoginPage.URL}, Got: {driver.current_url}"

    assert driver.find_element(*LoginPage.USER_NAME).is_displayed(), \
        "Login page elements are not visible after logout."