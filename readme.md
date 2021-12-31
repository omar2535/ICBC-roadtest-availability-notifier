# ICBC roadtest booker

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white)

## What does this do

This program is an automatic booker for ICBC road examinations. Due to road examinations getting booked up extremely quickly, this program assists people in finding those empty slots that are opened up from time to time.

## Features

- [x] Able to login automatically to your ICBC account
- [x] Able to specify a region and ICBC location to check for openings
- [x] Able to send an email notification when a preferred slot is open
- [ ] Able to check bookings when user already has a booking

## CONFIG

A configuration file must exist for this program to work. Follow the simple commands:

```sh
touch CONFIG.py
```

and add a configuration similar to the one provided below:

```py
'''GLOBAL CONFIGURATION FILE'''
DEBUG = False

'''For credentials'''

DRIVERS_LAST_NAME = "Asdf"
LICENCE_NUMBER = "1234567"
KEYWORD = "Google"

'''For preferences'''

# The location that you are searching for ICBC testing centers
LOCATION = "Vancouver, BC"

# The ICBC center name that you want to make a booking with
# Has to be an exact match to the name that the website shows
ICBC_CENTER = "Vancouver driver licensing (Point Grey)"

# Preferred days of the week that you can do your test on
PREFERRED_DAYS = ["Monday", "Wednesday", "Friday"]

# Preferred times as a tuple
PREFERRED_TIMES = [('09:00', '11:00'), ('12:00', '17:00')]

# Preferred before what date
PREFERRED_BEFORE_DATE = '2022-12-31'

'''For email notification'''

# FOLLOW THE GUIDE HERE TO SETUP A GMAIL ACC: https://towardsdatascience.com/e-mails-notification-bot-with-python-4efa227278fb

#Email Account
email_sender_account = "<GMAIL_ADDRESS>"
email_sender_username = "<GMAIL_ADDRESS>"
email_sender_password = <PASSWORD>
email_smtp_server = "smtp.gmail.com" # "<SMTP, eg smtp.gmail.com for gmail>"
email_smtp_port = 587 # <SMTP Porf, eg 587 for gmail>

#Email Content
email_recepients = ["<EMAIL #1>","<EMAIL #2>"]
email_subject = "Found available ICBC road test bookings matching preferences!"
```

## Setup

**Linux:**

```sh
python3 -m venv .env
source .env/bin/activate

pip install -r requirements.txt
```

**Windows:**

```sh
python3 -m venv .env
.env\Scripts\activate.bat

pip install -r requirements.txt
```

## Running the program

```sh
python main.py
```
