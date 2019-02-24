from Locators.PageLocators import NavigationLocators
from Pages.BasePage import BasePage


class Navigation(BasePage):

    def __init__(self, driver):
        super(Navigation).__init__(driver)
        self.locator = NavigationLocators()

    def navigateTo(self, locator):
        self.findElement(locator).click()
