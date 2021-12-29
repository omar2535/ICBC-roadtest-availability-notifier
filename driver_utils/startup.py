from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from CONSTANTS import DEBUG

def startup() -> webdriver.Chrome:
    """Starts up chrome web driver

    Returns:
        webdriver.Chrome: chrome web driver
    """
    # Install chrome drivers
    s = Service(ChromeDriverManager().install())

    # Setup options for headless chrome
    options = Options()
    options.headless = not DEBUG

    # Start the chrome driver
    return webdriver.Chrome(options=options, service=s)
