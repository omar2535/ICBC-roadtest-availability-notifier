from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
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
    
    # Setup logging preferences to access XHR
    # https://gist.github.com/lorey/079c5e178c9c9d3c30ad87df7f70491d
    capabilities = DesiredCapabilities.CHROME
    capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}

    # Setup options for headless chrome
    options = Options()
    options.headless = not DEBUG

    # Start the chrome driver
    return webdriver.Chrome(desired_capabilities=capabilities, options=options, service=s)
