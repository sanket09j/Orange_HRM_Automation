import pytest

from Pages.login_page import LoginPage
from Pages.leave_page import LeavePage
from Utilities.config_reader import ConfigReader


@pytest.fixture
def login_leave(setup):

    driver = setup

    driver.get(ConfigReader.get_base_url())

    login = LoginPage(driver)

    login.login("Admin", "admin123")

    return driver


@pytest.mark.smoke
@pytest.mark.regression
def test_open_leave_module(login_leave):

    driver = login_leave

    leave = LeavePage(driver)

    leave.open_leave()

    assert "leave" in driver.current_url.lower()


@pytest.mark.regression
def test_open_apply_leave(login_leave):

    driver = login_leave

    leave = LeavePage(driver)

    leave.open_leave()

    leave.open_apply_leave()

    assert leave.is_apply_page_displayed()


@pytest.mark.regression
def test_open_my_leave(login_leave):

    driver = login_leave

    leave = LeavePage(driver)

    leave.open_leave()

    leave.open_my_leave()

    assert leave.is_my_leave_page_displayed()


@pytest.mark.regression
def test_open_leave_list(login_leave):

    driver = login_leave

    leave = LeavePage(driver)

    leave.open_leave()

    leave.open_leave_list()

    assert leave.is_leave_list_displayed()


@pytest.mark.sanity
def test_leave_page_title(login_leave):

    driver = login_leave

    leave = LeavePage(driver)

    leave.open_leave()

    assert "OrangeHRM" in driver.title