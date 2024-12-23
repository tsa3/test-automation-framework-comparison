from playwright.sync_api import Page


class CartPage:
    PRODUCTS_PAGE_LINK = 'a[href="/products"]'
    CART_PAGE_LINK = 'a[href="/view_cart"]'
    PROCEED_TO_CHECKOUT = 'a:has-text("Proceed To Checkout")'
    MODAL_MESSAGE = 'h4.modal-title.w-100'
    MODAL_CLOSE_BUTTON = 'button[data-dismiss="modal"]'
    CHECKOUT_PAGE_HEADER = 'h2:has-text("Address Details")'

    def __init__(self, page: Page):
        self.page = page

    def add_product_to_cart(self, product_id):
        self.page.click(f'a[data-product-id="{product_id}"]')

    def open_products_page(self):
        self.page.click(self.PRODUCTS_PAGE_LINK)

    def go_to_cart(self):
        self.page.click(self.CART_PAGE_LINK)

    def proceed_to_checkout(self):
        self.page.click(self.PROCEED_TO_CHECKOUT)

    def is_product_added(self):
        modal_message = self.page.locator(self.MODAL_MESSAGE).text_content()
        self.page.click(self.MODAL_CLOSE_BUTTON)
        return modal_message == "Added!"

    def is_checkout_page(self):
        return self.page.locator(self.CHECKOUT_PAGE_HEADER).is_visible()
