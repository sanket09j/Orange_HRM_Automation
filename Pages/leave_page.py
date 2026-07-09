from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
from Utilities.logger import LogGen


logger = LogGen.get_logger()


class LeavePage(BasePage):

    # ---------------- Menu ---------------- #

    LEAVE_MENU = (
        By.XPATH,
        "//span[normalize-space()='Leave']"
    )

    APPLY_MENU = (
        By.XPATH,
        "//a[normalize-space()='Apply']"
    )

    MY_LEAVE_MENU = (
        By.XPATH,
        "//a[normalize-space()='My Leave']"
    )

    LEAVE_LIST_MENU = (
        By.XPATH,
        "//a[normalize-space()='Leave List']"
    )

    # ---------------- Page Headers ---------------- #

    APPLY_HEADER = (
        By.XPATH,
        "//h6[contains(normalize-space(),'Apply Leave')]"
    )

    MY_LEAVE_HEADER = (
        By.XPATH,
        "//h5[contains(normalize-space(),'My Leave')]"
    )

    LEAVE_LIST_HEADER = (
        By.XPATH,
        "//h5[contains(normalize-space(),'Leave List')]"
    )

    def __init__(self, driver):
        super().__init__(driver)

    # ---------------- Open Leave ---------------- #

    def open_leave(self):

        logger.info("Opening Leave Module")

        self.click(self.LEAVE_MENU)

    def open_apply_leave(self):

        logger.info("Opening Apply Leave")

        self.click(self.APPLY_MENU)

    def open_my_leave(self):

        logger.info("Opening My Leave")

        self.click(self.MY_LEAVE_MENU)

    def open_leave_list(self):

        logger.info("Opening Leave List")

        self.click(self.LEAVE_LIST_MENU)

    # ---------------- Verification ---------------- #

    def is_apply_page_displayed(self):

        logger.info("Verifying Apply Leave Page")

        return self.is_element_displayed(
            self.APPLY_HEADER
        )

    def is_my_leave_page_displayed(self):

        logger.info("Verifying My Leave Page")

        return self.is_element_displayed(
            self.MY_LEAVE_HEADER
        )

    def is_leave_list_displayed(self):

        logger.info("Verifying Leave List Page")

        return self.is_element_displayed(
            self.LEAVE_LIST_HEADER
        )