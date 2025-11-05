import time

import pytest

from Utilities.LoggerFile import LogGenerator
from Utilities.ReadconfiFile import ReadConfig
from pageObjects.Add_Emp import AddEmployee
from pageObjects.Login_Page import LoginPage


class Test_AddEmployee:
    username=ReadConfig.get_username()
    password=ReadConfig.get_password()
    log=LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.group11
    def test_OrangeAddEmployee005(self,setup):
        self.log.info("test_OrangeAddEmployee005 is start")
        self.log.info("opening the browser")
        self.browser=setup
        self.lp=LoginPage(self.browser)
        self.log.info("enter username")
        self.log.info("username is--->" + str(self.username))
        self.lp.enter_username(self.username)
        self.log.info("enter password")
        self.log.info("password is--->" + str(self.password))
        self.lp.enter_password(self.password)
        self.log.info("click on login button")
        self.lp.click_login()
        time.sleep(3)
        self.ae=AddEmployee(self.browser)
        self.log.info("click on PIM")
        self.ae.Click_PIM()
        self.log.info("click on ADD Employee")
        self.ae.Click_ADD_EMP()
        self.log.info("entering firstname")
        self.ae.Enter_Firstname("Rakesh")
        self.log.info("entering middlename")
        self.ae.Enter_Middlename("d")
        self.log.info("entering lastname")
        self.ae.Enter_Lastname("Likhare")
        path="C:\\Users\\hp\\Downloads\\ChatGPT Image Oct 11, 2025, 10_10_20 PM.png"
        self.log.info("uploading photo")
        self.ae.Click_ADD_Photo(path)
        self.log.info("click on Createlogdetail toggle")
        self.ae.Click_Createlogdetail()
        self.log.info("entering Username")
        self.ae.Enter_Username("Rakesh7345")
        self.log.info("entering Password")
        self.ae.Enter_Password("Rakesh123")
        self.log.info("entering Confirm Password")
        self.ae.Enter_ConPassword("Rakesh123")
        time.sleep(2)
        self.log.info("click on enable radio button")
        self.ae.Click_Radiobutton()
        time.sleep(4)
        self.log.info("click on save button")
        self.ae.Click_Savebutton()
        time.sleep(4)
        self.log.info("validate employeeadd status")
        if self.ae.Validate_addemp() == "Successfully Saved":
            self.browser.save_screenshot(".\\Screenshots\\test_OrangeAddEmployee005_pass.png")
            self.log.info("test_OrangeAddEmployee005 is pass")
            self.log.info("test_OrangeAddEmployee005 is end")
            self.log.info("browser closed")
            assert True
        else:
            self.browser.save_screenshot(".\\Screenshots\\test_OrangeAddEmployee005_fail.png")
            self.log.info("test_OrangeAddEmployee005 is fail")
            assert False

##pytest -v --browser chrome --html=HTMLReports/myreport3ADDEmp.html "testCases/OrangeAddEmp_test.py" --disable-warnings
