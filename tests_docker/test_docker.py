from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
import allure


@pytest.fixture(scope='class')
def web_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class TestGoogle:

    @allure.feature('Test')
    @allure.story('Check url')
    def test_url(self, web_driver):
        with allure.step('Find current url'):
            current_url = web_driver.current_url
            assert current_url == "https://www.google.com/"
