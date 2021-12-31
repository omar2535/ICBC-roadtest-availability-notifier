'''Notifies user when there's an available spot'''

from typing import Dict, List
from CONFIG import PREFERRED_BEFORE_DATE, PREFERRED_DAYS, PREFERRED_TIMES
from datetime import datetime

'''Constants'''
DATE_FORMATTER = '%Y-%m-%d'
DATE_AND_TIME_FORMATTER = '%Y-%m-%d %H:%M'

def check_available_dates_matches_config(availability) -> List[Dict]:
    appointments_matching_preferences = []
    for appointment in availability:
        if does_appointment_match_preferences(appointment):
            appointments_matching_preferences.append(appointment)
    return appointments_matching_preferences
        

# Sample object:
# {'appointmentDt': {'dayOfWeek': 'Friday', 'date': '2022-01-07'},
# 'startTm': '14:50', 'endTm': '15:35', 'posId': 275, 'resourceId': 16369,
# 'dlExam': {'code': '5-R-1', 'description': '5-R-ROAD'},
# 'lemgMsgId': 35}
def does_appointment_match_preferences(appointment: Dict) -> bool:
    """Checks if the appointment matches the preference from the config

    Args:
        appointment (Dict): Appointment object

    Returns:
        bool: True if appointment matches preference, false otherwise
    """
    
    day_of_week = appointment['appointmentDt']['dayOfWeek']
    date = appointment['appointmentDt']['date']
    start_time = appointment['startTm']
    end_time = appointment['endTm']
    
    return (check_day_of_week_in_preferences(day_of_week) and
            check_date_in_preferences(date) and 
            check_start_and_end_time_in_preferences(date, start_time, end_time))



# check if day of week in preferred days
def check_day_of_week_in_preferences(day_of_week: str) -> bool:
    for day in PREFERRED_DAYS:
        if day.lower() == day_of_week.lower():
            return True
    return False

def check_date_in_preferences(date: str) -> bool:
    available_date = datetime.strptime(date, DATE_FORMATTER)
    preferred_date = datetime.strptime(PREFERRED_BEFORE_DATE, DATE_FORMATTER)
    return available_date < preferred_date

def check_start_and_end_time_in_preferences(date: str, start_time: str, end_time: str) -> bool:
    start_time_date = datetime.strptime(f"{date} {start_time}", DATE_AND_TIME_FORMATTER)
    end_time_date = datetime.strptime(f"{date} {end_time}", DATE_AND_TIME_FORMATTER)
    
    for time_preference in PREFERRED_TIMES:
        preferred_start_time_date = datetime.strptime(f"{date} {time_preference[0]}", DATE_AND_TIME_FORMATTER)
        preferred_end_time_date = datetime.strptime(f"{date} {time_preference[1]}", DATE_AND_TIME_FORMATTER)
        if start_time_date >= preferred_start_time_date and end_time_date <= preferred_end_time_date:
            return True
    return False
