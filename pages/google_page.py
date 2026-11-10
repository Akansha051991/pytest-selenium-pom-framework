from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.logger import Logger


  
class GooglePage(BasePage):
    # Class-level logger so self.log works seamlessly
    log = Logger.get_logger(__name__)

    SEARCH_INPUT = (By.NAME, "q")
    COOKIE_ACCEPT_BTN = (By.ID, "L2AGLb")  # Google's "Accept all" button    Google's "Accept all" button ID in many regions
    def __init__(self, driver):
        super().__init__(driver)  # Initialize BasePage

    def accept_cookies(self):
        """Safely click the cookie accept button if it appears"""
        try:
            self.click(self.COOKIE_ACCEPT_BTN)
            self.log.info("Cookie banner accepted successfully.")
        except Exception:
            # If cookie popup doesn't appear in some regions, safely ignore
            pass

    def search(self, query):
        self.accept_cookies()
        self.log.info(f"Typing search query: '{query}'")
        """Type query into search box and press Enter"""
        self.type_text(self.SEARCH_INPUT, query)
       # Send RETURN key to submit search
        search_element = self.find_element(self.SEARCH_INPUT)
        search_element.send_keys(Keys.RETURN)