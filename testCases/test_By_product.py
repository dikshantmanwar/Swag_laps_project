



import time

from selenium.webdriver.common.by import By

from Utilitis.readproperties import ReadValue
from PageObject.LoginPage import Login
from Utilitis.Logger import LogGen
from PageObject.By_Product import By_product

class Test_By_Prodct():

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


        self.by.click_on_backpack()
        self.by.click_on_t_shirt()

        self.by.click_on_cart_icon()

        self.by.click_on_ckeckout()

        self.by.enter_firstname("Dikshant")
        self.by.enter_lastname('Manwat')
        self.by.enter_postal_code(345234)

        self.by.click_on_contineu_btn()
        self.by.click_on_finish_btn()
        time.sleep(5)
