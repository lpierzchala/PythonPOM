from Pages.BasePage import BasePage
from Locators.PageLocators import HomePageLocators
from Pages.LoginPage import LoginPage


class HomePage(BasePage):
    URL = 'http://automationpractice.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HomePageLocators()

    def goToLoginPage(self):
        self.findElement(self.locator.SIGN_IN).click()
        return LoginPage(self.driver)
