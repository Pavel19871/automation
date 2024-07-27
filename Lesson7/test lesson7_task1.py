from selenium import webdriver
import pytest
from pages.main_data import MainData
from pages.result_page import ResultPage


@pytest.fixture(scope='module')
def driver():
    browser = webdriver.Firefox()
    main_page = MainData(browser)
    main_page.add_data()
    main_page.submit_button()
    yield browser
    browser.quit()


@pytest.mark.parametrize('element, expect_color', [("div#first-name", "rgb(15, 81, 50)"), ("div#last-name", "rgb(15, 81, 50)"),
("div#address", "rgb(15, 81, 50)"), ("div#city", "rgb(15, 81, 50)"), ("div#country", "rgb(15, 81, 50)"), ("div#e-mail", "rgb(15, 81, 50)"),
("div#phone", "rgb(15, 81, 50)"), ("div#job-position", "rgb(15, 81, 50)"), ("div#company", "rgb(15, 81, 50)")])
def test_green_alerts(driver, element, expect_color):
    result_page = ResultPage(driver)
    color = result_page.check_element_color(element)
    assert color == expect_color


@pytest.mark.parametrize('element', ["div#zip-code"])
def test_red_alert(driver, element):
    result_page = ResultPage(driver)
    color = result_page.check_element_color(element)
    assert color != "rgb(15, 81, 50)", "This one is red"  