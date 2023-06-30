
#
# import time
# from Utilitis.readproperties import ReadValue
# from PageObject.LoginPage import Login
# from Utilitis.Logger import LogGen
#
# class Test_Url_login():
#
#     url=ReadValue.getUrl()
#     username=ReadValue.getusername()
#     password=ReadValue.getPassword()
#     log=LogGen.loggen()
#     def test_login(self,setup):
#
#         self.driver=setup
#         self.driver.get(self.url)
#
#         self.lp=Login(self.driver)
#
#         self.lp.get_username(self.username)
#         self.log.info("Entering username----->"+ self.username)
#         self.lp.get_password(self.password)
#         self.log.info("Entering password------>",self.username)
#         self.lp.click_on_login()
#
#         self.log.info("click on log in button")
#         if self.lp.login_status()==True:
#             self.log.info('login test is pass')
#             self.driver.save_screenshot(
#                 'C:\\Users\\Admin\\PycharmProjects\\Swag_Labs_Project\\Screenshot\\login_succesfull.png')
#
#             self.lp.click_on_menu()
#             self.lp.click_on_logout()
#             self.log.info("click on logout button")
#             self.driver.save_screenshot('C:\\Users\\Admin\\PycharmProjects\\Swag_Labs_Project\\Screenshot'
#                                     '\\logout_succesfull.png')
#             assert True
#         else:
#             self.log.info("test_login is Failed")
#             self.driver.save_screenshot(
#                 "C:\\Users\\Admin\\PycharmProjects\\Swag_Labs_Project\\Screenshot\\login_fail.png")
#             assert False
#         self.driver.close()
#         self.log.info("test_login is Completed")


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.find_element(By.ID,'user-name').send_keys('standard_user')
# driver.find_element(By.ID,'password').send_keys('secret_sauce')
# driver.find_element(By.ID,'login-button').click()
# time.sleep(3)
# driver.find_element(By.ID,'react-burger-menu-btn').click()
# time.sleep(5)
# driver.find_element(By.ID,"logout_sidebar_link").click()
# time.sleep(3)
