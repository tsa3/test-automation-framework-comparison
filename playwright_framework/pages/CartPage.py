from playwright.sync_api import Page, Locator


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.products_page_link: Locator = page.locator('a[href="/products"]')
        self.cart_page_link: Locator = page.locator('a[href="/view_cart"]')
        self.proceed_to_checkout_button: Locator = page.locator('a:has-text("Proceed To Checkout")')
        self.modal_message: Locator = page.locator('h4.modal-title.w-100')
        self.modal_close_button: Locator = page.locator('button[data-dismiss="modal"]')
        self.checkout_page_header: Locator = page.locator('h2:has-text("Address Details")')

    def add_product_to_cart(self, product_id):
        self.page.click(f'a[data-product-id="{product_id}"]')

    def open_products_page(self):
        self.products_page_link.click()

    def go_to_cart(self):
        self.cart_page_link.nth(0).click()

    def proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()

    def is_product_added(self) -> bool:
        modal_message = self.modal_message.text_content()
        self.modal_close_button.click()
        return modal_message.strip() == "Added!"

    def is_checkout_page(self) -> bool:
        return self.checkout_page_header.is_visible()