pytest -v --browser firefox --html=HTMLReports/myreportxyzBbat.html "testCases/OrangeAddEmp_test.py" --disable-warnings -m "group11 and sanity" --alluredir="AllureReports"

allure serve "AllureReports"