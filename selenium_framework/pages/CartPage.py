from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_framework.pages.PageObject import PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class CartPage(PageObject):
    products_page_link = (By.CSS_SELECTOR, 'a[href ="/products"]')
    cart_page_link = (By.CSS_SELECTOR, 'a[href ="/view_cart"]')
    proceed_to_checkout_button = (By.CLASS_NAME, 'check_out')
    modal_message = (By.CSS_SELECTOR, 'h4.modal-title.w-100')
    modal_close_button = (By.CSS_SELECTOR, 'button[data-dismiss="modal"]')
    checkout_page_header = (By.CSS_SELECTOR, 'h2:has-text("Address Details")')

    def __init__(self, driver):
        super(CartPage, self).__init__(driver=driver)

    def add_product_to_cart(self, product_id):
        product = self.driver.find_element(By.CSS_SELECTOR, f'a[data-product-id="{product_id}"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", product)
        product.click()

    def open_products_page(self):
        self.driver.find_element(*self.products_page_link).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_page_link).click()

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.proceed_to_checkout_button))
        self.driver.find_element(*self.proceed_to_checkout_button).click()

    def is_product_added(self) -> bool:
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.modal_message)
        )
        modal_element = self.driver.find_element(*self.modal_message).text
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.modal_close_button))
        self.driver.find_element(*self.modal_close_button).click()
        return modal_element == "Added!"

    def is_checkout_page(self) -> bool:
        return self.driver.find_element(*self.checkout_page_header).is_displayed()