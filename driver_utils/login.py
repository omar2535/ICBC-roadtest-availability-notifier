"""
Performs login for the user
"""

from selenium import webdriver
from CONSTANTS import BOOK_A_ROAD_TEST_HOME


def perform_login(driver: webdriver.Chrome):
    """Performs login on the current webpage with the driver

    Args:
        driver (webdriver): webdriver to perform login on
    """
    driver.get(BOOK_A_ROAD_TEST_HOME)
    breakpoint()
    pass