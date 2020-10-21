from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument("--disable-gpu")
    chrome_option.add_argument("--disable-pop-blocking")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\Selenium\\chromedriver.exe", options=chrome_option)
        print("*******Launching Chrome Browser************")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:\\Selenium\\geckodriver.exe")
        print("*******Launching Firefox Browser************")
    else:
        driver = webdriver.Chrome(executable_path="C:\\Selenium\\chromedriver.exe", options=chrome_option)
        print("*******Launching Chrome Browser************")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI or hook
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the value of browser
    return request.config.getoption("--browser")


# *************Reports**************
# This is hook of adding Environment info to HTML Reports
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customer Module'
    config._metadata['Tester'] = 'Praveen'

# This is hook of deleting/modifying Environment info to HTML Reports
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
