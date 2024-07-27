from selenium.webdriver.common.by import By


class FinalPage:
    def __init__(self, driver):
        self._driver = driver

    def cheking_price(self):
        total = self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        return total