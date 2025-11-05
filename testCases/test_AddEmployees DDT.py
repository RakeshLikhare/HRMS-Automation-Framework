import time

import pytest

from Utilities.LoggerFile import LogGenerator
from Utilities.ReadconfiFile import ReadConfig
from pageObjects.Add_Emp import AddEmployee
from pageObjects.Login_Page import LoginPage
from Utilities import Excel_utils

class Test_AddEmployees_DTT:
    log=LogGenerator.loggen()
    username=ReadConfig.get_username()
    password=ReadConfig.get_password()
    file_path=".\\testCases\\Test_Data\\Test_AddEmployees1.XLSX"

    @pytest.mark.group23
    def test_AddEmployees_DDT008(self,setup):
        self.log.info("test_AddEmployees_DDT008 is start")
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
        self.rows=Excel_utils.GetRowcount(self.file_path,"Add_Employees")
        print("Number of rows in our Excel sheet---->"+str(self.rows))
        self.log.info("Number of rows in our Excel sheet---->" + str(self.rows))
        for r in range(2,self.rows+1):
            print("employee data rcv from row no"+" "+str(r))
            self.first_name=Excel_utils.read_data(self.file_path,"Add_Employees",r,2)
            self.middle_name=Excel_utils.read_data(self.file_path,"Add_Employees",r,3)
            self.last_name=Excel_utils.read_data(self.file_path,"Add_Employees",r,4)
            self.log.info("click on ADD Employee")
            self.ae.Click_ADD_EMP()
            self.log.info("employee data rcv from row no" + " " + str(r))
            self.log.info("entering firstname")
            self.ae.Enter_Firstname(self.first_name)
            self.log.info("first name is--->" + self.first_name)
            print("first name is--->" + self.first_name)
            self.log.info("entering middlename")
            self.ae.Enter_Middlename(self.middle_name)
            self.log.info("middle name is--->" + self.middle_name)
            print("middle name is--->" + self.middle_name)
            self.log.info("entering lastname")
            self.ae.Enter_Lastname(self.last_name)
            self.log.info("last name is--->" + self.last_name)
            print("last name is--->" + self.last_name)
            path = "C:\\Users\\hp\\Downloads\\ChatGPT Image Oct 11, 2025, 10_10_20 PM.png"
            self.log.info("uploading photo")
            self.ae.Click_ADD_Photo(path)
            self.log.info("click on Createlogdetail toggle")
            self.ae.Click_Createlogdetail()
            self.log.info("entering Username")
            self.ae.Enter_Username("Rakesh83")
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
        self.log.info("validate employeeadd status")
        time.sleep(5)
        if self.ae.Validate_addemp() == "Successfully Saved":
            self.browser.save_screenshot(".\\Screenshots\\test_AddEmployees_DDT008_pass.png")
            self.log.info("test_AddEmployees_DDT008 is pass")
            self.log.info("test_AddEmployees_DDT008 is end")
            self.log.info("browser closed")
            assert True
        else:
            self.browser.save_screenshot(".\\Screenshots\\test_AddEmployees_DDT008_fail.png")
            self.log.info("test_AddEmployees_DDT008 is fail")
            assert False


###pytest -v  --browser chrome --html=HTMLReports/myreportADDempDDT.html "testCases/test_AddEmployees DDT.py" --disable-warnings


