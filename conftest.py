import os
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    """Command-line options for running tests on different browsers and modes"""
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests: chrome, firefox, or edge")
    parser.addoption("--headless", action="store_true", default=False, help="Run tests in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    """Setup and teardown WebDriver with multi-browser and headless support"""
    browser_name = request.config.getoption("--browser").lower()
    is_headless = request.config.getoption("--headless")

    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        if is_headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if is_headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        if is_headless:
            options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)
    
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported.")

    driver.maximize_window()
    yield driver

    # Teardown & Failure Screenshot Hook (Properly aligned inside fixture)
    if request.node.rep_call.failed:
        os.makedirs("reports", exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"reports/failure_{request.node.name}_{timestamp}.png"
        driver.save_screenshot(screenshot_name)
        print(f"\n[INFO] Test failed! Screenshot saved as: {screenshot_name}")

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to catch test failures for screenshot capture"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)