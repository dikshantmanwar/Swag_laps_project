import time
from selenium.webdriver.common.by import By
from Utilities.readproperties import ReadValue
from PageObject.LoginPage import LoginPage
from Utilities.Logger import LogGen
from PageObject.By_Product import ProductPage

class Test_By_Prodct:
    url = ReadValue.getUrl()
    username = ReadValue.getusername()
    password = ReadValue.getPassword()
    log = LogGen.loggen()

    def test_by_product(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)

        self.by = ProductPage(self.driver)

        self.lp.get_username(self.username)
        self.log.info("Entering username----->")
        self.lp.get_password(self.password)
        self.log.info("Entering password------>")
        self.lp.click_on_login()
        self.log.info("click on login button")

        self.by.click_on_backpack()
        self.log.info("Click on backpack button")
        self.by.click_on_t_shirt()

        self.by.click_on_cart_icon()

        self.by.click_on_checkout()

        self.by.enter_first_name("Dikshant")
        self.by.enter_last_name("Manwat")
        self.by.enter_postal_code(34523423)
        self.log.info("Enter all detail ")

        self.by.click_on_continue_btn()
        self.log.info("Click on contineu button")
        self.by.click_on_finish_btn()
        self.log.info("Click on finish button")
        time.sleep(5)
        self.driver.close()
