"""
Performs login for the user
"""

from selenium import webdriver
from CONSTANTS import BOOK_A_ROAD_TEST_HOME

# Constants
NEXT_BUTTON_CSS_SELECTOR = ".mat-raised-button.mat-button-base.mat-accent"

# Functions
def perform_login(driver: webdriver.Chrome):
    """Performs login on the current webpage with the driver

    Args:
        driver (webdriver): webdriver to perform login on
    """
    driver.get(BOOK_A_ROAD_TEST_HOME)
    
    # Click the next button
    driver.find_element_by_css_selector(NEXT_BUTTON_CSS_SELECTOR).click()
    
    # Enter driver's information
    breakpoint()
