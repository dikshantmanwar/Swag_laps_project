# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# class By_product():
#     backpack_id = (By.ID, 'add-to-cart-sauce-labs-backpack')
#     t_shirt_id = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
#     cart_xpath = (By.XPATH, "//a[@class='shopping_cart_link']")
#     ckeckout_id = (By.ID, 'checkout')
#     firstname_name = (By.NAME, 'firstName')
#     lastname_name = (By.NAME, 'lastName')
#     postal_code_id = (By.ID, "postal-code")
#     continue_btn_id = (By.ID, 'continue')
#     finish_btn_id = (By.ID, 'finish')
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 5)
#
#     def click_on_backpack(self):
#         self.wait.until(expected_conditions.element_to_be_clickable(self.backpack_id))
#         self.driver.find_element(*By_product.backpack_id).click()
#
#     def click_on_t_shirt(self):
#         self.wait.until(expected_conditions.element_to_be_clickable(self.t_shirt_id))
#         self.driver.find_element(*By_product.t_shirt_id).click()
#
#     def click_on_cart_icon(self):
#         self.wait.until(expected_conditions.element_to_be_clickable(self.cart_xpath))
#         self.driver.find_element(*By_product.cart_xpath).click()
#
#     def click_on_ckeckout(self):
#         self.wait.until(expected_conditions.element_to_be_clickable(self.ckeckout_id))
#         self.driver.find_element(*By_product.ckeckout_id).click()
#
#     def enter_firstname(self, firstname):
#         self.wait.until(expected_conditions.presence_of_element_located(self.firstname_name))
#         self.driver.find_element(*By_product.firstname_name).send_keys(firstname)
#
#     def enter_lastname(self, lastname):
#         self.wait.until(expected_conditions.presence_of_element_located(self.lastname_name))
#         self.driver.find_element(*By_product.lastname_name).send_keys(lastname)
#
#     def enter_postal_code(self, postalcode):
#         self.wait.until(expected_conditions.presence_of_element_located(self.postal_code_id))
#         self.driver.find_element(*By_product.postal_code_id).send_keys(postalcode)
#
#     def click_on_contineu_btn(self):
#         self.wait.until(expected_conditions.presence_of_element_located(self.continue_btn_id))
#         self.driver.find_element(*By_product.continue_btn_id).click()
#
#     def click_on_finish_btn(self):
#         self.wait.until(expected_conditions.presence_of_element_located(self.finish_btn_id))
#         self.driver.find_element(*By_product.finish_btn_id).click()


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:
    """
    Page object representing the product page.
    """

    # Element locators
    BACKPACK_ID = (By.ID, 'add-to-cart-sauce-labs-backpack')
    T_SHIRT_ID = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    CART_XPATH = (By.XPATH, "//a[@class='shopping_cart_link']")
    CHECKOUT_ID = (By.ID, 'checkout')
    FIRST_NAME_NAME = (By.NAME, 'firstName')
    LAST_NAME_NAME = (By.NAME, 'lastName')
    POSTAL_CODE_ID = (By.ID, "postal-code")
    CONTINUE_BTN_ID = (By.ID, 'continue')
    FINISH_BTN_ID = (By.ID, 'finish')

    def __init__(self, driver):
        """
        Initializes the ProductPage.

        :param driver: The WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def click_on_backpack(self):
        """
        Clicks on the backpack product.

        :return: None
        """
        self.wait.until(expected_conditions.element_to_be_clickable(self.BACKPACK_ID))
        self.driver.find_element(*self.BACKPACK_ID).click()

    def click_on_t_shirt(self):
        """
        Clicks on the T-shirt product.

        :return: None
        """
        self.wait.until(expected_conditions.element_to_be_clickable(self.T_SHIRT_ID))
        self.driver.find_element(*self.T_SHIRT_ID).click()

    def click_on_cart_icon(self):
        """
        Clicks on the shopping cart icon.

        :return: None
        """
        self.wait.until(expected_conditions.element_to_be_clickable(self.CART_XPATH))
        self.driver.find_element(*self.CART_XPATH).click()

    def click_on_checkout(self):
        """
        Clicks on the checkout button.

        :return: None
        """
        self.wait.until(expected_conditions.element_to_be_clickable(self.CHECKOUT_ID))
        self.driver.find_element(*self.CHECKOUT_ID).click()

    def enter_first_name(self, first_name):
        """
        Enters the first name in the corresponding input field.

        :param first_name: The first name to enter.
        :return: None
        """
        self.wait.until(expected_conditions.presence_of_element_located(self.FIRST_NAME_NAME))
        self.driver.find_element(*self.FIRST_NAME_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        """
        Enters the last name in the corresponding input field.

        :param last_name: The last name to enter.
        :return: None
        """
        self.wait.until(expected_conditions.presence_of_element_located(self.LAST_NAME_NAME))
        self.driver.find_element(*self.LAST_NAME_NAME).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        """
        Enters the postal code in the corresponding input field.

        :param postal_code: The postal code to enter.
        :return: None
        """
        self.wait.until(expected_conditions.presence_of_element_located(self.POSTAL_CODE_ID))
        self.driver.find_element(*self.POSTAL_CODE_ID).send_keys(postal_code)

    def click_on_continue_btn(self):
        """
        Clicks on the continue button.

        :return: None
        """
        self.wait.until(expected_conditions.presence_of_element_located(self.CONTINUE_BTN_ID))
        self.driver.find_element(*self.CONTINUE_BTN_ID).click()

    def click_on_finish_btn(self):
        """
        Clicks on the finish button.

        :return: None
        """
        self.wait.until(expected_conditions.presence_of_element_located(self.FINISH_BTN_ID))
        self.driver.find_element(*self.FINISH_BTN_ID).click()

# this is in practice branch