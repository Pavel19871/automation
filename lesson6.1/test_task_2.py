
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_answer_appears(browser):
    WebDriverWait(browser, 30)
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    browser.refresh()
    browser.find_element(By.CSS_SELECTOR, "input#delay").clear()
    browser.find_element(By.CSS_SELECTOR, "input#delay").send_keys("45")
    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    browser.find_element(By.XPATH, "//span[text()='=']").click()
    WebDriverWait(browser, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
    text = browser.find_element(By.CSS_SELECTOR, "div.screen").text
    assert text == "15"
    
    
    
    