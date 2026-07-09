import pytest

from Pages.login_page import LoginPage
from Pages.admin_page import AdminPage
from Utilities.config_reader import ConfigReader
from Utilities.json_reader import JsonReader


admin_data = JsonReader.read_json("admin_data.json")["admin_user"]


@pytest.fixture
def login_admin(setup):

    driver = setup

    driver.get(ConfigReader.get_base_url())

    login = LoginPage(driver)

    login.login("Admin", "admin123")

    return driver


@pytest.mark.smoke
@pytest.mark.regression
def test_open_admin_module(login_admin):

    driver = login_admin

    admin = AdminPage(driver)

    admin.open_admin()

    assert "admin" in driver.current_url.lower()


@pytest.mark.regression
def test_search_existing_user(login_admin):

    driver = login_admin

    admin = AdminPage(driver)

    admin.open_admin()

    admin.search_username(admin_data["search_username"])

    admin.click_search()

    assert admin_data["search_username"] in driver.page_source


@pytest.mark.sanity
def test_admin_page_title(login_admin):

    driver = login_admin

    admin = AdminPage(driver)

    admin.open_admin()

    assert "OrangeHRM" in driver.title