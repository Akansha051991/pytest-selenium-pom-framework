import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    # Chrome options config for anti-bot detection & window setup
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    
    # Teardown: Close browser safely after test completion
    driver.quit()

# Pytest Hook to capture screenshot automatically on test failure and save locally
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):  # pyright: ignore[reportUnusedParameter]
    outcome = yield
    rep = outcome.get_result()
    
    # Check if the test failed during the execution phase ("call")
    if rep.when == "call" and rep.failed:
        # Get the driver instance from the fixture arguments
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture:
            # Unique timestamp ke sath clean filename generate karein
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"failure_{item.name}_{timestamp}.png"
            
            # Direct project folder me screenshot save karein
            driver_fixture.save_screenshot(screenshot_name)
            print(f"\n[INFO] Test failed! Screenshot saved locally as: {screenshot_name}")