from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Install chrome drivers
s=Service(ChromeDriverManager().install())

# Setup options for headless chrome
options = Options()
options.headless = True

# Start the chrome driver
driver = webdriver.Chrome(options=options, service=s)
driver.get('https://thaomar.com/')


breakpoint()
