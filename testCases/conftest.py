import pytest
from selenium import webdriver

driver_path = "drivers/chromedriver.exe"


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# @pytest.fixture()
# def setup(browser):
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "edge":
#         driver = webdriver.Edge()
#     else:
#         driver = webdriver.Chrome()
#
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     return driver

from selenium import webdriver
import pytest

# browser = None
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Adjust the path to your Chrome executable
        driver_path = "Driver/chromedriver.exe"  # Adjust the path to your chromedriver.exe
        chrome_options.add_argument(f"executable_path={driver_path}")  # Add this line to set executable path
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Adjust the path to your Chrome executable
        driver_path = "Driver/chromedriver.exe"  # Adjust the path to your chromedriver.exe
        chrome_options.add_argument(f"executable_path={driver_path}")  # Add this line to set executable path
        driver = webdriver.Chrome(options=chrome_options)

    return driver







@pytest.fixture(
    params=[
        ("standard_user", "secret_sauce", "Pass"),
        ("locked_out_user", "secret_sauce", "Fail"),
        ("problem_user", "secret_sauce", "Pass"),
        ("performance_glitch_user", "secret_sauce", "Pass"),
    ]
)
def getDataForLogin(request):
    return request.param


import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "My Test Report"


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.append("<h2>My Custom Header</h2>")
