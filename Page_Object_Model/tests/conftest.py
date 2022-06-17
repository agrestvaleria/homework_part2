# В этой домашней работе, Вы должны начать описывать страницы нашего сайта
# из финального задания в стиле PO. http://automationpractice.com/index.php
#
# Необходимо описать 3 страницы:
#
# Главная страница.
# Страница логина.
# Старница корзины.
# В каждом классе должны быть проверки, которые однозначно проверяют,
# является ли данная страница ожидаемой. Так же 2 теста:
#
# при переходе с главной страницы на страницу корзины и проверка на то, что корзина пуста.
# при переходе с главной страницы на страницу логина и проверка на то, что мы на странице логина.
# Тесты могут быть как позитивные, так и негативные.


import pytest
from selenium import webdriver
from tests.Page_Object_Model.pages.Login_page import LoginPage
from tests.Page_Object_Model.pages.Main_page import MainPage
from tests.Page_Object_Model.pages.Cart_page import CartPage


@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
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
