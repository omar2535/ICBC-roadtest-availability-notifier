from CONFIG import ICBC_CENTER
from driver_utils.searcher import get_icbc_location_availability, parse_icbc_locations_results, search_for_bookings
from driver_utils.login import perform_login
from driver_utils.startup import startup
from CONSTANTS import BOOK_A_ROAD_TEST_HOME
from utils.availability_parser import check_available_dates_matches_config
from utils.notifier import notify_by_email

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
availability = get_icbc_location_availability(driver, location_results[ICBC_CENTER])

# Notifty user if there's availability matching preferences
matched_appointments = check_available_dates_matches_config(availability)

# If there are matched appointments, notify user
if len(matched_appointments) > 0:
    notify_by_email(matched_appointments)

breakpoint()
