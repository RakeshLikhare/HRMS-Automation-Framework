import time

import pytest

from Utilities.LoggerFile import LogGenerator
from Utilities.ReadconfiFile import ReadConfig
from pageObjects.Login_Page import LoginPage
from Utilities import Excel_utils

class Test_login_DTT:
    log=LogGenerator.loggen()
    file_path=".\\testCases\\Test_Data\\Test_Data8.xlsx"

    @pytest.mark.group6
    @pytest.mark.sanity
    def test_checklogin_DDT004(self,setup):
        self.log.info("test_checklogin_DDT004 is start")
        self.log.info("opening the browser")
        list_status=[]
        self.browser = setup
        self.lp=LoginPage(self.browser)
        self.rows=Excel_utils.GetRowcount(self.file_path,"Login_Data")
        self.log.info("rows in our excel sheet--->" + str(self.rows))
        print("rows in our excel sheet--->"+str(self.rows))
        for r in range(2,self.rows+1):
            self.username=Excel_utils.read_data(self.file_path,"Login_Data",r,2)
            self.password=Excel_utils.read_data(self.file_path, "Login_Data",r,3)
            self.Expected_Result = Excel_utils.read_data(self.file_path, "Login_Data",r,4)
            # print("username is--->"+self.username)
            # print("password is--->"+self.password)
            # print("Expected_Result is--->" +self.Expected_Result)
            self.log.info("this username and password entered for row no"+" "+str(r))
            self.log.info("enter username")
            self.log.info("username is--->" + str(self.username))
            self.lp.enter_username(self.username)
            self.log.info("enter password")
            self.log.info("password is--->" + str(self.password))
            self.lp.enter_password(self.password)
            self.log.info("click on login button")
            self.lp.click_login()
            self.log.info("validate login status")
            if self.lp.validate_login() == "loginpass" and self.Expected_Result == "Login_Pass":
                self.log.info("appending value in list")
                list_status.append("Pass")
                Excel_utils.write_data(self.file_path, "Login_Data",r,5,"Pass")
                time.sleep(3)
                self.log.info("Taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_checklogin_DDT004_pass.png")
                self.log.info("click on dropdown menu")
                self.lp.click_menuDropdown()
                self.log.info("click on logout button")
                self.lp.click_logout()
            elif self.lp.validate_login() == "loginpass" and self.Expected_Result == "Login_Fail":
                self.log.info("appending value in list")
                list_status.append("Fail")
                Excel_utils.write_data(self.file_path, "Login_Data", r, 5, "Fail")
                time.sleep(3)
                self.log.info("Taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_checklogin_DDT004_pass.png")
                self.log.info("click on dropdown menu")
                self.lp.click_menuDropdown()
                self.log.info("click on logout button")
                self.lp.click_logout()
            elif self.lp.validate_login() == "loginfail" and self.Expected_Result == "Login_Pass":
                self.log.info("appending value in list")
                list_status.append("Fail")
                Excel_utils.write_data(self.file_path, "Login_Data", r, 5, "Fail")
                time.sleep(3)
                self.log.info("Taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_checklogin_DDT004_fail.png")
            elif self.lp.validate_login() == "loginfail" and self.Expected_Result == "Login_Fail":
                self.log.info("appending value in list")
                list_status.append("Pass")
                Excel_utils.write_data(self.file_path, "Login_Data", r, 5, "Pass")
                time.sleep(2)
                self.log.info("Taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_checklogin_DDT004_fail.png")
        print(list_status)
        if "Fail" not in list_status:
            assert True
            self.log.info("test_checklogin_DDT004 is pass")
            self.log.info("test_checklogin_DDT004 is end")
            self.log.info("browser closed")
        else:
            self.log.info("test_checklogin_DDT004 is fail")
            assert False

###pytest -v  --browser chrome --html=HTMLReports/myreport2DDT.html "testCases/test_login DDT.py"

