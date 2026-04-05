from selenium import webdriver
from pages.CalcPage import CalcPage


def test_slow_calculator():
    browser = webdriver.Chrome()
    calc = CalcPage(browser)

    calc.set_delay(45)
    calc.click_button('7')
    calc.click_button('+')
    calc.click_button('8')
    calc.click_button('=')

    result = calc.get_result(50)

    assert result == '15'

    browser.quit()
