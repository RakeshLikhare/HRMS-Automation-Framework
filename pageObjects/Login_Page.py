from selenium.webdriver.common.by import By


class LoginPage:
    Text_username_xpath=(By.XPATH,"//input[@placeholder='Username']")
    Text_password_xpath=(By.XPATH,"//input[@placeholder='Password']")
    Click_loginButton_Xpath=(By.XPATH,"//button[@type='submit']")
    Click_droMenu_Xpath=(By.XPATH,"//span[@class='oxd-userdropdown-tab']")
    Click_logoutButton_Xpath=(By.XPATH,"//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        self.driver.find_element(*LoginPage.Text_username_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*LoginPage.Text_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPage.Click_loginButton_Xpath).click()

    def click_menuDropdown(self):
        self.driver.find_element(*LoginPage.Click_droMenu_Xpath).click()

    def click_logout(self):
        self.driver.find_element(*LoginPage.Click_logoutButton_Xpath).click()

    def validate_login(self):
        try:
            self.driver.find_element(*LoginPage.Click_droMenu_Xpath)
            print("login pass successfully")
            return "loginpass"
        except:
            print("login process face some issues")
            return "loginfail"



