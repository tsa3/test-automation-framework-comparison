from playwright.sync_api import Page

class LogoutPage:
    def __init__(self, page: Page):
        self.page = page

    def logout(self):
        self.page.click('a[href="/logout"]')

    def is_logged_out(self):
        return self.page.locator(".login-form").is_visible()
