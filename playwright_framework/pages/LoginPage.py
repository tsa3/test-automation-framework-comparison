from playwright.sync_api import Page, Locator

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input: Locator = page.locator('input[data-qa="login-email"]')
        self.password_input: Locator = page.locator('input[data-qa="login-password"]')
        self.signup_login_link: Locator = page.get_by_role("link", name="Signup / Login")
        self.login_button: Locator = page.get_by_role("button", name="Login")
        self.logged_in_as: Locator = page.locator("a")

    def navigate_to_login(self):
        self.signup_login_link.click()

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def is_logged_in(self, username: str) -> bool:
        return self.logged_in_as.filter(has_text=f"Logged in as {username}").is_visible()
