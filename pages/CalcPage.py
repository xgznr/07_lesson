from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, seconds):
        delay_input = self.browser.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, text):
        self.browser.find_element(By.XPATH, f"//span[text()='{text}']").click()

    def get_result(self, timeout):
        WebDriverWait(self.browser, timeout).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15")
        )
        return self.browser.find_element(By.CSS_SELECTOR, ".screen").text
