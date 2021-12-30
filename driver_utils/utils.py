'''
General utils for the driver
'''

from typing import List
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement

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


def get_all_elements_of_web_element(element: WebElement) -> List[WebElement]:
    """Gets an array of all subelements of the webelement

    Args:
        element (WebElement): Parent webelement

    Returns:
        List[WebElement]: Array of child webElements
    """
    return element.find_elements(By.XPATH, './*')


def filter_perf_logs(logs, url):
    result = []
    for log in logs:
        if log_filter(log, url):
            result.append(log)
    return result

# Filter for logs
def log_filter(log, url):
    return (
        log["method"] == "Network.responseReceived" and
        log["params"]["response"]["url"] == url
        and "json" in log["params"]["response"]["mimeType"]
    )
