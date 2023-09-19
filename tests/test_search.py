"""
These tests cover DuckDuckGo searches.
"""

import pytest
import random


from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from pages.result_detail import DuckDuckGoResultDetailPage

# The browser we're receiving as a parameter is the created fixture
@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  # PHRASE = 'panda'
  
  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for "panda"
  search_page.search(phrase).click()

  # Then the search result query is "panda"
  assert phrase == result_page.search_input_value()

  # And the search result links pertain to "panda"
  titles = result_page.result_link_titles()
  matches = [t for t in titles if phrase.lower() in t.lower()]
  assert len(matches) > 0

  # And the search result title constains "panda"
  assert phrase in result_page.title()

  # # TODO: Remove this exception once the test is complete
  # raise Exception("Incomplete Test")


@pytest.mark.parametrize('phrase', ['panda'])
def test_clic_search_result(browser, phrase):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  result_detail_page = DuckDuckGoResultDetailPage(browser)

  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for a phrase
  search_page.search(phrase).click()

  # And user clicks on any title result
  link_titles = result_page.result_links()
  rand_i = random.randint(0, len(link_titles) - 1)
  link_titles[rand_i].click()

  # Then the result detail page content constains the used phrase
  assert phrase in result_detail_page.get_result_detail_content()


@pytest.mark.parametrize('phrase', ['panda'])
def test_clic_more_results(browser, phrase):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)

  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for a phrase
  search_page.search(phrase).click()

  # And user clicks on More Results button
  result_page.result_more_results_button().click()

  # Then a new results div is shown
  result_page.result_more_results_div()
  

@pytest.mark.parametrize('phrase', ['python', 'panda'])
def test_search_autocomplete(browser, phrase):
  search_page = DuckDuckGoSearchPage(browser)
  
  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for a phrase
  search_page.search(phrase)

  # Then every word in autocomplete list contains that phrase
  autocomplete_phrases = search_page.search_autocomplete()
  assert [phrase.lower() in phr.text.lower() for phr in autocomplete_phrases]


@pytest.mark.parametrize('phrase', ['python'])
def test_search_phrase_from_result_page(browser, phrase):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)

  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for a phrase
  search_page.search("panda").click()

  # And the user search for a new phrase in result page
  result_page.search(phrase)

  # Then the search result links pertain to the phrase
  titles = result_page.result_link_titles()
  matches = [t for t in titles if phrase.lower() in t.lower()]
  assert len(matches) > 0


@pytest.mark.parametrize('phrase', ['python'])
def test_search_image(browser, phrase):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)

  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for images using a phrase
  search_page.search(phrase).click()
  result_page.search_images()

  # Then the search result image titles pertain to the phrase
  titles = result_page.result_images_title()
  matches = [t for t in titles if phrase.lower() in t.lower()]
  assert len(matches) > 0

