import os
import pytest
import tempfile
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    parser.addoption("--browsername", action="store", default="chrome")  # default set to chrome

@pytest.fixture(scope="function")
def browser(request):
    return request.config.getoption("--browsername")

@pytest.fixture(scope="function")
def setup(request, browser):
    """
    Function-scoped fixture that creates a browser instance for each test.
    This allows parallel test execution.
    """
    if browser == "chrome":
        options = Options()
        
        # Create a clean temporary profile directory
        user_data_dir = tempfile.mkdtemp(prefix="chrome_test_profile_")
        options.add_argument(f"--user-data-dir={user_data_dir}")
        
        # Aggressive password manager disabling
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "autofill.profile_enabled": False,
            "autofill.enabled": False,
            "profile.password_manager_leak_detection": False,
        }
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        options.add_experimental_option("useAutomationExtension", False)
        
        # Chrome arguments to disable password features
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-features=PasswordManager,PasswordManagerOnboarding")
        options.add_argument("--disable-password-manager-reauthentication")
        options.add_argument("--password-store=basic")
        options.add_argument("--use-mock-keychain")
        
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
        
        # Create a clean temporary profile directory
        user_data_dir = tempfile.mkdtemp(prefix="edge_test_profile_")
        options.add_argument(f"--user-data-dir={user_data_dir}")
        
        # Aggressive password manager disabling for Edge
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "autofill.profile_enabled": False,
            "autofill.enabled": False,
            "profile.password_manager_leak_detection": False,
        }
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        options.add_experimental_option("useAutomationExtension", False)
        
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-features=PasswordManager,PasswordManagerOnboarding")
        options.add_argument("--disable-password-manager-reauthentication")
        options.add_argument("--password-store=basic")
        options.add_argument("--use-mock-keychain")

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
    
    yield driver
    
    # Cleanup
    driver.quit()
    
    # Clean up temporary profile directory
    try:
        if 'user_data_dir' in locals():
            shutil.rmtree(user_data_dir, ignore_errors=True)
    except:
        pass


@pytest.fixture(autouse=True, scope="function")
def clear_state(request):
    """
    Clears browser state before each test to ensure clean state.
    Only runs if setup fixture is used in the test.
    """
    # Only clear state if the test used the setup fixture
    if 'setup' in request.fixturenames:
        driver = request.getfixturevalue('setup')
        try:
            driver.delete_all_cookies()
            driver.execute_script("window.localStorage.clear();")
            driver.execute_script("window.sessionStorage.clear();")
        except:
            pass
    
    yield


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


# @pytest.hookimpl(tryfirst=True)
# def pytest_html_report_title(report):
#     report.title = "My Test Report"


# @pytest.hookimpl(tryfirst=True)
# def pytest_html_results_summary(prefix):
#     prefix.append("<h2>My Custom Header</h2>")
