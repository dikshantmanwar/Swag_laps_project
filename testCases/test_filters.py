import pytest
from Utilities.Logger import LogGen
from Utilities.LoginHelper import LoginHelper
from PageObject.Filters import Filters


@pytest.mark.usefixtures("setup")
class TestFilters:
    """Test class for product filter functionality"""

    LOG = LogGen.loggen()

    def test_filter_name_a_to_z(self):
        """Test filtering products by Name (A to Z)"""
        assert LoginHelper.perform_login(self.driver), "Login failed"
        self.LOG.info("Test: Filter products by Name (A to Z)")

        filters = Filters(self.driver)
        filters.select_filter_by_visible_text("Name (A to Z)")
        self.LOG.info("Selected filter: Name (A to Z)")

        product_names = filters.get_all_product_names()
        self.LOG.info(f"Product names: {product_names}")
        
        assert filters.verify_name_sorted_a_to_z(), "Products are not sorted A to Z"
        self.LOG.info("Verification passed: Products sorted A to Z")

    def test_filter_name_z_to_a(self):
        """Test filtering products by Name (Z to A)"""
        assert LoginHelper.perform_login(self.driver), "Login failed"
        self.LOG.info("Test: Filter products by Name (Z to A)")

        filters = Filters(self.driver)
        filters.select_filter_by_value("za")
        self.LOG.info("Selected filter: Name (Z to A)")

        product_names = filters.get_all_product_names()
        self.LOG.info(f"Product names: {product_names}")
        
        assert filters.verify_name_sorted_z_to_a(), "Products are not sorted Z to A"
        self.LOG.info("Verification passed: Products sorted Z to A")

    def test_filter_price_low_to_high(self):
        """Test filtering products by Price (low to high)"""
        assert LoginHelper.perform_login(self.driver), "Login failed"
        self.LOG.info("Test: Filter products by Price (low to high)")

        filters = Filters(self.driver)
        filters.select_filter_by_visible_text("Price (low to high)")
        self.LOG.info("Selected filter: Price (low to high)")

        product_prices = filters.get_all_product_prices()
        self.LOG.info(f"Product prices: {product_prices}")
        
        assert filters.verify_price_sorted_low_to_high(), "Products are not sorted by price low to high"
        self.LOG.info("Verification passed: Products sorted by price low to high")

    def test_filter_price_high_to_low(self):
        """Test filtering products by Price (high to low)"""
        assert LoginHelper.perform_login(self.driver), "Login failed"
        self.LOG.info("Test: Filter products by Price (high to low)")

        filters = Filters(self.driver)
        filters.select_filter_by_value("hilo")
        self.LOG.info("Selected filter: Price (high to low)")

        product_prices = filters.get_all_product_prices()
        self.LOG.info(f"Product prices: {product_prices}")
        
        assert filters.verify_price_sorted_high_to_low(), "Products are not sorted by price high to low"
        self.LOG.info("Verification passed: Products sorted by price high to low")
