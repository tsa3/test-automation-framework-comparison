import pytest
from selenium_framework.pages.LoginPage import LoginPage


@pytest.fixture(scope="session")
def config(request):
    browser_name = request.config.getoption("--browser_selenium", default="chrome")
    login_page = LoginPage(browser=browser_name)
    login_page.driver.set_window_size(1920, 1080)
    login_page.driver.get("https://automationexercise.com/")
    yield login_page  # Provide the initialized LoginPage to tests
    login_page.close()  # Quit the browser when the session ends


@pytest.fixture(scope="session")
def exec_login(config):
    login_page = config
    login_page.navigate_to_login()
    login_page.login("conectaautomation@email.com", "senharuim")
    assert login_page.is_logged_in("Automacao"), "Falha ao logar."
    yield login_page.driver
