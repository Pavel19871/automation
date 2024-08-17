from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.refresh()
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def change_delay(self, term):
        self._delay = int(term)
        self._driver.find_element(By.CSS_SELECTOR, "input#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input#delay").send_keys(term)
        return term

    def do_math(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    def waiting_result(self):
        WebDriverWait(self._driver, self._delay+4).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
        result = self._driver.find_element(By.CSS_SELECTOR, "div.screen").text
        return result