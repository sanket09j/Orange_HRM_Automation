from Pages.login_page import LoginPage
from Utilities.config_reader import ConfigReader


def test_logout(setup):

    driver = setup

    driver.get(ConfigReader.get_base_url())

    login = LoginPage(driver)

    login.login("Admin", "admin123")

    login.logout()

    assert "login" in driver.current_url.lower()