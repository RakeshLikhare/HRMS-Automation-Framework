import time

import pytest

from Utilities.LoggerFile import LogGenerator
from Utilities.ReadconfiFile import ReadConfig
from pageObjects.Add_Emp import AddEmployee
from pageObjects.Login_Page import LoginPage


class Test_AddEmployee_params:
    log=LogGenerator.loggen()
    username=ReadConfig.get_username()
    password=ReadConfig.get_password()

    @pytest.mark.group2
    @pytest.mark.sanity
    def test_AddEmployee_params007(self,setup,):
        self.log.info("test_AddEmployee_params007 is start")
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
        self.ae = AddEmployee(self.browser)
        self.log.info("click on PIM")
        self.ae.Click_PIM()
        self.log.info("click on ADD Employee")
        self.ae.Click_ADD_EMP()
        self.log.info("entering firstname")
        self.ae.Enter_Firstname(AddNewemployee[0])
        self.log.info("entering middlename")
        self.ae.Enter_Middlename(AddNewemployee[1])
        self.log.info("entering lastname")
        self.ae.Enter_Lastname(AddNewemployee[2])
        path = "C:\\Users\\hp\\Downloads\\ChatGPT Image Oct 11, 2025, 10_10_20 PM.png"
        self.log.info("uploading photo")
        self.ae.Click_ADD_Photo(path)
        time.sleep(4)
        self.log.info("click on save button")
        self.ae.Click_Savebutton()
        self.log.info("validate employeeadd status")
        if self.ae.Validate_addemp() == "Successfully Saved":
            self.browser.save_screenshot(".\\Screenshots\\test_AddEmployee_params007_pass.png")
            self.log.info("test_AddEmployee_params007 is pass")
            self.log.info("test_AddEmployee_params007 is end")
            self.log.info("browser closed")
            assert True
        else:
            self.browser.save_screenshot(".\\Screenshots\\test_AddEmployee_params007_fail.png")
            self.log.info("test_AddEmployee_params007 is fail")
            assert False


##pytest -v  --browser chrome --html=HTMLReports/myreportADDempParams.html "testCases/test_AddEmployees DDT.py" --disable-warnings