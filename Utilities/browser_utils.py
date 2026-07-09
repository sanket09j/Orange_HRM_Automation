from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Utilities.config_reader import ConfigReader


class BrowserUtils:

    @staticmethod
    def get_driver(browser=None):

        if browser is None:
            browser = ConfigReader.get_browser()

        browser = browser.lower()

        # ---------------- Chrome ---------------- #

        if browser == "chrome":

            options = ChromeOptions()

            if ConfigReader.get_headless():
                options.add_argument("--headless=new")

            driver = webdriver.Chrome(
                service=ChromeService(
                    ChromeDriverManager().install()
                ),
                options=options
            )

        # ---------------- Edge ---------------- #

        elif browser == "edge":

            options = EdgeOptions()

            if ConfigReader.get_headless():
                options.add_argument("--headless=new")

            driver = webdriver.Edge(
                service=EdgeService(
                    EdgeChromiumDriverManager().install()
                ),
                options=options
            )

        else:

            raise Exception(
                f"{browser} browser is not supported"
            )

        driver.maximize_window()

        driver.implicitly_wait(
            ConfigReader.get_implicit_wait()
        )

        return driver