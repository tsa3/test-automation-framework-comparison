from modulefinder import packagePathMap
from multiprocessing.connection import wait
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    #Access page
    page.goto("https://automationexercise.com/")
    print(page.title())

    #Login
    page.get_by_role("link", name=" Signup / Login").click()
    # page.get_by_title("Log in to your customer account").click()
    page.fill('input[data-qa="login-email"]', "conectaautomation@email.com")
    page.fill('input[data-qa="login-password"]', "senharuim")
    page.get_by_role("button", name="Login").click()
    print(page.title())
    assert page.locator("a", has_text="Logged in as Automacao").is_visible(),"Falha ao logar"

    #Add to cart
    page.click('a[data-product-id="1"]')
    print(page.locator('h4.modal-title.w-100').text_content())
    assert page.locator('h4.modal-title.w-100').text_content() == "Added!", "Produto não adicionado no carrinho"
    page.click('button[data-dismiss="modal"]')

    #go to cart
    page.click('a[href="/view_cart"]')
    page.locator("a", has_text="Proceed To Checkout").click()
    page.click('a[href="/payment"]')

    page.fill('input[data-qa="name-on-card"]', "Nome Fantasia")
    page.fill('input[data-qa="card-number"]', "0123456789012345")
    page.fill('input[data-qa="cvc"]', "727")
    page.fill('input[data-qa="expiry-month"]', "11")
    page.fill('input[data-qa="expiry-year"]', "2034")
    page.click('#submit')
    page.locator('h2[data-qa="order-placed"]').wait_for(state='visible')
    assert page.locator('h2[data-qa="order-placed"]').text_content() == "Order Placed!", "Failed to order"

    # #Logout
    page.click('a[href="/logout"]')
    assert page.locator(".login-form").is_visible(), "Logout não pode ser efetuado."
