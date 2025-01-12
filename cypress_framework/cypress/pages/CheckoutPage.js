class CheckoutPage {
    constructor() {
      this.paymentBtn = 'a[href="/payment"]';
      this.cardNameInput = 'input[data-qa="name-on-card"]';
      this.cardNumberInput = 'input[data-qa="card-number"]';
      this.cardCvcInput = 'input[data-qa="cvc"]';
      this.cardExpMonthInput = 'input[data-qa="expiry-month"]';
      this.cardExpYearInput = 'input[data-qa="expiry-year"]';
      this.submitBtn = '#submit';
      this.orderResult = 'h2[data-qa="order-placed"]';
    }
  
    placeOrder() {
      cy.get(this.paymentBtn).click();
    }
  
    enterPaymentDetails(paymentInfo) {
      if (paymentInfo.name_on_card) {
        cy.get(this.cardNameInput).type(paymentInfo.name_on_card);
      }
      if (paymentInfo.card_number) {
        cy.get(this.cardNumberInput).type(paymentInfo.card_number);
      }
      if (paymentInfo.cvc) {
        cy.get(this.cardCvcInput).type(paymentInfo.cvc);
      }
      if (paymentInfo.expiry_month) {
        cy.get(this.cardExpMonthInput).type(paymentInfo.expiry_month);
      }
      if (paymentInfo.expiry_year) {
        cy.get(this.cardExpYearInput).type(paymentInfo.expiry_year);
      }
      cy.get(this.submitBtn).click();
    }
  
    isOrderPlaced() {
      cy.get(this.orderResult).should('be.visible').and('have.text', 'Order Placed!');
    }
  }
  
  export default CheckoutPage;
  