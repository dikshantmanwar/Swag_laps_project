import os
import pytest
import tempfile
import shutil
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions

# Import pytest-html for screenshot attachment
try:
    from pytest_html import extras as pytest_html
except ImportError:
    pytest_html = None


def pytest_addoption(parser):
    parser.addoption("--browsername", action="store", default="chrome")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browsername")


# Pytest-html report customization
def pytest_configure(config):
    """Configure pytest-html report with custom metadata"""
    config._metadata = {
        "Project Name": "Swag Labs Automation",
        "Test Environment": "QA",
        "Application URL": "https://www.saucedemo.com/",
        "Tester": "Dikshant Manwar",
        "Browser": config.getoption("--browsername"),
        "Execution Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    """Customize report title"""
    report.title = "Swag Labs Test Automation Report"


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary_prefix(prefix):
    """Add custom CSS styling to the report"""
    prefix.extend([
        '<style>',
        'body { font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; background-color: #f5f5f5; }',
        'h1 { color: white; text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 8px; margin-bottom: 30px; }',
        'h2 { color: #34495e; border-bottom: 2px solid #3498db; padding-bottom: 10px; }',
        'table { border-collapse: collapse; width: 100%; background-color: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; }',
        'th { background-color: #3498db; color: white; padding: 12px; text-align: left; font-weight: 600; }',
        'td { padding: 10px; border-bottom: 1px solid #ecf0f1; }',
        'tr:hover { background-color: #f8f9fa; }',
        '.passed { color: #27ae60; font-weight: bold; }',
        '.failed { color: #e74c3c; font-weight: bold; }',
        '.skipped { color: #f39c12; font-weight: bold; }',
        '.error { color: #c0392b; font-weight: bold; }',
        '#environment, #summary { background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 20px; }',
        'img { border: 2px solid #ddd; border-radius: 4px; padding: 5px; cursor: pointer; transition: transform 0.2s; }',
        'img:hover { transform: scale(1.05); box-shadow: 0 4px 8px rgba(0,0,0,0.2); }',
        '</style>'
    ])


def pytest_html_results_table_header(cells):
    """Customize table headers"""
    cells.insert(2, '<th>Description</th>')
    cells.insert(3, '<th>Time</th>')


def pytest_html_results_table_row(report, cells):
    """Customize table rows"""
    description = getattr(report, "description", "")
    cells.insert(2, f'<td>{description}</td>')
    cells.insert(3, f'<td>{datetime.now().strftime("%H:%M:%S")}</td>')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure and attach to report"""
    outcome = yield
    report = outcome.get_result()
    
    # Add test description from docstring
    docstring = getattr(item.function, '__doc__', '')
    report.description = docstring.strip() if docstring else ""
    
    extras = getattr(report, "extras", [])
    
    if report.when == "call" and report.failed:
        # Capture screenshot on failure
        if "setup" in item.fixturenames:
            try:
                driver = item.funcargs.get("setup")
                if driver:
                    # Create screenshot directory if not exists
                    screenshot_dir = "Screenshot"
                    os.makedirs(screenshot_dir, exist_ok=True)
                    
                    # Generate screenshot filename
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    test_name = item.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
                    screenshot_name = f"{test_name}_{timestamp}.png"
                    screenshot_path = os.path.join(screenshot_dir, screenshot_name)
                    
                    # Take screenshot
                    driver.save_screenshot(screenshot_path)
                    
                    # Attach to HTML report
                    if screenshot_path and pytest_html:
                        html = f'<div><img src="../{screenshot_path}" alt="screenshot" style="width:600px;height:400px;" ' \
                               f'onclick="window.open(this.src)" align="right"/></div>'
                        extras.append(pytest_html.html(html))
            except Exception as e:
                print(f"Failed to capture screenshot: {str(e)}")
    
    report.extras = extras


def get_browser_options(browser_type):
    """Returns configured browser options"""
    user_data_dir = tempfile.mkdtemp(prefix=f"{browser_type}_test_profile_")
    
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "autofill.profile_enabled": False,
        "autofill.enabled": False,
        "profile.password_manager_leak_detection": False,
    }
    
    common_args = [
        f"--user-data-dir={user_data_dir}",
        "--disable-blink-features=AutomationControlled",
        "--disable-save-password-bubble",
        "--disable-features=PasswordManager,PasswordManagerOnboarding",
        "--disable-password-manager-reauthentication",
        "--password-store=basic",
        "--use-mock-keychain"
    ]
    
    if os.getenv("CI", "").lower() == "true":
        common_args.extend([
            "--headless",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--window-size=1920,1080"
        ])
    
    if browser_type == "chrome":
        options = Options()
    else:
        options = EdgeOptions()
    
    for arg in common_args:
        options.add_argument(arg)
    
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option("useAutomationExtension", False)
    
    return options, user_data_dir


@pytest.fixture(scope="class")
def setup(request, browser):
    """
    Class-scoped fixture - one browser per test class.
    Enables parallel execution at class level with pytest-xdist.
    """
    user_data_dir = None
    
    if browser == "chrome":
        options, user_data_dir = get_browser_options("chrome")
        driver = webdriver.Chrome(options=options)
    elif browser == "edge":
        options, user_data_dir = get_browser_options("edge")
        driver = webdriver.Edge(options=options)
    else:
        driver = webdriver.Chrome()
    
    driver.maximize_window()
    driver.implicitly_wait(20)
    
    request.cls.driver = driver
    
    yield driver
    
    driver.quit()
    if user_data_dir:
        shutil.rmtree(user_data_dir, ignore_errors=True)


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
