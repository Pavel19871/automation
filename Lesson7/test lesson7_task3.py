from selenium import webdriver
from pages.login import LoginPage
from pages.shopping import Shopping
from pages.my_cart import MyCart
from pages.checkout import CheckOut
from pages.finale import FinalPage


def test_price_check():
    browser = webdriver.Firefox()
    login_page = LoginPage(browser)
    shopping = Shopping(browser)
    my_cart = MyCart(browser)
    checkout = CheckOut(browser)
    finale = FinalPage(browser)
    login_page.sign_up()
    shopping.add_cart()
    shopping.to_cart()
    my_cart.checkout()
    checkout.add_info("Pavel", "Lomakin", "457000")
    checkout.button_continue()
    finale.cheking_price()
    assert "58.29" in finale.cheking_price()
    browser.quit()