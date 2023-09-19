"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:

    # URL
    URL = 'https://duckduckgo.com/'

    # Locators

    SEARCH_INPUT = (By.ID, 'searchbox_input')
    # Using Xpath
    SEARCH_BUTTON = (By.XPATH, '//button[@aria-label="Search"]')
    # Using CSS
    # SEARCH_BUTTON = (By.CSS, 'button[aria-label="Search"]')
    SEARCH_AUTOCOMPLETE_LIST = (By.ID, 'listbox--searchbox_homepage')


    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        # search_input.send_keys(phrase + Keys.RETURN)
        search_input.send_keys(phrase)
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        return search_button

    def search_autocomplete(self):
        search_autocomplete_list = self.browser.find_element(*self.SEARCH_AUTOCOMPLETE_LIST)
        search_autocomplete_list_items = search_autocomplete_list.find_elements(By.TAG_NAME, "li")
        return search_autocomplete_list_items
