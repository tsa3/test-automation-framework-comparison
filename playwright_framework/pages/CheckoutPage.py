from playwright.sync_api import Page, Locator

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.payment_btn: Locator = page.locator('a[href="/payment"]')
        self.card_name_input: Locator = page.locator('input[data-qa="name-on-card"]')
        self.card_number_input: Locator = page.locator('input[data-qa="card-number"]')
        self.card_cvc_input: Locator = page.locator('input[data-qa="cvc"]')
        self.card_exp_month_input: Locator = page.locator('input[data-qa="expiry-month"]')
        self.card_exp_year_input: Locator = page.locator('input[data-qa="expiry-year"]')
        self.submit_btn: Locator = page.locator("#submit")
        self.order_result: Locator = page.locator('h2[data-qa="order-placed"]')

    def place_order(self):
        self.payment_btn.click()

    def enter_payment_details(self, payment_info: dict):
        self.card_name_input.fill(payment_info.get("name_on_card", ""))
        self.card_number_input.fill(payment_info.get("card_number", ""))
        self.card_cvc_input.fill(payment_info.get("cvc", ""))
        self.card_exp_month_input.fill(payment_info.get("expiry_month", ""))
        self.card_exp_year_input.fill(payment_info.get("expiry_year", ""))
        self.submit_btn.click()

    def is_order_placed(self):
        self.order_result.wait_for(state='visible')
        return self.order_result.text_content() == "Order Placed!"
