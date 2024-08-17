from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:
    def __init__(self, browser):
        self._driver = browser

    def check_element_color(self, locator):
        WebDriverWait(self._driver, 4).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert")))
        color = self._driver.find_element(By.CSS_SELECTOR, locator).value_of_css_property("color")
        return color  