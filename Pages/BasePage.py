from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(self.URL)

    def findElement(self, locator, timeout=30):
        '''Find element for given locator'''
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print('Timeout: Cannot find element defined by selector')
            return False

    def fillWithValue(self, value, locator=None, element=None):
        '''Set value for element for given locator or WebElemnet'''
        if locator:
            element = self.findElement(locator)
        element.clear()
        element.send_keys(value)

    def selectElementFromList(self, locator, param_name=""):
        """Select element from dropdown list"""
        try:
            Select(self.driver.find_element(locator).select_by_visible_text(param_name))
        except NoSuchElementException:
            print(f"There is no {param_name} on the list")

    def getTitle(self):
        return self.driver.title

    def makePageScreenshot(self):
        fileName = "screenshots/" + str(self.id()) + '.png'
