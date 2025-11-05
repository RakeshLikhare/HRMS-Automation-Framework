import time

from selenium.webdriver import Keys     ##ye library import krni padi for select and delete
from selenium.webdriver.common.by import By


class SearchEmployee:
    Text_Employeename_Xpath=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
    Text_Employeeid_Xpath=(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input")
    Click_Searchbutton_Xpath=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
    Text_Employeefound_Xpath=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div')

    def __init__(self,driver):
        self.driver=driver

    def Enter_Employeename(self,employeename):
        self.driver.find_element(*SearchEmployee.Text_Employeename_Xpath).send_keys(Keys.CONTROL + "a")  # select all text
        self.driver.find_element(*SearchEmployee.Text_Employeename_Xpath).send_keys(Keys.BACKSPACE)    #delete
        time.sleep(2)
        self.driver.find_element(*SearchEmployee.Text_Employeename_Xpath).send_keys(employeename)

    def Enter_Employeeid(self,employeeid):
        self.driver.find_element(*SearchEmployee.Text_Employeeid_Xpath).send_keys(Keys.CONTROL + "a")   # select all text
        self.driver.find_element(*SearchEmployee.Text_Employeeid_Xpath).send_keys(Keys.BACKSPACE)    #delete
        time.sleep(2)
        self.driver.find_element(*SearchEmployee.Text_Employeeid_Xpath).send_keys(employeeid)

    def Searchbutton(self):
        self.driver.find_element(*SearchEmployee.Click_Searchbutton_Xpath).click()

    def ValidateEmployee_search(self):
        try:
            Empsearch = self.driver.find_element(*SearchEmployee.Text_Employeefound_Xpath).text
            print("employee search successfully")
            return Empsearch
        except:
            print("some issues found during employee search")









