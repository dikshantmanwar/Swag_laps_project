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
        username_field = self.driver.find_element(*self.USERNAME_ID)
        username_field.clear()
        username_field.send_keys(username)

    def get_password(self, password):
        """
        Enters the password in the corresponding input field.

        :param password: The password to enter.
        :return: None
        """
        self.wait.until(
            expected_conditions.presence_of_element_located(self.PASSWORD_ID)
        )
        password_field = self.driver.find_element(*self.PASSWORD_ID)
        password_field.clear()
        password_field.send_keys(password)

    def click_on_login(self):
        """
        Clicks on the login button.

        :return: None
        """
        self.wait.until(expected_conditions.element_to_be_clickable(self.LOGIN_ID))
        self.driver.find_element(*self.LOGIN_ID).click()
        # Wait a moment and dismiss any popup
        import time
        time.sleep(1.5)
        self.dismiss_password_popup()

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
    
    def dismiss_password_popup(self):
        """
        Dismisses the Chrome password manager popup if it appears.
        Uses multiple strategies to ensure popup is closed.
        
        :return: None
        """
        from selenium.webdriver.common.keys import Keys
        import time
        
        try:
            # Wait a moment for popup to appear
            time.sleep(0.5)
            
            # Strategy 1: Send Escape key multiple times
            body = self.driver.find_element(By.TAG_NAME, 'body')
            for _ in range(3):
                body.send_keys(Keys.ESCAPE)
                time.sleep(0.2)
        except:
            pass
        
        try:
            # Strategy 2: Click on a safe area of the page
            products_area = self.driver.find_element(By.CLASS_NAME, 'inventory_container')
            products_area.click()
        except:
            pass
        
        try:
            # Strategy 3: Use JavaScript to dismiss any dialogs
            self.driver.execute_script("""
                // Remove any modal overlays or dialogs
                var overlays = document.querySelectorAll('[role="dialog"], [role="alertdialog"]');
                overlays.forEach(function(overlay) {
                    overlay.remove();
                });
                
                // Click on body to dismiss browser popups
                document.body.click();
            """)
        except:
            pass
        
        try:
            # Strategy 4: Try to find and click OK button if it exists
            ok_button = WebDriverWait(self.driver, 2).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='OK' or text()='Ok']"))
            )
            ok_button.click()
        except:
            pass
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
