import time

import pytest

from Utilities.LoggerFile import LogGenerator
from Utilities.ReadconfiFile import ReadConfig
from pageObjects.Add_Emp import AddEmployee
from pageObjects.Login_Page import LoginPage
from pageObjects.Search_Emp import SearchEmployee


class Test_SearchEmployee_params:
    log=LogGenerator.loggen()
    username=ReadConfig.get_username()
    password=ReadConfig.get_password()

    @pytest.mark.regression1
    @pytest.mark.group00
    def test_SearchEmployee009(self,setup,SearchEmploye1):
        self.log.info("test_SearchEmployee009 is start")
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
        time.sleep(3)
        self.se=SearchEmployee(self.browser)
        self.log.info("entering employee name")
        self.log.info("employee name is-->"+SearchEmploye1[0])
        self.se.Enter_Employeename(SearchEmploye1[0])
        Emp_id=SearchEmploye1[1]
        self.log.info("entering employee id")
        self.log.info("employee id is-->"+Emp_id)
        self.se.Enter_Employeeid(Emp_id)
        self.log.info("click on search button")
        self.se.Searchbutton()
        time.sleep(5)
        self.log.info("validate searchemployee status")
        if self.se.ValidateEmployee_search() == Emp_id:
            self.browser.save_screenshot(".\\Screenshots\\test_SearchEmployee009_pass.png")
            self.log.info("Employee is found")
            self.log.info("test_SearchEmployee009 is pass")
            self.log.info("test_SearchEmployee009 is end")
            self.log.info("browser closed")
            assert True
        else:
            self.browser.save_screenshot(".\\Screenshots\\test_SearchEmployee009_fail.png")
            self.log.info("Employee not found")
            self.log.info("test_SearchEmployee009 is fail")
            assert False

##pytest -v --browser chrome --disable-warnings --html=HTMLReports/myreportSearchempParams.html "testCases/test_SearchEmployees params.py"
