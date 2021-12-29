"""
Functions for the booking page
"""

from selenium import webdriver
from CREDENTIALS import CONFIG
from driver_utils.utils import wait_for_page_to_load
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

'''ID SELECTORS'''
LOCATION_FIELD_ID = "mat-input-3"

'''ATTRIBUTE SELECTORS'''
LOCATION_SELECTOR = "id=\"mat-input-3\""

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
    location_field.send_keys(Keys.SPACE)
    
    
    breakpoint()
    