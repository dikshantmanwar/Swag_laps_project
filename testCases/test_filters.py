import pytest
from Utilities.readproperties import ReadValue
from Utilities.Logger import LogGen
from PageObject.LoginPage import LoginPage
from PageObject.Filters import Filters


class TestFilters:
    """
    Test class for product filter functionality.
    """

    URL = ReadValue.getUrl()
    USERNAME = ReadValue.getusername()
    PASSWORD = ReadValue.getPassword()
    LOG = LogGen.loggen()

    @classmethod
    def setup_class(cls):
        """Setup method that runs once before all tests in the class"""
        cls.LOG.info("Setting up TestFilters class")

    def test_01_login(self, setup):
        """Login once before running filter tests"""
        self.driver = setup
        self.LOG.info("Test: Login for filter tests")
        self.driver.get(self.URL)
        lp = LoginPage(self.driver)
        lp.get_username(self.USERNAME)
        lp.get_password(self.PASSWORD)
        lp.click_on_login()
        
        if lp.login_status():
            self.LOG.info("Login successful")
            assert True
        else:
            self.LOG.error("Login failed")
            assert False

    def test_02_filter_name_a_to_z(self, setup):
        """Test filtering products by Name (A to Z)"""
        self.driver = setup
        self.LOG.info("Test: Filter products by Name (A to Z)")

        # Apply filter
        filters = Filters(self.driver)
        filters.select_filter_by_visible_text("Name (A to Z)")
        self.LOG.info("Selected filter: Name (A to Z)")

        # Verify sorting
        product_names = filters.get_all_product_names()
        self.LOG.info(f"Product names: {product_names}")
        
        assert filters.verify_name_sorted_a_to_z(), "Products are not sorted A to Z"
        self.LOG.info("Verification passed: Products sorted A to Z")

    def test_03_filter_name_z_to_a(self, setup):
        """Test filtering products by Name (Z to A)"""
        self.driver = setup
        self.LOG.info("Test: Filter products by Name (Z to A)")

        # Apply filter
        filters = Filters(self.driver)
        filters.select_filter_by_value("za")
        self.LOG.info("Selected filter: Name (Z to A)")

        # Verify sorting
        product_names = filters.get_all_product_names()
        self.LOG.info(f"Product names: {product_names}")
        
        assert filters.verify_name_sorted_z_to_a(), "Products are not sorted Z to A"
        self.LOG.info("Verification passed: Products sorted Z to A")

    def test_04_filter_price_low_to_high(self, setup):
        """Test filtering products by Price (low to high)"""
        self.driver = setup
        self.LOG.info("Test: Filter products by Price (low to high)")

        # Apply filter
        filters = Filters(self.driver)
        filters.select_filter_by_visible_text("Price (low to high)")
        self.LOG.info("Selected filter: Price (low to high)")

        # Verify sorting
        product_prices = filters.get_all_product_prices()
        self.LOG.info(f"Product prices: {product_prices}")
        
        assert filters.verify_price_sorted_low_to_high(), "Products are not sorted by price low to high"
        self.LOG.info("Verification passed: Products sorted by price low to high")

    def test_05_filter_price_high_to_low(self, setup):
        """Test filtering products by Price (high to low)"""
        self.driver = setup
        self.LOG.info("Test: Filter products by Price (high to low)")

        # Apply filter
        filters = Filters(self.driver)
        filters.select_filter_by_value("hilo")
        self.LOG.info("Selected filter: Price (high to low)")

        # Verify sorting
        product_prices = filters.get_all_product_prices()
        self.LOG.info(f"Product prices: {product_prices}")
        
        assert filters.verify_price_sorted_high_to_low(), "Products are not sorted by price high to low"
        self.LOG.info("Verification passed: Products sorted by price high to low")
