import pytest

from Utilities.browser_utils import BrowserUtils
from Utilities.logger import LogGen
from Utilities.screenshot import Screenshot

logger = LogGen.get_logger()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser Name: chrome or edge"
    )


@pytest.fixture(scope="function")
def setup(request):

    browser = request.config.getoption("--browser")

    logger.info("===== Browser Started =====")

    driver = BrowserUtils.get_driver(browser)

    yield driver

    logger.info("===== Browser Closed =====")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("setup")

        if driver:
            Screenshot.capture(driver, item.name)