from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Locators definition
        self.search_box = (By.NAME, "q")
        self.cookie_accept_btn = (By.ID, "L2AGLb") # Google's "Accept all" button ID in many regions

    def open_url(self, url):
        self.driver.get(url)
        # Handle Google Cookie popup if it appears
        try:
            wait = WebDriverWait(self.driver, 3)
            accept_btn = wait.until(EC.element_to_be_clickable(self.cookie_accept_btn))
            accept_btn.click()
        except TimeoutException:
            # If no cookie popup appears, continue normally
            pass

    def search_item(self, query):
        #Explicit Wait: Wait until the search box is ready and clickable
        wait = WebDriverWait(self.driver, 10)
        # Find search box and perform search action
        search_element = wait.until(EC.element_to_be_clickable(self.search_box))

        # Perform search action
        search_element.send_keys(query)
        search_element.send_keys(Keys.RETURN)