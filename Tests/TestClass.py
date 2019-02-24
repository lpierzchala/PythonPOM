from selenium import webdriver
import unittest
from Pages.HomePage import HomePage
import sys

class TestClass(unittest.TestCase):

    def setUp(self):
        self.driverPath = r"C:\Users\lpierzchala\Desktop\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.driverPath,
                                       service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])

    def test01_loginWithInvalidPassword(self):
        homePage = HomePage(self.driver)
        homePage.visit()
        assert ("My Store" in homePage.getTitle())
        loginPage = homePage.goToLoginPage()
        loginPage.loginAs('test@example.com', 'password')
        assert loginPage.isInvalidPasowrdSet()

    def tearDown(self):
        if sys.exc_info()[0]:
            # Save screenshot if test is failed
            self.driver.save_screenshot(str(self.id()) + '.png')
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
