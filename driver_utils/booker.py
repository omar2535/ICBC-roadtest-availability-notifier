"""
Functions for the booking page
"""
import time
from selenium import webdriver
from CONFIG import CONFIG
from driver_utils.utils import get_all_elements_of_web_element, wait_for_page_to_load
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

