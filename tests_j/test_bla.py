import warnings
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def web_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                              options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class TestGoogle:

    def test_url(self, web_driver):
        current_url = web_driver.current_url
        assert current_url == "https://www.google.com/"
