import time

import pytest

from Utilities.LoggerFile import LogGenerator
from Utilities.ReadconfiFile import ReadConfig
from pageObjects.Add_Emp import AddEmployee
from pageObjects.Login_Page import LoginPage
from Utilities import Excel_utils
from pageObjects.Search_Emp import SearchEmployee


class Test_SearchEmployees_DTT:
    log=LogGenerator.loggen()
    username=ReadConfig.get_username()
    password=ReadConfig.get_password()
    file_path=".\\testCases\\Test_Data\\Test_Data6.XLSX"

    @pytest.mark.group44
    def test_SearchEmployees_DDT010(self,setup):
        self.log.info("test_SearchEmployees_DDT010 is start")
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
        self.rows=Excel_utils.GetRowcount(self.file_path,"Search_Employee")
        print("Number of rows in our Excel sheet---->"+str(self.rows))
        self.log.info("Number of rows in our Excel sheet---->" + str(self.rows))
        for r in range(2,self.rows+1):
            print("employee data rcv from row no"+" "+str(r))
            self.employee_name=Excel_utils.read_data(self.file_path,"Search_Employee",r,2)
            self.employee_id=Excel_utils.read_data(self.file_path,"Search_Employee",r,3)
            print("employeename is--->"+ str(self.employee_name))
            print("employeeid is--->"+ str(self.employee_id))
            self.se = SearchEmployee(self.browser)
            self.log.info("entering employee name")
            self.log.info("employee name is-->" + str(self.employee_name))
            self.se.Enter_Employeename(self.employee_name)
            Emp_id = self.employee_id
            self.log.info("entering employee id")
            self.log.info("employee id is-->" + Emp_id)
            self.se.Enter_Employeeid(Emp_id)
            self.log.info("click on search button")
            self.log.info("Employee is found")
            self.se.Searchbutton()
            time.sleep(5)
        self.log.info("validate searchemployee status")
        if self.se.ValidateEmployee_search() == Emp_id:
            self.browser.save_screenshot(".\\Screenshots\\test_SearchEmployees_DDT010_pass.png")
            self.log.info("All Employee is found")
            self.log.info("test_SearchEmployees_DDT010 is pass")
            self.log.info("test_SearchEmployees_DDT010 is end")
            self.log.info("browser closed")
            assert True
        else:
            self.browser.save_screenshot(".\\Screenshots\\test_SearchEmployees_DDT010_fail.png")
            self.log.info("Employee not found")
            self.log.info("test_SearchEmployees_DDT010 is fail")
            assert False

###pytest -v --browser chrome --disable-warnings "testCases/test_SearchEmployees DDT.py" --html=HTMLReports/myreportSearchempDDT.html
