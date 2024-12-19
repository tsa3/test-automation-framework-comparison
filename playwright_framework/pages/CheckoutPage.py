from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def open_checkout_page(self):
        self.page.goto("https://automationexercise.com/checkout")

    def place_order(self):
        self.page.click('a[href="/payment"]')

    def enter_payment_details(self, name_on_card, card_number, cvc, expiry_month, expiry_year):
        self.page.fill('input[data-qa="name-on-card"]', name_on_card)
        self.page.fill('input[data-qa="card-number"]', card_number)
        self.page.fill('input[data-qa="cvc"]', cvc)
        self.page.fill('input[data-qa="expiry-month"]', expiry_month)
        self.page.fill('input[data-qa="expiry-year"]', expiry_year)
        self.page.click('#submit')

    def is_order_placed(self):
        self.page.locator('h2[data-qa="order-placed"]').wait_for(state='visible')
        return self.page.locator('h2[data-qa="order-placed"]').text_content() == "Order Placed!"
