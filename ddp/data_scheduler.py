"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""

from datetime import datetime

def date_passed(todays_date, scheduled_date):
    # Function to convert date from '26th March' format to '26 March'
    def format_date(date_str):
        # Removing the suffixes 'st', 'nd', 'rd', 'th' from the day
        for suffix in ['st', 'nd', 'rd', 'th']:
            if suffix in date_str:
                date_str = date_str.replace(suffix, '')
                break
        return date_str

    # Formatting the dates
    todays_date_formatted = format_date(todays_date)
    scheduled_date_formatted = format_date(scheduled_date)

    # Converting strings to datetime objects
    today = datetime.strptime(todays_date_formatted, "%d %B")
    scheduled = datetime.strptime(scheduled_date_formatted, "%d %B")

    # Comparing the dates
    if today > scheduled:
        return "The scheduled date has passed."
    elif today < scheduled:
        return "The scheduled date is yet to pass."
    else:
        return "The scheduled date is today."

# Example Test Cases
print(date_passed('26th March', '25th March'))  # The scheduled date has passed.
print(date_passed('26th March', '26th March'))  # The scheduled date is today.
print(date_passed('26th March', '27th March'))  # The scheduled date is yet to pass.


