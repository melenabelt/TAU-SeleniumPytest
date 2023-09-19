"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo result page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoResultPage:

    # Locators

    SEARCH_INPUT = (By.ID, "search_form_input")
    RESULT_LINKS = (By.CSS_SELECTOR, "a[data-testid='result-title-a']")
    RESULT_MORE_RESULTS_BUTTON = (By.ID, "more-results")
    RESULT_MORE_RESULTS_DIV = (By.XPATH, "//div[@arial-label='Page 2']")
    RESULT_IMAGES_LINK = (By.CSS_SELECTOR, ".js-zci-link--images")
    RESULT_IMAGE_TITLES = (By.CSS_SELECTOR, ".tile--img__sub > span.tile--img__title")
    

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles
    
    def result_links(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        return links
    
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value
    
    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
    
    def title(self):
        return self.browser.title
    
    def search_images(self):
        result_images_button = self.browser.find_element(*self.RESULT_IMAGES_LINK)
        result_images_button.click()
    
    def result_images_title(self):
        result_image_title = self.browser.find_element(*self.RESULT_IMAGE_TITLES)
        return result_image_title.text
    
    def result_more_results_button(self):
        result_more_results_button = self.browser.find_element(*self.RESULT_MORE_RESULTS_BUTTON)
        return result_more_results_button
    
    def result_more_results_div(self):
        result_more_results_div = self.browser.find_element(*self.RESULT_MORE_RESULTS_DIV)
        return result_more_results_div
    

