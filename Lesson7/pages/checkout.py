from selenium.webdriver.common.by import By


class CheckOut:
    def __init__(self, driver):
        self._driver = driver

    def add_info(self, first_name, last_name, zip):
        self._driver.find_element(By.CSS_SELECTOR, "input#first-name").send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, "input#last-name").send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, "input#postal-code").send_keys(zip)

    def button_continue(self):
        self._driver.find_element(By.CSS_SELECTOR, "input#continue").click()    