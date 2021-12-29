"""
Performs login for the user
"""
from selenium import webdriver
from CONFIG import DRIVERS_LAST_NAME, KEYWORD, LICENCE_NUMBER
from driver_utils.utils import wait_for_page_to_load
from selenium.webdriver.common.by import By

'''ID SELECTORS'''
KEYWORD_FIELD_ID = "mat-input-7"

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
    
    # Wait for page to load
    wait_for_page_to_load(driver, By.CSS_SELECTOR, NEXT_BUTTON_CSS_SELECTOR)
    
    # Click the next button on home page to be brought to login form
    driver.find_element_by_css_selector(NEXT_BUTTON_CSS_SELECTOR).click()
    
    # Wait for page to load
    wait_for_page_to_load(driver, By.CSS_SELECTOR, SIGN_IN_BUTTON_CSS_SELECTOR)
    
    # Enter login credentials
    name_field = driver.find_element_by_xpath(f"//input[@{DRIVER_NAME_INPUT_ATTRIBUTE}]")
    licence_field = driver.find_element_by_xpath(f"//input[@{DRIVER_LICENCE_INPUT_ATTRIBUTE}]")
    keyword_field = driver.find_element_by_xpath(f"//input[@{KEYWORD_INPUT_ATTRIBUTE}]")
    
    name_field.send_keys(DRIVERS_LAST_NAME)
    licence_field.send_keys(LICENCE_NUMBER)
    keyword_field.send_keys(KEYWORD)
    
    # Check the agree to terms checkbox
    driver.find_element_by_css_selector(AGREE_TO_TERMS_CHECMKARK_CSS_SELECTOR).click()

    # Click sign in
    driver.find_element_by_css_selector(SIGN_IN_BUTTON_CSS_SELECTOR).click()
