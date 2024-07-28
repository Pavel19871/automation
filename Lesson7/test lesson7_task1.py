from selenium import webdriver
import pytest
from pages.main_data import MainData
from pages.result_page import ResultPage

EXPECTED_COLOR = "rgb(15, 81, 50)"

@pytest.fixture(scope='module')
def driver():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()

test_data = {
    "first_name": "Иван",
    "last_name": "Петров",
    "address": "Ленина, 55-3",
    "zip_code": "",
    "city": "Москва",
    "country": "Россия",
    "email": "test@skypro.com",
    "phone": "+7985899998787",
    "job_position": "QA",
    "company": "SkyPro"
}

def format_message(element, color, expected=True):
    if expected:
        return f"Элемент: {element}, Ожидаемый цвет: {color}"
    else:
        return f"Элемент: {element}, Неожидаемый цвет: {color}"

@pytest.mark.parametrize('element, expect_color', [
    ("div#first-name", EXPECTED_COLOR), 
    ("div#last-name", EXPECTED_COLOR),
    ("div#address", EXPECTED_COLOR), 
    ("div#city", EXPECTED_COLOR), 
    ("div#country", EXPECTED_COLOR), 
    ("div#e-mail", EXPECTED_COLOR),
    ("div#phone", EXPECTED_COLOR), 
    ("div#job-position", EXPECTED_COLOR), 
    ("div#company", EXPECTED_COLOR)
])
def test_green_alerts(driver, element, expect_color):
    main_page = MainData(driver)
    main_page.add_data(test_data)
    main_page.submit_button()
    result_page = ResultPage(driver)
    color = result_page.check_element_color(element)
    assert color == expect_color, format_message(element, color)

@pytest.mark.parametrize('element', ["div#zip-code"])
def test_red_alert(driver, element):
    main_page = MainData(driver)
    main_page.add_data(test_data)
    main_page.submit_button()
    result_page = ResultPage(driver)
    color = result_page.check_element_color(element)
    assert color != EXPECTED_COLOR, format_message(element, color, expected=False)