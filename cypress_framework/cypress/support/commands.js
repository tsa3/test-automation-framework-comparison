import LoginPage from '../pages/LoginPage';

Cypress.Commands.add('login', (email, password, username) => {
    const loginPage = new LoginPage();
    loginPage.navigateToLogin();
    loginPage.login(email, password);
    loginPage.isLoggedIn(username);
  });