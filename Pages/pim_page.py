from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
from Utilities.logger import LogGen


logger = LogGen.get_logger()


class PIMPage(BasePage):

    # ---------------- Menu ---------------- #

    PIM_MENU = (By.XPATH, "//span[text()='PIM']")

    EMPLOYEE_LIST = (
        By.XPATH,
        "//a[normalize-space()='Employee List']"
    )

    ADD_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Add']"
    )

    # ---------------- Add Employee ---------------- #

    FIRST_NAME = (By.NAME, "firstName")

    MIDDLE_NAME = (By.NAME, "middleName")

    LAST_NAME = (By.NAME, "lastName")

    SAVE_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    # ---------------- Employee List ---------------- #

    EMPLOYEE_INFORMATION_HEADER = (
        By.XPATH,
        "//h5[contains(normalize-space(),'Employee Information')]"
    )

    EMPLOYEE_NAME_SEARCH = (
        By.XPATH,
        "(//input[@placeholder='Type for hints...'])[1]"
    )

    SEARCH_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )

    def __init__(self, driver):
        super().__init__(driver)

    # ---------------- Open PIM ---------------- #

    def open_pim(self):

        logger.info("Opening PIM Module")

        self.click(self.PIM_MENU)

    # ---------------- Add Employee ---------------- #

    def click_add_employee(self):

        logger.info("Clicking Add Employee")

        self.click(self.ADD_BUTTON)

    def enter_first_name(self, first_name):

        logger.info(f"First Name : {first_name}")

        self.enter_text(
            self.FIRST_NAME,
            first_name
        )

    def enter_middle_name(self, middle_name):

        logger.info(f"Middle Name : {middle_name}")

        self.enter_text(
            self.MIDDLE_NAME,
            middle_name
        )

    def enter_last_name(self, last_name):

        logger.info(f"Last Name : {last_name}")

        self.enter_text(
            self.LAST_NAME,
            last_name
        )

    def click_save(self):

        logger.info("Saving Employee")

        self.click(self.SAVE_BUTTON)

    def add_employee(
            self,
            first_name,
            middle_name,
            last_name
    ):

        self.click_add_employee()

        self.enter_first_name(first_name)

        self.enter_middle_name(middle_name)

        self.enter_last_name(last_name)

        self.click_save()

    # ---------------- Employee List ---------------- #

    def open_employee_list(self):

        logger.info("Opening Employee List")

        self.click(self.EMPLOYEE_LIST)

    def is_employee_list_displayed(self):

        logger.info("Verifying Employee List Page")

        return self.is_element_displayed(
            self.EMPLOYEE_INFORMATION_HEADER
        )

    # ---------------- Search Employee ---------------- #

    def search_employee(self, employee_name):

        logger.info(f"Searching Employee : {employee_name}")

        self.enter_text(
            self.EMPLOYEE_NAME_SEARCH,
            employee_name
        )

        self.click(self.SEARCH_BUTTON)