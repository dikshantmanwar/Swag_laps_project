
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class By_product():
     backpack_id =(By.ID, 'add-to-cart-sauce-labs-backpack')
     t_shirt_id  =(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")
     cart_xpath  =(By.XPATH,"//a[@class='shopping_cart_link']")
     ckeckout_id =(By.ID,'checkout')
     firstname_name  = (By.NAME,'firstName')
     lastname_name   = (By.NAME,'lastName')
     postal_code_id = (By.ID,"postal-code")
     continue_btn_id =(By.ID,'continue')
     finish_btn_id=(By.ID,'finish')

     def __init__(self,driver):
         self.driver=driver
         self.wait=WebDriverWait(driver,5)

     def click_on_backpack(self):
          self.wait.until(expected_conditions.element_to_be_clickable(self.backpack_id))
          self.driver.find_element(*By_product.backpack_id).click()

     def click_on_t_shirt(self):
          self.wait.until(expected_conditions.element_to_be_clickable(self.t_shirt_id))
          self.driver.find_element(*By_product.t_shirt_id).click()

     def click_on_cart_icon(self):
         self.wait.until(expected_conditions.element_to_be_clickable(self.cart_xpath))
         self.driver.find_element(*By_product.cart_xpath).click()

     def click_on_ckeckout(self):
         self.wait.until(expected_conditions.element_to_be_clickable(self.ckeckout_id))
         self.driver.find_element(*By_product.ckeckout_id).click()

     def enter_firstname(self,firstname):
         self.wait.until(expected_conditions.presence_of_element_located(self.firstname_name))
         self.driver.find_element(*By_product.firstname_name).send_keys(firstname)

     def enter_lastname(self, lastname):
         self.wait.until(expected_conditions.presence_of_element_located(self.lastname_name))
         self.driver.find_element(*By_product.lastname_name).send_keys(lastname)

     def enter_postal_code(self, postalcode):
         self.wait.until(expected_conditions.presence_of_element_located(self.postal_code_id))
         self.driver.find_element(*By_product.postal_code_id).send_keys(postalcode)

     def click_on_contineu_btn(self):
         self.wait.until(expected_conditions.presence_of_element_located(self.continue_btn_id))
         self.driver.find_element(*By_product.continue_btn_id).click()

     def click_on_finish_btn(self):
         self.wait.until(expected_conditions.presence_of_element_located(self.finish_btn_id))
         self.driver.find_element(*By_product.finish_btn_id).click()