from selenium import webdriver
import pytest

@pytest.fixture(scope='session')
def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("–-disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-setuid-sandbox")
    driver = webdriver.Chrome(chrome_options=options, executable_path='chromedriver')

    # options = webdriver.ChromeOptions()
    # options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    # options.add_argument("--disable-gpu")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--remote-debugging-port=9222")
    # driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class TestGoogle:

    def test_url(self, web_driver):
        current_url = web_driver.current_url
        assert current_url == "https://www.google.com/"

    def test_title(self, web_driver):
        title = web_driver.title
        assert title == "Google"
