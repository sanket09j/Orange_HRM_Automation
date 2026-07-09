import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.login_page import LoginPage
from Pages.pim_page import PIMPage
from Utilities.config_reader import ConfigReader


@pytest.fixture
def login_pim(setup):

    driver = setup

    driver.get(ConfigReader.get_base_url())

    # Wait until the username textbox is visible
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(LoginPage.USERNAME)
    )

    login = LoginPage(driver)

    login.login("Admin", "admin123")

    return driver

@pytest.mark.smoke
@pytest.mark.regression
def test_open_pim_module(login_pim):

    driver = login_pim

    pim = PIMPage(driver)

    pim.open_pim()

    assert "pim" in driver.current_url.lower()


@pytest.mark.regression
def test_open_employee_list(login_pim):

    driver = login_pim

    pim = PIMPage(driver)

    pim.open_pim()

    pim.open_employee_list()

    assert pim.is_employee_list_displayed()


@pytest.mark.sanity
def test_pim_page_title(login_pim):

    driver = login_pim

    pim = PIMPage(driver)

    pim.open_pim()

    assert "OrangeHRM" in driver.title