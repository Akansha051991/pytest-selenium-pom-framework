import os
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from utils.config_reader import ConfigReader
from utils.logger import Logger
import allure

log = Logger.get_logger(__name__)

def pytest_addoption(parser):
    """Command-line options for running tests on different browsers and modes"""
    parser.addoption(
        "--browser",
        action="store",
        default=ConfigReader.get_browser(),
        help="Browser to run tests on: chrome, firefox, or edge"
    )
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="Run tests in headless mode: true or false"
    )


@pytest.fixture(scope="function")
def driver(request):
    """Setup and teardown WebDriver with ConfigReader & multi-browser and headless support"""
    cli_browser = request.config.getoption("--browser")
    browser_name = cli_browser.lower() if cli_browser else ConfigReader.get_browser().lower()
    cli_headless = request.config.getoption("--headless")
    # Properly evaluate headless option string to boolean
    if isinstance(cli_headless, str):
        is_headless = cli_headless.lower() in ("true", "yes", "1")
    else:
        is_headless = bool(cli_headless)

    log.info(f"--- STARTING TEST: Setting up {browser_name.capitalize()} Browser (Headless: {is_headless}) ---")

    driver_instance = None

    

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        if is_headless:
            options.add_argument("--headless=new")
        driver_instance = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if is_headless:
            options.add_argument("-headless")
        driver_instance = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        if is_headless:
            options.add_argument("--headless=new")
        driver_instance = webdriver.Edge(options=options)
    
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported.")

    driver_instance.maximize_window()
    base_url = ConfigReader.get_base_url()
    log.info(f"Navigating to Base URL: {base_url}")
    driver_instance.get(base_url)
    # Attach driver instance to request node for screenshot hook access
    request.node.driver = driver_instance
    yield driver_instance

    # Teardown: Always logs and quits the browser properly
    log.info(f"--- TEARDOWN: Closing {browser_name.capitalize()} Browser ---")
    driver_instance.quit()
        
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    """Injects clean, custom project metadata into the pytest-html report Environment table."""
    metadata['Project Name'] = 'Hybrid Automation Framework'
    metadata['Test Scope'] = 'UI & API Regression Suite'
    metadata['QA Engineer'] = 'Automation Team'
    metadata['Target Environment'] = 'QA / Staging'
    
    # Remove redundant/clutter default keys for a clean executive look
    metadata.pop('Packages', None)
    metadata.pop('Plugins', None)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Modern hook to capture test failures, save locally, and embed screenshot into pytest-html report"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    # Execute only when test fails during execution phase ("call")
    if rep.when == "call" and rep.failed:
        driver = getattr(item, "driver", None)
        if driver:
            try:
                os.makedirs("reports", exist_ok=True)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                # Clean invalid filename characters like brackets [] for local file system safety
                safe_item_name = item.name.replace("[", "_").replace("]", "").replace("::", "_")
                screenshot_name = f"reports/failure_{safe_item_name}_{timestamp}.png"
                
                # 1. Save locally as backup
                driver.save_screenshot(screenshot_name)
                print(f"\n[INFO] Test failed! Screenshot saved locally as: {screenshot_name}")
                log.error(f"Test failed: {item.name}. Screenshot saved to {screenshot_name}")

                # 2. Modern pytest-html v4 attachment format using item and extra
                import pytest_html
                screenshot_base64 = driver.get_screenshot_as_base64()
                
                # Attach to report extra
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_base64))
                rep.extra = extra
                
            # 3. NEW: Attach screenshot directly to Allure Report dashboard
                screenshot_png = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot_png,
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
                log.info("Failure screenshot successfully attached to Allure report.")
                
            except Exception as e:
                log.error(f"Failed to capture/attach failure screenshot: {e}")