from selenium.webdriver.common.by import By


class Shopping:
    def __init__(self, driver):
        self._driver = driver

    def add_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()

    def to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()       