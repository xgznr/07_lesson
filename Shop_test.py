import pytest
from selenium import webdriver
from pages.MainShopPage import MainShopPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_purchase_total(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = MainShopPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inv_page = MainShopPage(driver)
    items = [
        "Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"
        ]
    for item in items:
        inv_page.add_to_cart(item)

    inv_page.go_to_cart()
    CartPage(driver).checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Evgenii", "Ivanov", "806800")

    total_text = checkout_page.get_total_price()
    assert "58.29" in total_text, \
        f"Ожидалась сумма $58.29, но получили {total_text}"
