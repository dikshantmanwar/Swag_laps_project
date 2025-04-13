import pytest
from Utilities.readproperties import ReadValue
from Utilities.Logger import LogGen
from PageObject.LoginPage import LoginPage

@pytest.mark.usefixtures("setup")
class TestUrlLogin:
    """
    Test class for login functionality.
    """

    URL = ReadValue.getUrl()
    USERNAME = ReadValue.getusername()
    INVALID_UN = ReadValue.invalidgetusername()
    PASSWORD = ReadValue.getPassword()
    INVALID_PW = ReadValue.invalidgetPassword()
    LOG = LogGen.loggen()

    @pytest.mark.invalid_login
    def test_login_with_invalid_username_and_password(self):
        self.LOG.info("Test: Login with invalid username and password")
        self.driver.get(self.URL)
        self.LOG.info("Navigated to URL: %s", self.URL)

        self.lp = LoginPage(self.driver)
        self.lp.get_username(self.INVALID_UN)
        self.LOG.info("Entered invalid username: %s", self.INVALID_UN)

        self.lp.get_password(self.INVALID_PW)
        self.LOG.info("Entered invalid password: %s", self.INVALID_PW)

        self.lp.click_on_login()
        self.LOG.info("Clicked login button")

        Actual_error = self.lp.error_massage()
        self.LOG.info("Captured error message: %s", Actual_error)

        Expected_error = "Epic sadface: Username and password do not match any user in this service"
        assert Expected_error == Actual_error, "Assertion failed"

    @pytest.mark.invalid_login
    def test_login_without_username_and_with_password(self):
        self.LOG.info("Test: Login without username and with password")
        self.driver.get(self.URL)
        self.LOG.info("Navigated to URL: %s", self.URL)

        self.lp = LoginPage(self.driver)
        self.lp.get_password(self.INVALID_PW)
        self.LOG.info("Entered password only: %s", self.INVALID_PW)

        self.lp.click_on_login()
        self.LOG.info("Clicked login button")

        Actual_error = self.lp.error_massage()
        self.LOG.info("Captured error message: %s", Actual_error)

        Expected_error = "Epic sadface: Username is required"
        assert Expected_error == Actual_error, "Assertion failed - Expected: %s | Got: %s" % (Expected_error, Actual_error)

    def test_login_with_valid_username_and_without_password(self):
        self.LOG.info("Test: Login with username but no password")
        self.driver.get(self.URL)
        self.LOG.info("Navigated to URL: %s", self.URL)

        self.lp = LoginPage(self.driver)
        self.lp.get_username(self.INVALID_UN)
        self.LOG.info("Entered username only: %s", self.INVALID_UN)

        self.lp.click_on_login()
        self.LOG.info("Clicked login button")

        Actual_error = self.lp.error_massage()
        self.LOG.info("Captured error message: %s", Actual_error)

        Expected_error = "Epic sadface: Password is required"
        assert Expected_error == Actual_error, "Assertion failed - Expected: %s | Got: %s" % (Expected_error, Actual_error)
    def test_login_valid_username_password(self):
        self.LOG.info("Test: Login with valid username and password")
        self.driver.get(self.URL)
        self.LOG.info("Navigated to URL: %s", self.URL)

        self.lp = LoginPage(self.driver)
        self.lp.get_username(self.USERNAME)
        self.LOG.info("Entered valid username: %s", self.USERNAME)

        self.lp.get_password(self.PASSWORD)
        self.LOG.info("Entered valid password: %s", self.PASSWORD)

        self.lp.click_on_login()
        self.LOG.info("Clicked login button")

        if self.lp.login_status():
            self.LOG.info("Login successful")
            self.driver.save_screenshot("Screenshot/New_login_successful.png")
            self.lp.click_on_menu()
            self.lp.click_on_logout()
            self.LOG.info("Clicked logout")
            self.driver.save_screenshot("Screenshot/New_logout_successful.png")
            assert True
        else:
            self.LOG.error("Login failed")
            self.driver.save_screenshot("Screenshot/New_login_fail.png")
            assert False

        self.LOG.info("Test login completed")
