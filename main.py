from driver_utils.login import perform_login
from driver_utils.startup import startup

# Start-up the chrome driver
driver = startup()

# Perform login
perform_login(driver)
