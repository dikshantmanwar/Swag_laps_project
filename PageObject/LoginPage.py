from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login():
     username_id=(By.ID,'user-name')
     password_id=(By.ID,'password')
     login_id=(By.ID,'login-button')
     menu_button_id=(By.ID,'react-burger-menu-btn')
     logout_id=(By.ID,"logout_sidebar_link")

     def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,5)

     def get_username(self,username):
         self.wait.until(expected_conditions.presence_of_element_located(self.username_id))
         self.driver.find_element(*Login.username_id).send_keys(username)

     def get_password(self,password):
         self.wait.until(expected_conditions.presence_of_element_located(self.password_id))
         self.driver.find_element(*Login.password_id).send_keys(password)

     def click_on_login(self):
         self.wait.until(expected_conditions.element_to_be_clickable(self.login_id))
         self.driver.find_element(*Login.login_id).click()

     def click_on_menu(self):
         self.wait.until(expected_conditions.element_to_be_clickable(self.menu_button_id))
         self.driver.find_element(*Login.menu_button_id).click()

     def click_on_logout(self):
         self.wait.until(expected_conditions.element_to_be_clickable(self.logout_id))
         self.driver.find_element(*Login.logout_id).click()

     def login_status(self):
         try:
             self.wait.until(expected_conditions.presence_of_element_located(self.menu_button_id))
             self.driver.find_element(*Login.menu_button_id)
             return True
         except (NoSuchElementException, TimeoutException):
             return False
