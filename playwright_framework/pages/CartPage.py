from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def add_product_to_cart(self, product_id):
        self.page.click(f'a[data-product-id="{product_id}"]')

    def open_products_page(self):
        self.page.click('a[href="/products"]')

    def go_to_cart(self):
        self.page.click('a[href="/view_cart"]')

    def proceed_to_checkout(self):
        self.page.locator("a", has_text="Proceed To Checkout").click()

    def is_product_added(self):
        modal_message = self.page.locator('h4.modal-title.w-100').text_content()
        self.page.click('button[data-dismiss="modal"]')
        return modal_message == "Added!"

    def is_checkout_page(self):
        return self.page.locator('h2', has_text="Address Details").is_visible()
