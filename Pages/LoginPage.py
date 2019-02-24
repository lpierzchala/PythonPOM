from Pages.BasePage import BasePage
from Locators.PageLocators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LoginPageLocators()

    def add_new_user(self, email=""):
        self.findElement(self.locator.EMAIL_CREATE).send_keys(email)
        self.findElement(self.locator.CREATE_BUTTON).click()

    def loginAs(self, user='', password=''):
        self.fillWithValue(self.locator.EMAIL_INPUT, user)
        self.fillWithValue(self.locator.PASSWORD_INPUT, password)
        self.findElement(self.locator.LOGIN_BUTTON).click()

    def isInvalidPasowrdSet(self):
        return self.driver.find_element_by_link_text("Invalid password.")
