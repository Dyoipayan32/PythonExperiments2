import time

import pytest


@pytest.mark.usefixtures("setup")
class TestFix05:
    def test_launch_google(self, setup):
        self.browser = setup
        self.browser.get("https://www.google.com")
        self.browser.maximize_window()
        self.browser.refresh()
        time.sleep(5)
