from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class GooglePage(BasePage):
    SEARCH_INPUT = (By.NAME, "q")
    COOKIE_ACCEPT_BTN = (By.ID, "L2AGLb")  # Google's "Accept all" button    Google's "Accept all" button ID in many regions
    def __init__(self, driver):
        super().__init__(driver)  # Initialize BasePage
    def open_google(self, url):
        self.driver.get(url)
        self.accept_cookies()  # Automatically handle cookie popup when opening
        # Handle Google Cookie popup if it appears
    def accept_cookies(self):
        """Safely click the cookie accept button if it appears"""
        try:
            self.click(self.COOKIE_ACCEPT_BTN)
        except Exception:
            # If cookie popup doesn't appear in some regions, safely ignore
            pass

def search_for(self, query):
        # Using BasePage's robust type_text method
        self.type_text(self.SEARCH_INPUT, query)
        self.driver.find_element(*self.SEARCH_INPUT).submit()