from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    """
    Page object representing the login page.
    """

    # Element locators
    USERNAME_ID = (By.ID, "user-name")
    PASSWORD_ID = (By.ID, "password")
    LOGIN_ID = (By.ID, "login-button")
    MENU_BUTTON_ID = (By.ID, "react-burger-menu-btn")
    LOGOUT_ID = (By.ID, "logout_sidebar_link")
    ERROR_MASSAGE=(By.XPATH,"//div[@class='error-message-container error']")
    price=(By.XPATH,'//div[@class="inventory_item_price"]')

    def __init__(self, driver):
        """
        Initializes the LoginPage.

        :param driver: The WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def get_username(self, username):
        """
        Enters the username in the corresponding input field.

        :param username: The username to enter.
        :return: None
        """
        self.wait.until(
            expected_conditions.presence_of_element_located(self.USERNAME_ID)
        )
        self.driver.find_element(*self.USERNAME_ID).send_keys(username)

    def get_password(self, password):
        """
        Enters the password in the corresponding input field.

        :param password: The password to enter.
        :return: None
        """
        self.wait.until(
            expected_conditions.presence_of_element_located(self.PASSWORD_ID)
        )
        self.driver.find_element(*self.PASSWORD_ID).send_keys(password)

    def click_on_login(self):
        """
        Clicks on the login button.

        :return: None
        """
        self.wait.until(expected_conditions.element_to_be_clickable(self.LOGIN_ID))
        self.driver.find_element(*self.LOGIN_ID).click()

    def click_on_menu(self):
        """
        Clicks on the menu button.

        :return: None
        """
        self.wait.until(
            expected_conditions.element_to_be_clickable(self.MENU_BUTTON_ID)
        )
        self.driver.find_element(*self.MENU_BUTTON_ID).click()

    def click_on_logout(self):
        """
        Clicks on the logout button.

        :return: None
        """
        self.wait.until(expected_conditions.element_to_be_clickable(self.LOGOUT_ID))
        self.driver.find_element(*self.LOGOUT_ID).click()

    def login_status(self):
        """
        Checks the login status.

        :return: True if the login is successful, False otherwise.
        """
        try:
            self.wait.until(
                expected_conditions.presence_of_element_located(self.MENU_BUTTON_ID)
            )
            self.driver.find_element(*self.MENU_BUTTON_ID)
            return True
        except (NoSuchElementException, TimeoutException):
            return False
    def error_massage(self):
        self.wait.until(
            expected_conditions.presence_of_element_located(self.ERROR_MASSAGE)
        )
        error=self.driver.find_element(*self.ERROR_MASSAGE).text
        return error
    def all_item_price(self):
        self.wait.until(
            expected_conditions.presence_of_element_located(self.price)
        )
        Price = self.driver.find_elements(*self.price).text
        return Price
