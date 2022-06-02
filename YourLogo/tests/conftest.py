import pytest
from selenium import webdriver
from YourLogo.pages.Login_page import LoginPage
from YourLogo.pages.Main_page import MainPage
from YourLogo.pages.Cart_page import CartPage
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import warnings


@pytest.fixture(scope="class")
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                              options=chrome_options)
    driver.set_window_size(1920, 1080)
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
