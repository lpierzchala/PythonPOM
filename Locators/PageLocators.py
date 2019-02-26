from selenium.webdriver.common.by import By


class HomePageLocators():
    SIGN_IN = (By.LINK_TEXT, ('Sign in'))


class NavigationLocators():
    WOMEN = (By.XPATH, ('//*[@id="block_top_menu"]//a[@title="Women"]'))
    DRESSES = (By.XPATH, ('//*[@id="block_top_menu"]//a[@title="Dresses"]'))
    TSHIRTS = (By.XPATH, ('//*[@id="block_top_menu"]//a[@title="T-SHIRTS"]'))


class LoginPageLocators():
    EMAIL_CREATE = (By.CSS_SELECTOR, ('#email_create'))
    EMAIL_INPUT = (By.CSS_SELECTOR, ('#email'))
    PASSWORD_INPUT = (By.CSS_SELECTOR, ('#passwd'))
    CREATE_BUTTON = (By.CSS_SELECTOR, ('#SubmitCreate'))
    LOGIN_BUTTON = (By.CSS_SELECTOR, ('#SubmitLogin'))
