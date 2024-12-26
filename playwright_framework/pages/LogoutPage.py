from playwright.sync_api import Page, Locator

class LogoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.logout_button: Locator = page.locator('a[href="/logout"]')
        self.login_form_input: Locator = page.locator(".login-form")

    def logout(self):
        self.logout_button.click()

    def is_logged_out(self) -> bool:
        return self.login_form_input.is_visible()
