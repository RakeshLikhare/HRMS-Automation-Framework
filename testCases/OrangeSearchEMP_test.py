import time

import pytest

from Utilities.LoggerFile import LogGenerator
from Utilities.ReadconfiFile import ReadConfig
from pageObjects.Add_Emp import AddEmployee
from pageObjects.Login_Page import LoginPage
from pageObjects.Search_Emp import SearchEmployee


class Test_SearchEmployee:
    username=ReadConfig.get_username()
    password=ReadConfig.get_password()
    log=LogGenerator.loggen()

    @pytest.mark.regression
    @pytest.mark.group17
    def test_SearchEmployee006(self,setup):
        self.log.info("test_SearchEmployee006 is start")
        self.log.info("opening the browser")
        self.browser = setup
        self.lp = LoginPage(self.browser)
        self.log.info("enter username")
        self.log.info("username is--->" + str(self.username))
        self.lp.enter_username(self.username)
        self.log.info("enter password")
        self.log.info("password is--->" + str(self.password))
        self.lp.enter_password(self.password)
        self.log.info("click on login button")
        self.lp.click_login()
        time.sleep(3)
        self.ae = AddEmployee(self.browser)
        self.log.info("click on PIM")
        self.ae.Click_PIM()
        self.se=SearchEmployee(self.browser)
        self.log.info("entering employee name")
        self.se.Enter_Employeename("james")
        Emp_id="0365"
        self.log.info("entering employee id")
        self.se.Enter_Employeeid(Emp_id)
        self.log.info("click on search button")
        self.se.Searchbutton()
        time.sleep(5)
        self.log.info("validate searchemployee status")
        if self.se.ValidateEmployee_search() == Emp_id:
            self.browser.save_screenshot(".\\Screenshots\\test_SearchEmployee006_pass.png")
            self.log.info("test_SearchEmployee006 is pass")
            self.log.info("test_SearchEmployee006 is end")
            self.log.info("browser closed")
            assert True
        else:
            self.browser.save_screenshot(".\\Screenshots\\test_SearchEmployee006_fail.png")
            self.log.info("test_SearchEmployee006 is fail")
            assert False

##pytest -v --browser chrome --html=HTMLReports/myreport4SearchEmp.html "testCases/OrangeSearchEMP_test.py" --disable-warnings

