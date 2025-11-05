import pytest
from selenium import webdriver

chrome_option=webdriver.ChromeOptions()
chrome_option.add_argument("headless")

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture
def setup(request):
    browser=request.config.getoption("--browser")

    if browser=="chrome":
        print("\nbrowser run in chrome")
        driver=webdriver.Chrome()

    elif browser=="firefox":
        print("\nbrowser run in firefox")
        driver=webdriver.Firefox()

    elif browser=="edge":
        print("\nbrowser run in edge")
        driver=webdriver.Edge()

    else:
        print("\nheadless browser")
        driver = webdriver.Chrome(options=chrome_option)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(params=[
    ("Admin","admin123","Login_Pass"),
    ("Admin1","admin123","Login_Fail"),
    ("Admin","admin1234","Login_Fail"),
    ("Admin1","admin1234","Login_Fail")
])
def GetDataForLogin(request):
    return request.param


@pytest.fixture(params=[
    ("Rakesh","D","Likhare"),
    ("Pranay","W","Kadaskar"),
    ("Vijay","S","Rathod"),
    ("Shubham","S","Share")
])
def AddNewemployee(request):
    return request.param


@pytest.fixture(params=[
    ("Ash Tyson","0367"),
    ("Charlotte","00392"),
    ("Charles Carter","0320"),
    ("Amelia Brown","01715")
])
def SearchEmploye1(request):
    return request.param