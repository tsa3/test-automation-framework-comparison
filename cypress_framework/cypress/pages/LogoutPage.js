class LogoutPage {
    constructor() {
      this.logoutButton = 'a[href="/logout"]';
      this.loginFormInput = '.login-form';
    }
  
    logout() {
      cy.get(this.logoutButton).click();
    }
  
    isLoggedOut() {
      cy.get(this.loginFormInput).should('be.visible');
    }
  }
  
  export default LogoutPage;
  