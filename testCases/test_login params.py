import time

import pytest

from Utilities.LoggerFile import LogGenerator
from Utilities.ReadconfiFile import ReadConfig
from pageObjects.Login_Page import LoginPage


class Test_login_params:
    log=LogGenerator.loggen()

    @pytest.mark.group2
    @pytest.mark.sanity
    def test_checklogin_params003(self,setup,GetDataForLogin):
        self.log.info("test_checklogin_params003 is start")
        self.log.info("opening the browser")
        self.browser = setup
        self.lp=LoginPage(self.browser)
        self.log.info("enter username")
        self.log.info("username is--->"+GetDataForLogin[0])
        self.lp.enter_username(GetDataForLogin[0])
        self.log.info("enter password")
        self.log.info("password is--->"+GetDataForLogin[1])
        self.lp.enter_password(GetDataForLogin[1])
        self.log.info("click on login button")
        self.lp.click_login()
        try:
            self.log.info("validate login status")
            if self.lp.validate_login() == "loginpass" and GetDataForLogin[2]=="Login_Pass":
                time.sleep(3)
                self.log.info("Taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_checklogin_params003_pass.png")
                self.log.info("click on dropdown menu")
                self.lp.click_menuDropdown()
                self.log.info("click on logout button")
                self.lp.click_logout()
                self.log.info("test_checklogin_params003 is pass")
                assert True
            elif self.lp.validate_login() == "loginpass" and GetDataForLogin[2]=="Login_Fail":
                time.sleep(3)
                self.log.info("Taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_checklogin_params003_pass.png")
                self.log.info("click on dropdown menu")
                self.lp.click_menuDropdown()
                self.log.info("click on logout button")
                self.lp.click_logout()
                self.log.info("test_checklogin_params003 is pass")
                assert False
            elif self.lp.validate_login() == "loginfail" and GetDataForLogin[2]=="Login_Pass":
                time.sleep(3)
                self.log.info("Taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_checklogin_params003_fail.png")
                self.log.info("test_checklogin_params003 is fail")
                assert False
            elif self.lp.validate_login() == "loginfail" and GetDataForLogin[2]=="Login_Fail":
                time.sleep(2)
                self.log.info("Taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_checklogin_params003_fail.png")
                self.log.info("test_checklogin_params003 is fail")
                assert True
        finally:
            self.log.info("test_checklogin_params003 is end")
            self.log.info("browser closed")
            self.browser.quit()


###pytest -v  --browser chrome --html=HTMLReports/myreport1Prrams.html "testCases/test_login params.py"
