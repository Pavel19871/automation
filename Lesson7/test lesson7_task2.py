from selenium import webdriver
from pages.calculator import Calculator


def test_calculator():
    browser = webdriver.Firefox()
    calculator = Calculator(browser)
    calculator.change_delay("45")
    calculator.do_math()
    calculator.waiting_result()
    assert calculator.waiting_result() == "15"
    browser.quit()  