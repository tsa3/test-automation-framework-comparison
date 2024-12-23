from playwright.sync_api import Page

class LogoutPage:
    LOGOUT_BTN = 'a[href="/logout"]'
    LOGIN_FORM_INPUT = ".login-form"

    def __init__(self, page: Page):
        self.page = page

    def logout(self):
        self.page.click(self.LOGOUT_BTN)

    def is_logged_out(self):
        return self.page.locator(self.LOGIN_FORM_INPUT).is_visible()
