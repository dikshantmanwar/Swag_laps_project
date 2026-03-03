from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select


class Filters:
    filter_dropdown = (By.XPATH, "//select[@class='product_sort_container']")
    product_names = (By.CSS_SELECTOR, ".inventory_item_name")
    product_prices = (By.CSS_SELECTOR, ".inventory_item_price")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def select_filter_by_visible_text(self, filter_text):
        """
        Select filter option by visible text.
        Options: 'Name (A to Z)', 'Name (Z to A)', 'Price (low to high)', 'Price (high to low)'
        """
        self.wait.until(expected_conditions.presence_of_element_located(self.filter_dropdown))
        dropdown = Select(self.driver.find_element(*self.filter_dropdown))
        dropdown.select_by_visible_text(filter_text)

    def select_filter_by_value(self, value):
        """
        Select filter option by value attribute.
        Values: 'az', 'za', 'lohi', 'hilo'
        """
        self.wait.until(expected_conditions.presence_of_element_located(self.filter_dropdown))
        dropdown = Select(self.driver.find_element(*self.filter_dropdown))
        dropdown.select_by_value(value)

    def get_selected_filter(self):
        """Returns the currently selected filter option text"""
        dropdown = Select(self.driver.find_element(*self.filter_dropdown))
        return dropdown.first_selected_option.text

    def get_all_product_names(self):
        """Returns list of all product names displayed on the page"""
        self.wait.until(expected_conditions.presence_of_all_elements_located(self.product_names))
        elements = self.driver.find_elements(*self.product_names)
        return [element.text for element in elements]

    def get_all_product_prices(self):
        """Returns list of all product prices as floats"""
        self.wait.until(expected_conditions.presence_of_all_elements_located(self.product_prices))
        elements = self.driver.find_elements(*self.product_prices)
        # Remove '$' and convert to float
        return [float(element.text.replace('$', '')) for element in elements]

    def verify_name_sorted_a_to_z(self):
        """Verify products are sorted alphabetically A to Z"""
        names = self.get_all_product_names()
        return names == sorted(names)

    def verify_name_sorted_z_to_a(self):
        """Verify products are sorted alphabetically Z to A"""
        names = self.get_all_product_names()
        return names == sorted(names, reverse=True)

    def verify_price_sorted_low_to_high(self):
        """Verify products are sorted by price low to high"""
        prices = self.get_all_product_prices()
        return prices == sorted(prices)

    def verify_price_sorted_high_to_low(self):
        """Verify products are sorted by price high to low"""
        prices = self.get_all_product_prices()
        return prices == sorted(prices, reverse=True)
