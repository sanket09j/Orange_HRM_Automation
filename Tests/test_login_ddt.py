import os
import pytest

from Pages.login_page import LoginPage
from Utilities.config_reader import ConfigReader
from Utilities.excel_utils import ExcelUtils


file = os.path.join(
    os.getcwd(),
    "TestData",
    "LoginData.xlsx"
)

sheet = "Login"

rows = ExcelUtils.get_row_count(file, sheet)


@pytest.mark.regression
def test_login_ddt(setup):

    driver = setup

    login = LoginPage(driver)

    for r in range(2, rows + 1):

        driver.get(ConfigReader.get_base_url())

        username = ExcelUtils.read_data(
            file,
            sheet,
            r,
            1
        )

        password = ExcelUtils.read_data(
            file,
            sheet,
            r,
            2
        )

        login.login(username, password)

        if username == "Admin" and password == "admin123":

            assert "dashboard" in driver.current_url.lower()

            # Logout before next iteration
            login.logout()

        else:

            assert "dashboard" not in driver.current_url.lower()