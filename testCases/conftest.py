import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")  # default set to chrome

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class")
def setup(request, browser):
    if browser == "chrome":
        options = Options()

        # Enable headless mode only in CI (like GitHub Actions)
        if os.getenv("CI", "").lower() == "true":
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    elif browser == "edge":
        options = EdgeOptions()

        if os.getenv("CI", "").lower() == "true":
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Edge(options=options)

    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver
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


@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "My Test Report"


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix):
    prefix.append("<h2>My Custom Header</h2>")



@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix):
    prefix.append("<h2>My Custom Header</h2>")
