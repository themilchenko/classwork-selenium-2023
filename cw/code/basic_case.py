import pytest
from login_page import LoginPage


class BasicCase:
    is_logged = False

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.driver = browser

    # Login once per test set
    @pytest.fixture(scope="class", autouse=True)
    def login(self, browser):
        if not self.is_logged:
            browser.delete_all_cookies()
            browser.refresh()
            log = LoginPage(browser)
            log.login()