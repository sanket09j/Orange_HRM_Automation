import pytest

from Pages.login_page import LoginPage
from Utilities.config_reader import ConfigReader


@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login(setup):

    driver = setup

    driver.get(ConfigReader.get_base_url())

    login_page = LoginPage(driver)

    login_page.login("Admin", "admin123")

    assert "dashboard" in driver.current_url.lower()