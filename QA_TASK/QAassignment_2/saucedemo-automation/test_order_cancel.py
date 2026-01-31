import pytest
from conftest import driver
from login_page import LoginPage
from product_page import ProductPage
from cart_page import CartPage
from order_cancel import OrderCancel

@pytest.mark.smoke
def test_order(driver):
    login_page = LoginPage(driver)
    login_page.login('standard_user','secret_sauce')

    products_page = ProductPage(driver)
    products_page.add_first_item_to_cart()

    products_page.click_cart_icon()
    cart_page = CartPage(driver)
    assert cart_page.get_item_count() == 1, "Expected 1 item in cart."

    cart_page.click_checkout()

    order_cancel = OrderCancel(driver)
    order_cancel.cancel_order()

    assert driver.current_url == CartPage.URL, \
        f"Redirect failed! Expected: {CartPage.URL}, Got: {driver.current_url}"

    cart_title = driver.find_element(*cart_page.cart_header).text
    assert cart_title == 'Your Cart', f'Expected Your Cart title but got {cart_title}'

    assert cart_page.get_item_count() == 1, 'Order Proceeds'
