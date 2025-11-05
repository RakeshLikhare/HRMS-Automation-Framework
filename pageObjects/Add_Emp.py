from selenium.webdriver.common.by import By


class AddEmployee:

    Click_PIM_Xpath=(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
    Click_ADD_EMP_Xpath = (By.XPATH, "//a[normalize-space()='Add Employee']")
    Text_Firstname_Xpath=(By.XPATH,"//input[@placeholder='First Name']")
    Text_Middlename_Xpath = (By.XPATH, "//input[@placeholder='Middle Name']")
    Text_Lastname_Xpath = (By.XPATH, "//input[@placeholder='Last Name']")
    Click_ADD_Photo_Xpath=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/input')
    Click_Createlogdetail_Xpath = (By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
    Text_Username_Xpath = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input')
    Click_Radiobutton_Xpath = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span')
    Text_Password_Xpath = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input')
    Text_ConPassword_Xpath = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input')
    Click_Savebutton_Xpath = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
    Text_Success_msg_Xpath=(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']")

    def __init__(self,driver):
        self.driver=driver

    def Click_PIM(self):
        self.driver.find_element(*AddEmployee.Click_PIM_Xpath).click()

    def Click_ADD_EMP(self):
        self.driver.find_element(*AddEmployee.Click_ADD_EMP_Xpath).click()

    def Enter_Firstname(self,firstname):
        self.driver.find_element(*AddEmployee.Text_Firstname_Xpath).send_keys(firstname)

    def Enter_Middlename(self,middlename):
        self.driver.find_element(*AddEmployee.Text_Middlename_Xpath).send_keys(middlename)

    def Enter_Lastname(self,lastname):
        self.driver.find_element(*AddEmployee.Text_Lastname_Xpath).send_keys(lastname)

    def Click_ADD_Photo(self,Path):
        self.driver.find_element(*AddEmployee.Click_ADD_Photo_Xpath).send_keys(Path)

    def Click_Createlogdetail(self):
        self.driver.find_element(*AddEmployee.Click_Createlogdetail_Xpath).click()

    def Enter_Username(self,username):
        self.driver.find_element(*AddEmployee.Text_Username_Xpath).send_keys(username)

    def Click_Radiobutton(self):
        self.driver.find_element(*AddEmployee.Click_Radiobutton_Xpath).click()

    def Enter_Password(self,password):
        self.driver.find_element(*AddEmployee.Text_Password_Xpath).send_keys(password)

    def Enter_ConPassword(self,confirmpassword):
        self.driver.find_element(*AddEmployee.Text_ConPassword_Xpath).send_keys(confirmpassword)

    def Click_Savebutton(self):
        self.driver.find_element(*AddEmployee.Click_Savebutton_Xpath).click()

    def Validate_addemp(self):
        try:
            success_msg=self.driver.find_element(*AddEmployee.Text_Success_msg_Xpath).text
            print("employee add process is complete successfully")
            return success_msg
        except:
            print("employee add process is face some issue")





