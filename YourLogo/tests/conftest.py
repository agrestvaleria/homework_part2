import pytest
from selenium import webdriver
from tests.YourLogo.pages.Login_page import LoginPage
from tests.YourLogo.pages.Main_page import MainPage
from tests.YourLogo.pages.Cart_page import CartPage


@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def login_page(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    yield login_page
    browser.quit()


@pytest.fixture(scope="class")
def main_page(browser):
    main_page = MainPage(browser)
    main_page.main_page()
    yield main_page
    browser.quit()


@pytest.fixture(scope="class")
def cart_page(browser):
    cart_page = CartPage(browser)
    cart_page.open_cart_page()
    yield cart_page
    browser.quit()
