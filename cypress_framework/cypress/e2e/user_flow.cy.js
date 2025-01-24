import CartPage from '../pages/CartPage';
import CheckoutPage from '../pages/CheckoutPage';
import LogoutPage from '../pages/LogoutPage';

describe('User Flow Tests', () => {
  const cartPage = new CartPage();
  const checkoutPage = new CheckoutPage();
  const logoutPage = new LogoutPage();

  beforeEach(() => {
    cy.session('userSession', () => {
      cy.visit('https://automationexercise.com/');
      cy.login('conectaautomation@email.com', 'senharuim', 'Automacao');
    });

    cy.visit('https://automationexercise.com/');
  });

  it('should add a product to the cart', () => {
    cartPage.addProductToCart('1');
    cartPage.isProductAdded();
  });

  it('should proceed to checkout', () => {
    cartPage.goToCart();
    cartPage.proceedToCheckout();
    cartPage.isCheckoutPage();
  });

  it('should place an order', () => {
    cartPage.goToCart();
    cartPage.proceedToCheckout();
    cy.fixture('card_info').then((cardInfo) => {
      checkoutPage.placeOrder();
      checkoutPage.enterPaymentDetails(cardInfo);
      checkoutPage.isOrderPlaced();
    });
  });

  it('should log out', () => {
    logoutPage.logout();
    logoutPage.isLoggedOut();
  });
});
