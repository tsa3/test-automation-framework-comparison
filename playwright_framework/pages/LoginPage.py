from playwright.sync_api import Page

class LoginPage:
    EMAIL_INPUT = 'input[data-qa="login-email"]'
    PWD_INPUT = 'input[data-qa="login-password"]'
    SIGNUP_LOGIN_LINK = {"role": "link", "name": "Signup / Login"}
    LOGIN_BTN = {"role": "button", "name": "Login"}
    
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_login(self):
        self.page.get_by_role(**self.SIGNUP_LOGIN_LINK).click()

    def login(self, email, password):
        self.page.fill(self.EMAIL_INPUT, email)
        self.page.fill(self.PWD_INPUT, password)
        self.page.get_by_role(**self.LOGIN_BTN).click()

    def is_logged_in(self, username):
        return self.page.locator("a", has_text=f"Logged in as {username}").is_visible()
