import time

from Utilitis.readproperties import ReadValue
from PageObject.LoginPage import Login
from Utilitis.Logger import LogGen

class Test_Url_login():

    url=ReadValue.getUrl()
    log=LogGen.loggen()
    def test_login(self,setup,getDataForLogin):

        self.driver=setup
        self.driver.get(self.url)

        self.lp=Login(self.driver)

        self.lp.get_username(getDataForLogin[0])
        self.log.info("Entering username")
        self.lp.get_password(getDataForLogin[1])
        self.log.info("Entering password")
        self.lp.click_on_login()
        self.driver.save_screenshot('C:\\Users\\Admin\\PycharmProjects\\Swag_Labs_Project\\Screenshot\\login_succesfull.png')
        self.log.info("click on log in button")
        self.lp.click_on_menu()
        self.lp.click_on_logout()
        self.log.info("click on logout button")
        self.driver.save_screenshot('C:\\Users\\Admin\\PycharmProjects\\Swag_Labs_Project\\Screenshot'
                                    '\\logout_succesfull.png')
        self.driver.close()