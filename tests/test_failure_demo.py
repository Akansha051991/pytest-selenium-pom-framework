import allure
import pytest

import allure
import pytest

@allure.feature("Error Handling & Validation")
@allure.story("Intentional Failure to Verify Screenshot Attachment")
def test_intentional_failure_and_screenshot(driver):
    # Browser ko Google par le jayenge taaki ek real webpage ka screenshot capture ho sake
    
    
    with allure.step("Opening Google home page"):
        driver.get("https://www.google.com")
    
    with allure.step("Verifying page title with an incorrect expected value"):
        # Yeh assertion jaan boojh kar fail karwayegi taaki test fail ho aur conftest hook trigger ho
        assert "NonExistentPageTitle12345" in driver.title, "Title mismatch: Intentionally failed to test Allure screenshot attachment!"