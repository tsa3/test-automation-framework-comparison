class LoginPage {
    constructor() {
      this.emailInput = 'input[data-qa="login-email"]';
      this.passwordInput = 'input[data-qa="login-password"]';
      this.signupLoginLink = 'a:contains("Signup / Login")';
      this.loginButton = 'button:contains("Login")';
      this.loggedInAs = 'a';
    }
  
    navigateToLogin() {
      cy.get(this.signupLoginLink).click();
    }
  
    login(email, password) {
      cy.get(this.emailInput).type(email);
      cy.get(this.passwordInput).type(password);
      cy.get(this.loginButton).click();
    }
  
    isLoggedIn(username) {
      cy.get(this.loggedInAs).contains(`Logged in as ${username}`).should('be.visible');
    }
  }
  
  export default LoginPage;
  