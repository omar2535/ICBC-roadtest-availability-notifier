"""
Performs login for the user
"""
import time
from selenium import webdriver
from CONSTANTS import BOOK_A_ROAD_TEST_HOME
from CREDENTIALS import DRIVERS_LAST_NAME, KEYWORD, LICENCE_NUMBER

'''CSS SELECTORS'''
NEXT_BUTTON_CSS_SELECTOR = ".mat-raised-button.mat-button-base.mat-accent"
SIGN_IN_BUTTON_CSS_SELECTOR = ".mat-raised-button.mat-button-base.mat-accent"
AGREE_TO_TERMS_CHECMKARK_CSS_SELECTOR = ".mat-checkbox-inner-container"

'''ATTRIBUTE SELECTORS'''
DRIVER_NAME_INPUT_ATTRIBUTE = "aria-label=\"driver-name\""
DRIVER_LICENCE_INPUT_ATTRIBUTE = "aria-label=\"driver-licence\""
KEYWORD_INPUT_ATTRIBUTE = "aria-label=\"keyword\""

'''FUNCTIONS'''
def perform_login(driver: webdriver.Chrome):
    """Performs login on the current webpage with the driver

    Args:
        driver (webdriver): webdriver to perform login on
    """
    # Get the main page to login
    driver.get(BOOK_A_ROAD_TEST_HOME)
    time.sleep(1)
    
    # Click the next button on home page to be brought to login form
    driver.find_element_by_css_selector(NEXT_BUTTON_CSS_SELECTOR).click()
    time.sleep(1)
    
    # Enter login credentials
    name_field = driver.find_element_by_xpath(f"//input[@{DRIVER_NAME_INPUT_ATTRIBUTE}]")
    licence_field = driver.find_element_by_xpath(f"//input[@{DRIVER_LICENCE_INPUT_ATTRIBUTE}]")
    keyword_field = driver.find_element_by_xpath(f"//input[@{KEYWORD_INPUT_ATTRIBUTE}]")
    
    name_field.send_keys(DRIVERS_LAST_NAME)
    licence_field.send_keys(LICENCE_NUMBER)
    keyword_field.send_keys(KEYWORD)
    time.sleep(1)
    
    # Check the agree to terms checkbox
    driver.find_element_by_css_selector(AGREE_TO_TERMS_CHECMKARK_CSS_SELECTOR).click()
    time.sleep(1)

    # Click sign in
    driver.find_element_by_css_selector(SIGN_IN_BUTTON_CSS_SELECTOR).click()
    time.sleep(1)
