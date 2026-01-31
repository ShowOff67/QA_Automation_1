import pytest
from login_page import LoginPage
from product_page import ProductPage
from cart_page import CartPage
from checkout_step_one_page import CheckoutStepOnePage
from checkout_step_two_page import CheckoutStepTwoPage
from conftest import driver

@pytest.mark.order(1)
@pytest.mark.smoke
def test_successful_single_product_order(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    products_page = ProductPage(driver)
    products_page.add_first_item_to_cart()

    products_page.click_cart_icon()
    cart_page = CartPage(driver)
    assert cart_page.get_item_count() == 1, "Expected 1 item in cart."
    
    cart_page.click_checkout()
    checkout_one = CheckoutStepOnePage(driver)
    checkout_one.fill_user_info("Test", "User", "12345")
    
    checkout_two = CheckoutStepTwoPage(driver)
    total = checkout_two.get_price_total()
    assert 0.00 < total < 100.00, f"Total price is unrealistic: ${total}"

    checkout_two.click_finish()
    
    success_header = driver.find_element(*checkout_two.SUCCESS_HEADER).text
    assert success_header == "Thank you for your order!", "Order success message not found."
    success_text = driver.find_element(*checkout_two.SUCCESS_TEXT).text
    assert "Your order has been dispatched" in success_text, "Order confirmation text mismatch."