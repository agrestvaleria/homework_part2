from tests.YourLogo.pages.Cart_page import CartPage
from tests.YourLogo.configs.config_parser import cart_empty, quantity


class TestCartPage:

    def test_cart_page(self, cart_page):
        result = cart_page.it_is_cart_page()
        assert result == CartPage.cart_url

    def test_cart_is_empty(self, cart_page):
        result = cart_page.cart_is_empty()
        assert result == cart_empty

    def test_cart_with_clothes(self, cart_page):
        result = cart_page.cart_with_clothes()
        assert result == quantity
