class CartPage {
    constructor() {
      this.productsPageLink = 'a[href="/products"]';
      this.cartPageLink = 'a[href="/view_cart"]';
      this.proceedToCheckoutButton = 'a:contains("Proceed To Checkout")';
      this.modalMessage = 'h4.modal-title.w-100';
      this.modalCloseButton = 'button[data-dismiss="modal"]';
      this.checkoutPageHeader = 'h2:contains("Address Details")';
    }
  
    addProductToCart(productId) {
      cy.get(`a[data-product-id="${productId}"]`).first().click();
    }
  
    openProductsPage() {
      cy.get(this.productsPageLink).click();
    }
  
    goToCart() {
      cy.get(this.cartPageLink).first().click();
    }
  
    proceedToCheckout() {
      cy.get(this.proceedToCheckoutButton).click();
    }
  
    isProductAdded() {
      cy.get(this.modalMessage)
        .invoke('text')
        .then((text) => {
          expect(text.trim()).to.eq("Added!");
          cy.get(this.modalCloseButton).click();
        });
    }
  
    isCheckoutPage() {
      cy.get(this.checkoutPageHeader).should('be.visible');
    }
  }
  
  export default CartPage;
  