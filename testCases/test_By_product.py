import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.readproperties import ReadValue
from Utilities.LoginHelper import LoginHelper
from Utilities.Logger import LogGen
from PageObject.By_Product import ProductPage


class TestByProduct:
    """
    Test class for product purchase functionality.
    """

    FIRST_NAME = ReadValue.getFirstName()
    LAST_NAME = ReadValue.getLastName()
    POSTAL_CODE = ReadValue.getPostalCode()
    LOG = LogGen.loggen()

    def test_purchase_products(self, setup):
        """Test login and complete product purchase flow"""
        self.driver = setup
        self.LOG.info("Test: Login and purchase products")
        
        # Login using helper
        assert LoginHelper.perform_login(self.driver), "Login failed"
        
        # Initialize product page
        self.by = ProductPage(self.driver)

        # Add products to cart
        self.by.click_on_backpack()
        self.LOG.info("Added backpack to cart")
        self.by.click_on_t_shirt()
        self.LOG.info("Added t-shirt to cart")

        # Go to cart
        self.by.click_on_cart_icon()
        self.LOG.info("Clicked on cart icon")

        # Proceed to checkout
        self.by.click_on_checkout()
        self.LOG.info("Clicked on checkout")

        # Enter checkout information
        self.by.enter_first_name(self.FIRST_NAME)
        self.by.enter_last_name(self.LAST_NAME)
        self.by.enter_postal_code(self.POSTAL_CODE)
        self.LOG.info("Entered checkout details")

        # Complete purchase
        self.by.click_on_continue_btn()
        self.LOG.info("Clicked on continue button")
        self.by.click_on_finish_btn()
        self.LOG.info("Clicked on finish button")

        # Verify order completion
        wait = WebDriverWait(self.driver, 10)
        success_message = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        actual_message = success_message.text
        self.LOG.info(f"Order completion message: {actual_message}")
        
        assert "Thank you for your order" in actual_message or "complete" in actual_message.lower(), \
            f"Expected success message but got: {actual_message}"
        self.LOG.info("Order completed successfully")
