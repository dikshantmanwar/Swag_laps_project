from Utilities.readproperties import ReadValue
from PageObject.LoginPage import LoginPage
from Utilities.Logger import LogGen


class LoginHelper:
    """Helper class for login operations"""
    
    LOG = LogGen.loggen()
    
    @staticmethod
    def perform_login(driver, username=None, password=None):
        """
        Performs login with provided or default credentials
        
        :param driver: WebDriver instance
        :param username: Optional username (uses config if not provided)
        :param password: Optional password (uses config if not provided)
        :return: True if login successful, False otherwise
        """
        url = ReadValue.getUrl()
        username = username or ReadValue.getusername()
        password = password or ReadValue.getPassword()
        
        LoginHelper.LOG.info(f"Performing login for user: {username}")
        driver.get(url)
        
        lp = LoginPage(driver)
        lp.get_username(username)
        lp.get_password(password)
        lp.click_on_login()
        
        if lp.login_status():
            LoginHelper.LOG.info("Login successful")
            return True
        else:
            LoginHelper.LOG.error("Login failed")
            return False
