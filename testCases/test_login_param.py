import pytest
from Utilities.readproperties import ReadValue
from PageObject.LoginPage import LoginPage
from Utilities.Logger import LogGen


class TestUrlLoginParam:
    """
    Test class for parameterized login functionality.
    """

    URL = ReadValue.getUrl()
    LOG = LogGen.loggen()

    def test_login_using_param(self, setup, getDataForLogin):
        self.driver = setup
        self.LOG.info("Test: Parameterized login test")
        self.driver.get(self.URL)

        self.lp = LoginPage(self.driver)

        self.lp.get_username(getDataForLogin[0])
        self.LOG.info("Entering username: %s", getDataForLogin[0])
        self.lp.get_password(getDataForLogin[1])
        self.LOG.info("Entering password for user: %s", getDataForLogin[0])
        self.lp.click_on_login()
        self.LOG.info("Clicked on login button")

        login_status = []
        if self.lp.login_status():
            self.driver.save_screenshot("Screenshot/login_test_pass.png")
            if getDataForLogin[2] == "Pass":
                login_status.append("Pass")
                self.LOG.info("Login successful as expected for: %s", getDataForLogin[0])
            elif getDataForLogin[2] == "Fail":
                login_status.append("Fail")
                self.LOG.error("Login successful but expected to fail for: %s", getDataForLogin[0])
            
            self.lp.click_on_menu()
            self.LOG.info("Clicked on menu button")
            self.lp.click_on_logout()
            self.LOG.info("Clicked on logout button")
        else:
            self.driver.save_screenshot("Screenshot/login_param_test_fail.png")
            if getDataForLogin[2] == "Fail":
                login_status.append("Pass")
                self.LOG.info("Login failed as expected for: %s", getDataForLogin[0])
            elif getDataForLogin[2] == "Pass":
                login_status.append("Fail")
                self.LOG.error("Login failed but expected to pass for: %s", getDataForLogin[0])

        self.LOG.info("Login status: %s", login_status)

        if "Fail" not in login_status:
            self.LOG.info("test_login_params is Passed")
            assert True
        else:
            self.LOG.info("test_login_params is Failed")
            assert False

        self.LOG.info("test_login_params is Completed")
