from driver_utils.searcher import get_icbc_location_availability, parse_icbc_locations_results, search_for_bookings
from driver_utils.login import perform_login
from driver_utils.startup import startup
from CONSTANTS import BOOK_A_ROAD_TEST_HOME

# Start-up the chrome driver
driver = startup()

# Get the main page to login
driver.get(BOOK_A_ROAD_TEST_HOME)

# Perform login
perform_login(driver)

# Search for bookings
search_for_bookings(driver)

# Parse location results
location_results = parse_icbc_locations_results(driver)

# Check one of the location's availability
availabilty = get_icbc_location_availability(driver, location_results[1])

breakpoint()
