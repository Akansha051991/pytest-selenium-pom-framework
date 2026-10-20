from pages.google_page import GooglePage
import pytest


# Test Data (Data-driven approach: inputs and expected titles separated from logic) for failed test
# FAILED_SEARCH_DATA = [
#     ("Python Selenium Pytest", "Python Selenium Pytest - Google Search"),
#     ("Automation Testing Framework", "Automation Testing Framework - Google Search"),


# ]

# Test Data (Data-driven approach: inputs and expected titles separated from logic) for passed test
# PASSED_SEARCH_DATA = [
#     ("Python Selenium Pytest", "Google"),
#     ("Automation Testing Framework", "Google"),


# ]

# Mix Test Data: Kuch pass honge, kuch intentionally fail honge (screenshot test karne ke liye)
SEARCH_DATA = [
    ("Python Selenium Pytest", "Google"),                      # Yeh PASS ho jayega
    ("Automation Testing Framework", "WrongTitle1234-Fail"),   # Yeh FAIL hoga aur screenshot capture karega
]

@pytest.mark.parametrize("search_keyword, expected_title", SEARCH_DATA)
def test_google_search(driver, search_keyword, expected_title):
    #Initialize Google page Object
    google_page = GooglePage(driver)

    # Open Google Url
    google_page.open_url("https://www.google.com")

    #Perform Search

    google_page.search_item(search_keyword)

    #Basic assertion to chrck if title contains expected keywords

    assert expected_title in driver.title

