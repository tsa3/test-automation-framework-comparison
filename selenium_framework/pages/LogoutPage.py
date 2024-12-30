from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_framework.pages.PageObject import PageObject

class LogoutPage(PageObject):
    logout_button = (By.CSS_SELECTOR, 'a[href="/logout"]')
    login_form_input = (By.CSS_SELECTOR, ".login-form")

    def __init__(self, driver):
        super(LogoutPage, self).__init__(driver = driver)

    def logout(self):
        self.driver.find_element(*self.logout_button).click()

    def is_logged_out(self) -> bool:
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_element(*self.login_form_input)))
        return self.driver.find_element(*self.login_form_input).is_displayed()
