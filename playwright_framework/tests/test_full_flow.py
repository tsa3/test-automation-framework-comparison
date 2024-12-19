import pytest
from playwright_framework.pages.CartPage import CartPage
from playwright_framework.pages.CheckoutPage import CheckoutPage
from playwright_framework.pages.LogoutPage import LogoutPage


@pytest.mark.usefixtures("exec_login")
class TestUserFlow:
    def test_add_product_to_cart(self, exec_login):
        cart_page = CartPage(exec_login)
        cart_page.add_product_to_cart(product_id="1")
        assert cart_page.is_product_added(), "Produto não adicionado no carrinho"

    def test_proceed_to_checkout(self, exec_login):
        cart_page = CartPage(exec_login)
        cart_page.go_to_cart()
        cart_page.proceed_to_checkout()
        assert cart_page.is_checkout_page, "Página de checkout não foi exibida."

    def test_place_order(self, exec_login):
        checkout_page = CheckoutPage(exec_login)
        checkout_page.open_checkout_page()
        checkout_page.place_order()
        checkout_page.enter_payment_details(
            name_on_card="Nome Fantasia",
            card_number="0123456789012345",
            cvc="727",
            expiry_month="11",
            expiry_year="2034"
        )
        assert checkout_page.is_order_placed(), "O pedido não foi concluído."

    def test_logout(self, exec_login):
        logout_page = LogoutPage(exec_login)
        logout_page.logout()
        assert logout_page.is_logged_out(), "Logout não foi realizado corretamente."
