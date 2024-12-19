import pytest
from playwright.sync_api import sync_playwright
from playwright_framework.pages.LoginPage import LoginPage


@pytest.fixture(scope="session")
def config():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        browser.close()


@pytest.fixture(scope="session")
def exec_login(config):
    page = config.new_page()
    page.goto("https://automationexercise.com/")

    # Realizar login
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("conectaautomation@email.com", "senharuim")
    assert login_page.is_logged_in("Automacao"), "Falha ao logar."

    yield page
    page.close()
