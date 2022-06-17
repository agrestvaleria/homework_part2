from tests.Page_Object_Model.pages.Main_page import MainPage
from tests.Page_Object_Model.configs.config_parser import search_string, tabs_names


class TestMainPage:

    def test_main_page(self, main_page):
        result = main_page.it_is_main_page()
        assert result == MainPage.main_url

    def test_search_bar(self, main_page):
        result = main_page.search_field()
        assert result == search_string

    def test_tabs(self, main_page):
        result = main_page.tabs()
        assert result == tabs_names
