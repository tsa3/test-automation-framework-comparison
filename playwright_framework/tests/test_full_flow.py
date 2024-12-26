import pytest
import json
import os
from playwright_framework.pages.CartPage import CartPage
from playwright_framework.pages.CheckoutPage import CheckoutPage
from playwright_framework.pages.LogoutPage import LogoutPage


@pytest.mark.usefixtures("exec_login")
class TestUserFlow:
    @pytest.fixture(autouse=True)
    def setup_pages(self, exec_login):
        self.cart_page = CartPage(exec_login)
        self.checkout_page = CheckoutPage(exec_login)
        self.logout_page = LogoutPage(exec_login)

    @pytest.fixture
    def card_info(self):
        with open("D:\camil\Documents\Conecta\Test-Automation-Framework-Comparison\playwright_framework\card_info.json") as f:
            d = json.load(f)
            return d

    def test_add_product_to_cart(self):
        self.cart_page.add_product_to_cart(product_id="1")
        assert self.cart_page.is_product_added(), "Produto não adicionado no carrinho"

    def test_proceed_to_checkout(self):
        self.cart_page.go_to_cart()
        self.cart_page.proceed_to_checkout()
        assert self.cart_page.is_checkout_page, "Página de checkout não foi exibida."

    def test_place_order(self, card_info):
        self.checkout_page.open_checkout_page()
        self.checkout_page.place_order()
        self.checkout_page.enter_payment_details(card_info)
        assert self.checkout_page.is_order_placed(), "O pedido não foi concluído."

    def test_logout(self):
        self.logout_page.logout()
        assert self.logout_page.is_logged_out(), "Logout não foi realizado corretamente."
