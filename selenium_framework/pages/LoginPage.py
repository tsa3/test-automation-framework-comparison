from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_framework.pages.PageObject import PageObject


class LoginPage(PageObject):
    email_input = (By.CSS_SELECTOR, 'input[data-qa="login-email"]')
    password_input = (By.CSS_SELECTOR, 'input[data-qa="login-password"]')
    signup_login_link = (By.LINK_TEXT, "Signup / Login")
    login_button = (By.CSS_SELECTOR,  'button[data-qa="login-button"]')
    logged_in_as = (By.XPATH, '//a[i[@class="fa fa-user"]]')

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)

    def navigate_to_login(self):
        self.driver.find_element(*self.signup_login_link).click()

    def login(self, email: str, password: str):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_logged_in(self, username: str) -> bool:
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_element(*self.logged_in_as)))
        return f"Logged in as {username}" in self.driver.find_element(*self.logged_in_as).text
