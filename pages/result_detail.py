"""
This module contains DuckDuckGoResultDetailPage,
the page object for the DuckDuckGo result detail page.
"""

from selenium.webdriver.common.by import By

class DuckDuckGoResultDetailPage:

    # Locators

    
    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def get_result_detail_content(self):
        return self.browser.page_source

    

    