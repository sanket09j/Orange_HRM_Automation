from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
from Utilities.logger import LogGen

logger = LogGen.get_logger()


class LoginPage(BasePage):

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    INVALID_CREDENTIALS = (
        By.XPATH,
        "//p[contains(@class,'oxd-alert-content-text')]"
    )

    REQUIRED_MESSAGE = (
        By.XPATH,
        "//span[contains(@class,'oxd-input-field-error-message')]"
    )

    PROFILE_MENU = (By.CLASS_NAME, "oxd-userdropdown-name")
    LOGOUT = (By.XPATH, "//a[text()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        logger.info("Entering Username")
        self.enter_text(self.USERNAME, username)

    def enter_password(self, password):
        logger.info("Entering Password")
        self.enter_text(self.PASSWORD, password)

    def click_login(self):
        logger.info("Clicking Login Button")
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_invalid_credentials_message(self):
        return self.get_text(self.INVALID_CREDENTIALS)

    def get_required_message(self):
        return self.get_text(self.REQUIRED_MESSAGE)

    def logout(self):
        self.click(self.PROFILE_MENU)
        self.click(self.LOGOUT)