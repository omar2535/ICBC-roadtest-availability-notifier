import time
from driver_utils.searcher import search_for_bookings
from driver_utils.login import perform_login
from driver_utils.startup import startup
from CONSTANTS import BOOK_A_ROAD_TEST_HOME

# Start-up the chrome driver
driver = startup()

# Get the main page to login
driver.get(BOOK_A_ROAD_TEST_HOME)

# Perform login
perform_login(driver)

# Wait a bit
time.sleep(1)

# Search for bookings
search_for_bookings(driver)
