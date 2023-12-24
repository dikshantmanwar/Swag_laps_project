from Utilities.readproperties import ReadValue
from Utilities.Logger import LogGen
from PageObject.LoginPage import LoginPage


class TestUrlLogin:
    """
    Test class for login functionality.
    """

    URL = ReadValue.getUrl()
    USERNAME = ReadValue.getusername()
    PASSWORD = ReadValue.getPassword()
    LOG = LogGen.loggen()

    def __init__(self, setup):
        self.driver = setup
        self.driver.get(self.URL)

        self.lp = LoginPage(self.driver)

    def test_login(self):
        """
        Test method for the login functionality.
        """

        self.lp.get_username(self.USERNAME)
        self.LOG.info("Entering username ----->%s", self.USERNAME)
        self.lp.get_password(self.PASSWORD)
        self.LOG.info("Entering password ------> %s", self.PASSWORD)
        self.lp.click_on_login()

        self.LOG.info("Click on login button")
        if self.lp.login_status():
            self.LOG.info('Login test is pass')
            self.driver.save_screenshot(
                'C:\\Users\\Admin\\PycharmProjects\\Swag_Labs_Project\\Screenshot\\login_successful.png')
            self.lp.click_on_menu()
            self.lp.click_on_logout()
            self.LOG.info("Click on logout button")
            self.driver.save_screenshot(
                'C:\\Users\\Admin\\PycharmProjects\\Swag_Labs_Project\\Screenshot\\logout_successful.png')
            assert True
        else:
            self.LOG.info("Test login is Failed")
            self.driver.save_screenshot(
                "C:\\Users\\Admin\\PycharmProjects\\Swag_Labs_Project\\Screenshot\\login_fail.png")
            assert False

        self.driver.close()
        self.LOG.info("Test login is Completed")
