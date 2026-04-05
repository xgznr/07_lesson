from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, browser):
        self.driver = browser
        self.checkout_button = (By.ID, "checkout")

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()
