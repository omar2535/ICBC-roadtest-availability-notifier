# ICBC roadtest booker

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white)

## What does this do

This program is an automatic booker for ICBC road examinations. Due to road examinations getting booked up extremely quickly, this program assists people in finding those empty slots that are opened up from time to time.

## Features

- [x] Able to login automatically to your ICBC account
- [ ] Able to specify a region and ICBC location to check for openings
- [ ] Able to automatically book the slot for you
- [ ] Able to send a notification when a slot is open

## CONFIG

A configuration file must exist for this program to work. Follow the simple commands:

```sh
touch CONFIG.py
```

and add a configuration similar to the one provided below:

```py
DRIVERS_LAST_NAME = "<LAST_NAME>"
LICENCE_NUMBER = "<LICENSE_NUMBER>"
KEYWORD = "<KEYWORD>"
CONFIG = {
    "location": "<LOCATION>"
}
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
