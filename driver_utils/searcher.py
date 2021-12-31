"""
Functions for the search page
"""
import time
import json
from typing import Dict, List
from selenium import webdriver
from CONFIG import LOCATION
from CONSTANTS import GET_AVAILABLE_APPOINTMENTS
from driver_utils.utils import filter_perf_logs, get_all_elements_of_web_element, wait_for_page_to_load, log_filter
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

'''Class selectors'''
ICBC_LOCATION_RESULTS_CLASS = "results-title"
ICBC_LOCATION_TITLE_CLASS = "location-title"
ICBC_LOCATION_DEPARTMENT_NAME_CLASS = "department-title"

'''ID SELECTORS'''
LOCATION_FIELD_ID = "mat-input-3"
AUTOCOMPLETE_BOX_ID = "mat-autocomplete-0"

'''ATTRIBUTE SELECTORS'''
LOCATION_SELECTOR = "id=\"mat-input-3\""

'''CSS SELECTORS'''
SEARCH_BUTTON_CSS_SELECTOR = ".mat-raised-button.mat-button-base.mat-accent.search-button"
ICBC_LOCATION_RESULTS_CSS_SELECTOR = ".results-title.ng-star-inserted"
ICBC_LOCATION_RESULTS_PAGE_BACK_BUTTON_CSS_SELECTOR = ".mat-stroked-button.mat-button-base.mat-accent.ng-star-inserted"

def search_for_bookings(driver: webdriver.Chrome):
    """Searches for bookings based on config

    Args:
        driver (webdriver.Chrome): Webdriver
    """
    
    # Wait for the page to load
    wait_for_page_to_load(driver, By.ID, LOCATION_FIELD_ID)

    # Enter location into the form
    location_field = driver.find_element_by_xpath(f"//input[@{LOCATION_SELECTOR}]")
    location_field.send_keys(LOCATION)
    
    # Have to manually add delay and some inputs to display autocomplete box
    time.sleep(1)
    location_field.click()
    location_field.send_keys(Keys.SPACE)
    location_field.send_keys(Keys.BACK_SPACE)
    
    # Get autocomplete box
    autocomplete: WebElement = driver.find_element_by_id(AUTOCOMPLETE_BOX_ID)
    
    # Grab autocomplete results and click on the first one
    time.sleep(1)
    autocomplete_results = get_all_elements_of_web_element(autocomplete)
    if len(autocomplete_results) == 0:
        raise Exception(f"No location found for: {LOCATION}")
    autocomplete_results[0].click()
    
    # Click the search button
    driver.find_element_by_css_selector(SEARCH_BUTTON_CSS_SELECTOR).click()



def parse_icbc_locations_results(driver: webdriver.Chrome) -> Dict[str, WebElement]:
    """Searches for bookings based on config

    Args:
        driver (webdriver.Chrome): Webdriver

    Returns:
        List[WebElement]: List of possible locations for ICBC testing centers
    """
    
    # Wait for page to load
    wait_for_page_to_load(driver, By.CLASS_NAME, ICBC_LOCATION_RESULTS_CLASS)
    
    # Parse ICBC location results page
    results: WebElement = driver.find_element_by_css_selector(ICBC_LOCATION_RESULTS_CSS_SELECTOR)
    results_arr = get_all_elements_of_web_element(results)
    
    # Throw away the first element
    results_arr = results_arr[1:]
    
    # Convert to dictionary with key of location name and webelement values
    results_dict = {}
    for web_element in results_arr:
        key = web_element.find_element(By.CLASS_NAME, ICBC_LOCATION_DEPARTMENT_NAME_CLASS).text
        results_dict[key] = web_element
    
    return results_dict
    

def get_icbc_location_availability(driver: webdriver.Chrome, element: WebElement) -> List[Dict]:
    """Get ICBC location availability

    Args:
        driver (webdriver.Chrome): Chrome web driver
        element (WebElement): Clickable element that brings driver to availability page

    Returns:
        List[Dict]: List of availability objects
    """
    
    # Click on the location and wait for XHR response
    element.click()
    time.sleep(3)
    
    # Get the XHR response
    logs_raw = driver.get_log("performance")
    logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
    
    # Filter for the endpoint we are querying for
    log = filter_perf_logs(logs, GET_AVAILABLE_APPOINTMENTS)[0]
    response_body = driver.execute_cdp_cmd(
        "Network.getResponseBody", {"requestId": log["params"]["requestId"]}
    )
    
    # Return the body which contains availabilities
    return json.loads(response_body['body'])


def click_back_to_location_results_page(driver: webdriver.Chrome):
    """Clicks the back button on the ICBC results page

    Args:
        driver (webdriver.Chrome): Chrome web driver
    """
    driver.find_element_by_css_selector(ICBC_LOCATION_RESULTS_PAGE_BACK_BUTTON_CSS_SELECTOR).click()