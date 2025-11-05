import time

import pytest

from Utilities.LoggerFile import LogGenerator
from Utilities.ReadconfiFile import ReadConfig
from pageObjects.Login_Page import LoginPage


class Test_login:
    username=ReadConfig.get_username()
    password=ReadConfig.get_password()
    log=LogGenerator.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_checkurl001(self,setup):
        self.log.info("test_checkurl001 is start")
        self.log.info("opening the browser")
        self.browser=setup
        self.log.info("Capturing page title")
        self.log.info("captured title is--->"+self.browser.title)
        print("title is--->"+self.browser.title)
        if self.browser.title == "OrangeHRM":
            time.sleep(2)
            self.log.info("Taking screenshot")
            self.browser.save_screenshot(".\\Screenshots\\test_checkurl001_pass.png")
            self.log.info("test_checkurl001 is pass")
            assert True
        else:
            self.log.info("test_checkurl001 is fail")
            assert False
        self.log.info("test_checkurl001 is end")
        self.log.info("browser closed")
        self.browser.quit()

    @pytest.mark.sanity
    @pytest.mark.group1
    def test_checklogin002(self,setup):
        self.log.info("test_checklogin002 is start")
        self.log.info("opening the browser")
        self.browser = setup
        self.lp=LoginPage(self.browser)
        self.log.info("enter username")
        self.log.info("username is--->"+self.username)
        self.lp.enter_username(self.username)
        self.log.info("enter password")
        self.log.info("password is--->"+self.password)
        self.lp.enter_password(self.password)
        self.log.info("click on login button")
        self.lp.click_login()
        try:
            self.log.info("validate login status")
            if self.lp.validate_login() == "loginpass":
                time.sleep(3)
                self.log.info("Taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_checklogin002_pass.png")
                self.log.info("click on dropdown menu")
                self.lp.click_menuDropdown()
                self.log.info("click on logout button")
                self.lp.click_logout()
                self.log.info("test_checklogin002 is pass")
                assert True
            else:
                time.sleep(2)
                self.log.info("Taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_checklogin002_fail.png")
                self.log.info("test_checklogin002 is fail")
                assert False
        finally:
            self.log.info("test_checklogin002 is end")
            self.log.info("browser closed")
            self.browser.quit()


