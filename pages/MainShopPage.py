from selenium.webdriver.common.by import By


class MainShopPage:

    def __init__(self, browser):
        self.driver = browser

    def login(self, user, pwd):
        self.driver.find_element(By.ID, "user-name").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(pwd)
        self.driver.find_element(By.ID, "login-button").click()

    def add_to_cart(self, name):
        formatted_name = name.lower().replace(" ", "-")
        self.driver.find_element(
            By.ID, f"add-to-cart-{formatted_name}"
            ).click()

    def go_to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "a[class='shopping_cart_link']"
            ).click()
