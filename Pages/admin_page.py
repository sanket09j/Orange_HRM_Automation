from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from Pages.base_page import BasePage
from Utilities.logger import LogGen

logger = LogGen.get_logger()


class AdminPage(BasePage):

    ADMIN_MENU = (
    By.XPATH,
    "//span[normalize-space()='Admin']"
)

    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")

    USER_ROLE_DROPDOWN = (
        By.XPATH,
        "(//div[contains(@class,'oxd-select-text')])[1]"
    )

    USER_ROLE_ADMIN = (
        By.XPATH,
        "//div[@role='listbox']//span[text()='Admin']"
    )

    EMPLOYEE_NAME = (
        By.XPATH,
        "//input[@placeholder='Type for hints...']"
    )

    EMPLOYEE_OPTIONS = (
        By.XPATH,
        "//div[contains(@class,'oxd-autocomplete-option')]"
    )

    STATUS_DROPDOWN = (
        By.XPATH,
        "(//div[contains(@class,'oxd-select-text')])[2]"
    )

    STATUS_ENABLED = (
        By.XPATH,
        "//div[@role='listbox']//span[text()='Enabled']"
    )

    USERNAME = (
        By.XPATH,
        "(//input[contains(@class,'oxd-input')])[2]"
    )

    PASSWORD = (
        By.XPATH,
        "(//input[@type='password'])[1]"
    )

    CONFIRM_PASSWORD = (
        By.XPATH,
        "(//input[@type='password'])[2]"
    )

    SAVE_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    SEARCH_USERNAME = (
        By.XPATH,
        "(//input[contains(@class,'oxd-input')])[2]"
    )

    SEARCH_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def open_admin(self):
        logger.info("Opening Admin Module")
        self.click(self.ADMIN_MENU)

    def click_add(self):
        logger.info("Clicking Add Button")
        self.click(self.ADD_BUTTON)

    def select_admin_role(self):
        logger.info("Selecting Admin Role")
        self.click(self.USER_ROLE_DROPDOWN)
        self.click(self.USER_ROLE_ADMIN)

    def enter_employee_name(self):

        logger.info("Selecting First Available Employee")

        textbox = self.wait.until(
            EC.visibility_of_element_located(
                self.EMPLOYEE_NAME
            )
        )

        textbox.clear()

        textbox.send_keys("a")

        options = self.wait.until(
            EC.visibility_of_all_elements_located(
                self.EMPLOYEE_OPTIONS
            )
        )

        ActionChains(self.driver).move_to_element(
            options[0]
        ).click().perform()

    def select_status(self):
        logger.info("Selecting Enabled")
        self.click(self.STATUS_DROPDOWN)
        self.click(self.STATUS_ENABLED)

    def enter_username(self, username):
        self.enter_text(self.USERNAME, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD, password)

    def enter_confirm_password(self, password):
        self.enter_text(self.CONFIRM_PASSWORD, password)

    def click_save(self):
        self.click(self.SAVE_BUTTON)

    def search_username(self, username):
        self.enter_text(self.SEARCH_USERNAME, username)

    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    def add_user(self, username, password):

        self.click_add()

        self.select_admin_role()

        self.enter_employee_name()

        self.select_status()

        self.enter_username(username)

        self.enter_password(password)

        self.enter_confirm_password(password)

        self.click_save()