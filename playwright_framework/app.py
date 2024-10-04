from modulefinder import packagePathMap
from multiprocessing.connection import wait
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    #Access page
    page.goto("http://www.automationpractice.pl/index.php")
    print(page.title())

    #Login
    page.get_by_title("Log in to your customer account").click()
    page.fill("#email", "conectaautomation@email.com")
    page.fill("#passwd", "senharuim")
    page.get_by_role("button", name="Sign in").click()
    print(page.title())

    #Add to cart
    page.goto("http://www.automationpractice.pl/index.php")
    page.get_by_title("Women").click()
    page.get_by_title("Blouse").click()
    page.get_by_title("White").click()
    page.click('#add_to_cart')

    #Logout
    page.get_by_title("Log me out").click()
    print(page.title())
