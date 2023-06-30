# import time
#
# from Utilitis.readproperties import ReadValue
# from PageObject.LoginPage import Login
# from Utilitis.Logger import LogGen
#
# class Test_Url_login():
#
#     url=ReadValue.getUrl()
#     log=LogGen.loggen()
#     def test_login(self,setup,getDataForLogin):
#
#         self.driver=setup
#         self.driver.get(self.url)
#
#         self.lp=Login(self.driver)
#
#         self.lp.get_username(getDataForLogin[0])
#         self.log.info("Entering username---->"+getDataForLogin[0])
#         self.lp.get_password(getDataForLogin[1])
#         self.log.info("Entering password---------->"+getDataForLogin[0])
#         self.lp.click_on_login()
#         self.driver.save_screenshot('C:\\Users\\Admin\\PycharmProjects\\Swag_Labs_Project\\Screenshot\\login_succesfull.png')
#         self.log.info("click on log in button")
#
#
#         login_stauts=[]
#         if self.lp.login_status() == True:
#             if getDataForLogin[2] == "Pass":
#                 login_stauts.append("Pass")
#                 self.driver.save_screenshot(
#                     'C:\\Users\\Admin\\PycharmProjects\\Swag_Labs_Project\\Screenshot\\login_test_pass'
#                                             '.png')
#                 self.lp.click_on_menu()
#                 self.log.info("Click on menu button")
#                 self.lp.click_on_logout()
#                 self.log.info("Click on logout button")
#             elif getDataForLogin[2] == "Fail":
#                 login_stauts.append("Fail")
#                 self.driver.save_screenshot(
#                     'C:\\Users\\Admin\\PycharmProjects\\Swag_Labs_Project\\Screenshot\\login_test_pass'
#                                             '.png')
#                 self.lp.click_on_menu()
#                 self.log.info("Click on menu button")
#                 self.lp.click_on_logout()
#                 self.log.info("Click on logout button")
#
#             #assert True
#         else:
#             if getDataForLogin[2] == "Fail":
#                 login_stauts.append("Pass")
#                 self.driver.save_screenshot(
#                     'C:\\Users\\Admin\\PycharmProjects\\Swag_Labs_Project\\Screenshot\\login_param_test_fail_'
#                                             '.png')
#             elif getDataForLogin[2] == "Pass":
#                 login_stauts.append("Fail")
#                 self.driver.save_screenshot(
#                     'C:\\Users\\Admin\\PycharmProjects\\Swag_Labs_Project\\Screenshot\\login_param_test_fail'
#                                             '.png')
#         print(login_stauts)
#
#         if "Fail" not in login_stauts:
#             self.log.info("test_login_params is Passed")
#             assert True
#         else:
#             self.log.info("test_login_params is Failed")
#             assert False
#         self.driver.close()
#         self.log.info("test_login_params is Completed")
#
#
