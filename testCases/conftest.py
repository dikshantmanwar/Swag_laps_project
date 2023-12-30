import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
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
