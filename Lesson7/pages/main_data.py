from selenium.webdriver.common.by import By

class MainData:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def add_data(self, data):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(data.get("first_name", ""))
        self._driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(data.get("last_name", ""))
        self._driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(data.get("address", ""))
        self._driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys(data.get("zip_code", ""))
        self._driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(data.get("city", ""))
        self._driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(data.get("country", ""))
        self._driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(data.get("email", ""))
        self._driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(data.get("phone", ""))
        self._driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(data.get("job_position", ""))
        self._driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(data.get("company", ""))

    def submit_button(self):
        self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()    