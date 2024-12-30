from selenium_framework.pages.PageObject import PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(PageObject):
    checkout_link = "https://automationexercise.com/checkout"
    payment_btn = (By.CSS_SELECTOR, 'a[href="/payment"]')
    card_name_input = (By.CSS_SELECTOR, 'input[data-qa="name-on-card"]')
    card_number_input = (By.CSS_SELECTOR, 'input[data-qa="card-number"]')
    card_cvc_input = (By.CSS_SELECTOR, 'input[data-qa="cvc"]')
    card_exp_month_input = (By.CSS_SELECTOR, 'input[data-qa="expiry-month"]')
    card_exp_year_input = (By.CSS_SELECTOR, 'input[data-qa="expiry-year"]')
    submit_btn = (By.ID, "submit")
    order_result = (By.CSS_SELECTOR, 'h2[data-qa="order-placed"]')


    def __init__(self, driver):
        super(CheckoutPage, self).__init__(driver=driver)

    def open_checkout_page(self):
        self.driver.get(self.checkout_link)

    def place_order(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*self.payment_btn))
        self.driver.find_element(*self.payment_btn).click()

    def enter_payment_details(self, payment_info: dict):
        self.driver.find_element(*self.card_name_input).send_keys(payment_info.get("name_on_card"))
        self.driver.find_element(*self.card_number_input).send_keys(payment_info.get("card_number"))
        self.driver.find_element(*self.card_cvc_input).send_keys(payment_info.get("cvc"))
        self.driver.find_element(*self.card_exp_month_input).send_keys(payment_info.get("expiry_month"))
        self.driver.find_element(*self.card_exp_year_input).send_keys(payment_info.get("expiry_year"))
        self.driver.find_element(*self.submit_btn).click()

    def is_order_placed(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_element(*self.order_result)))
        return self.driver.find_element(*self.order_result).text == "ORDER PLACED!"