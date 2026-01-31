import pytest
from login_page import LoginPage
from product_page import ProductPage
from cart_page import CartPage
from checkout_step_one_page import CheckoutStepOnePage
from checkout_step_two_page import CheckoutStepTwoPage
from conftest import driver

@pytest.mark.order(2)
@pytest.mark.regression
def test_multiple_product_order_validation(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    products_page = ProductPage(driver)
    products_page.add_item_by_name("Sauce Labs Backpack")
    products_page.add_item_by_name("Sauce Labs Bike Light")
    products_page.add_item_by_name("Sauce Labs Bolt T-Shirt")

    products_page.click_cart_icon()
    cart_page = CartPage(driver)
    
    # Assertion: Validate item count
    expected_item_count = 3
    assert cart_page.get_item_count() == expected_item_count, \
        f"Expected {expected_item_count} items, found {cart_page.get_item_count()}."
    
    #Checkout Steps
    cart_page.click_checkout()
    checkout_one = CheckoutStepOnePage(driver)
    checkout_one.fill_user_info("Multi", "Order", "12345")
    
    #Checkout Step 2 (Validation)
    checkout_two = CheckoutStepTwoPage(driver)

    expected_subtotal = 55.97 
    subtotal_element_text = driver.find_element(*checkout_two.ITEM_TOTAL).text 
    actual_subtotal = float(subtotal_element_text.replace('Item total: $', ''))
    
    assert actual_subtotal == expected_subtotal, \
        f"Subtotal mismatch. Expected: ${expected_subtotal}, Got: ${actual_subtotal}"

    #Complete the Purchase
    checkout_two.click_finish()
    
    # Assertion: Final success
    success_header = driver.find_element(*checkout_two.SUCCESS_HEADER).text
    assert "Thank you for your order!" in success_header, "Order completion failed."