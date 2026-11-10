from pages.google_page import GooglePage
import pytest
from utils.json_reader import JsonReader
from utils.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize logger for test module
log = Logger.get_logger(__name__)
json_data = JsonReader.read_json("test_data.json")
SEARCH_DATA = json_data.get("search_queries", [])


@pytest.mark.parametrize("data", SEARCH_DATA)
def test_google_search(driver, data):
    search_keyword = data["search_keyword"]
    expected_title = data["expected_title"]

    log.info(f"Starting test_google_search with keyword: '{search_keyword}'")
    #Initialize Google page Object
    google_page = GooglePage(driver)

    # Open Google Url
    google_page.open_url("https://www.google.com")
    
    google_page.search(search_keyword)
    log.info(f"Successfully performed search for: '{search_keyword}'")
    
    # Robust Explicit Wait: Wait until the page title contains the expected keyword (up to 10 seconds)
    try:
        WebDriverWait(driver, 10).until(
            EC.title_contains(search_keyword)
        )
    except Exception as e:
        log.warning(f"Title did not update in time for keyword '{search_keyword}'. Current title: '{driver.title}'")

    # Final Assertion
    assert expected_title in driver.title, f"Expected '{expected_title}' in title, but got '{driver.title}'"
    log.info(f"Test passed successfully for query: '{search_keyword}'")

