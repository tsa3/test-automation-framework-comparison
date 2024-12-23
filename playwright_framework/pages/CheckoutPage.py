from playwright.sync_api import Page

class CheckoutPage:
    CHECKOUT_LINK = "https://automationexercise.com/checkout"
    PAYMENT_BTN_LINK = 'a[href="/payment"]'
    CARD_NAME_INPUT = 'input[data-qa="name-on-card"]'
    CARD_NUMBER_INPUT = 'input[data-qa="card-number"]'
    CARD_CVC_INPUT = 'input[data-qa="cvc"]'
    CARD_EXP_MONTH_INPUT = 'input[data-qa="expiry-month"]'
    CARD_EXP_YEAR_INPUT = 'input[data-qa="expiry-year"]'
    SUBMIT_BTN = "#submit"
    ORDER_RESULT = 'h2[data-qa="order-placed"]'

    def __init__(self, page: Page):
        self.page = page

    def open_checkout_page(self):
        self.page.goto(self.CHECKOUT_LINK)

    def place_order(self):
        self.page.click(self.PAYMENT_BTN_LINK)

    def enter_payment_details(self, name_on_card, card_number, cvc, expiry_month, expiry_year):
        self.page.fill(self.CARD_NAME_INPUT, name_on_card)
        self.page.fill(self.CARD_NUMBER_INPUT, card_number)
        self.page.fill(self.CARD_CVC_INPUT, cvc)
        self.page.fill(self.CARD_EXP_MONTH_INPUT, expiry_month)
        self.page.fill(self.CARD_EXP_YEAR_INPUT, expiry_year)
        self.page.click(self.SUBMIT_BTN)

    def is_order_placed(self):
        self.page.locator(self.ORDER_RESULT).wait_for(state='visible')
        return self.page.locator(self.ORDER_RESULT).text_content() == "Order Placed!"
