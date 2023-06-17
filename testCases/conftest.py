
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome()
    else:
        driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver




@pytest.fixture(params= [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce")
])
def getDataForLogin(request):
    return request.param
# standard_user
# locked_out_user
# problem_user
# performance_glitch_user