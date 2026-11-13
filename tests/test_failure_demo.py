import allure
import pytest

@pytest.mark.xfail(reason="Intentional failure to showcase automated failure screenshot capture and Allure integration")
@allure.feature("Error Handling & Validation")
@allure.story("Intentional Failure to Verify Screenshot Attachment")
def test_intentional_failure_and_screenshot(driver):
    # Navigate to Google to capture a real webpage screenshot on failure
    with allure.step("Opening Google home page"):
        driver.get("https://www.google.com")
    
    with allure.step("Verifying page title with an incorrect expected value"):
        # Intentionally failing assertion to trigger the conftest failure hook and screenshot capture
        assert "NonExistentPageTitle12345" in driver.title, "Title mismatch: Intentionally failed to test Allure screenshot attachment!"