# HRMS Automation Framework

## Project Overview
This project is a Selenium WebDriver automation framework developed using Python and PyTest. It follows the Page Object Model (POM) design pattern to improve code reusability, maintainability, and readability.

The framework automates key HRMS application flows such as login, employee creation, employee search, data-driven testing, cross-browser execution, screenshot capture, and report generation.

## Tech Stack
- Python
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- Data Driven Testing
- HTML Reports
- Allure Reports
- OpenPyXL

## Features
- Login test automation
- Add employee test automation
- Search employee test automation
- Data-driven testing using Excel
- Parameterized test execution
- Cross-browser execution on Chrome, Edge, and Firefox
- Screenshot capture on test failure
- HTML report generation
- Allure report generation
- Logging support
- Configuration management using config.ini

## Project Structure
```text
HRMS-Automation-Framework
│
├── Configuration
│   └── config.ini
│
├── pageObjects
│   └── Page object classes
│
├── testCases
│   └── Test scripts
│
├── Utilities
│   └── Reusable utility methods
│
├── HTMLReports
│   └── HTML test execution reports
│
├── Screenshots
│   └── Failure screenshots
│
├── allure-report
│   └── Allure report files
│
├── requirements.txt
└── README.md
```

## Installation
Clone the repository:

```bash
git clone https://github.com/RakeshLikhare/HRMS-Automation-Framework.git
```

Go to the project folder:

```bash
cd HRMS-Automation-Framework
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

## How to Run Tests
Run all tests:
```bash
pytest
```

Run tests on Chrome browser:
```bash
pytest -v --browser chrome
```

Run tests with HTML report:
```bash
pytest -v --browser chrome --html=HTMLReports/myreport.html
```

Generate Allure report:
```bash
allure serve allure-report
```

## Test Scenarios Covered
- Verify login with valid credentials
- Verify login with invalid credentials
- Add new employee
- Search existing employee
- Data-driven login validation
- Parameterized employee test execution
- Cross-browser test execution

## Reports
The framework supports:
- HTML Report
- Allure Report
- Screenshot capture on failure

## Author
Rakesh Likhare
