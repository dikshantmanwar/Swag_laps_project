



import time

from selenium.webdriver.common.by import By

from Utilitis.readproperties import ReadValue
from PageObject.LoginPage import Login
from Utilitis.Logger import LogGen
from PageObject.By_Product import By_product

class Test_By_Prodct():
    backpack_id = (By.ID, 'add-to-cart-sauce-labs-backpack')
    t_shirt_id = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")

    url=ReadValue.getUrl()
    username=ReadValue.getusername()
    password=ReadValue.getPassword()
    log=LogGen.loggen()

    def test_by_product(self,setup):

        self.driver=setup
        self.driver.get(self.url)
        self.lp=Login(self.driver)

        self.by=By_product(self.driver)

        self.lp.get_username(self.username)
        self.log.info("Entering username----->"+ self.username)
        self.lp.get_password(self.password)
        self.log.info("Entering password------>"+ self.password)
        self.lp.click_on_login()
        self.log.info('click on login button')


        self.by.click_on_backpack()
        self.log.info('Click on backpack button')
        self.by.click_on_t_shirt()

        self.by.click_on_cart_icon()

        self.by.click_on_ckeckout()

        self.by.enter_firstname("Dikshant")
        self.by.enter_lastname('Manwat')
        self.by.enter_postal_code(345234)
        self.log.info('Enter all detail ')

        self.by.click_on_contineu_btn()
        self.log.info('Click on contineu button')
        self.by.click_on_finish_btn()
        self.log.info('Click on finish button')
        time.sleep(5)
        self.driver.close()
