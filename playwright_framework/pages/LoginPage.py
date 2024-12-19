from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_login(self):
        self.page.get_by_role("link", name="Signup / Login").click()

    def login(self, email, password):
        self.page.fill('input[data-qa="login-email"]', email)
        self.page.fill('input[data-qa="login-password"]', password)
        self.page.get_by_role("button", name="Login").click()

    def is_logged_in(self, username):
        return self.page.locator("a", has_text=f"Logged in as {username}").is_visible()
