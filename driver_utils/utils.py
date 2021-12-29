'''
General utils for the driver
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def wait_for_page_to_load(driver: webdriver.Chrome, by: By, selector: str, delay: int = 3):
    """Waits for page to load

    Args:
        driver (webdriver.Chrome): Driver
        ele_id (str): Element ID as a string
        delay (int): Delay to wait for before raising Exception. Default of 3 seconds

    """
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((by, selector)))
    except TimeoutException:
        raise TimeoutException(f"Could not load page in time for delay: {delay}")
