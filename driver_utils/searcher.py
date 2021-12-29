"""
Functions for the booking page
"""
import time
from selenium import webdriver
from CONFIG import CONFIG
from driver_utils.utils import wait_for_page_to_load
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

'''ID SELECTORS'''
LOCATION_FIELD_ID = "mat-input-3"
AUTOCOMPLETE_BOX_ID = "mat-autocomplete-0"

'''ATTRIBUTE SELECTORS'''
LOCATION_SELECTOR = "id=\"mat-input-3\""

'''CSS SELECTORS'''
SEARCH_BUTTON_CSS_SELECTOR = ".mat-raised-button.mat-button-base.mat-accent.search-button"

def search_for_bookings(driver: webdriver.Chrome):
    """Searches for bookings based on config

    Args:
        driver (webdriver.Chrome): [description]
    """
    
    # Wait for the page to load
    wait_for_page_to_load(driver, By.ID, LOCATION_FIELD_ID)

    # Enter location into the form
    location_field = driver.find_element_by_xpath(f"//input[@{LOCATION_SELECTOR}]")
    location_field.send_keys(CONFIG["location"])
    
    # Have to manually add delay and some inputs to display autocomplete box
    time.sleep(1)
    location_field.click()
    location_field.send_keys(Keys.SPACE)
    location_field.send_keys(Keys.BACK_SPACE)
    
    # Get autocomplete box
    autocomplete: WebElement = driver.find_element_by_id(AUTOCOMPLETE_BOX_ID)
    
    # Grab autocomplete results and click on the first one
    time.sleep(1)
    autocomplete_results = autocomplete.find_elements(By.XPATH, './*')
    if len(autocomplete_results) == 0:
        raise Exception(f"No location found for: {CONFIG['location']}")
    autocomplete_results[0].click()
    
    # Click the search button
    driver.find_element_by_css_selector(SEARCH_BUTTON_CSS_SELECTOR).click()

    
    # TODO: Need to take config and click on the ICBC location user wants
    breakpoint()
