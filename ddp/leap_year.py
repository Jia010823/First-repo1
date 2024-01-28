"""
Leap Year Checker Function

Objective:
Write a function named 'is_leap_year' to determine whether a given year is a leap year.

Function Parameter:
year (integer): The year to be checked.

Instructions:
- The function should return 'True' if the 'year' is a leap year and 'False' otherwise.
- A year is a leap year if it is divisible by 4, except for end-of-century years, which must be divisible by 400.
- Use conditional statements to implement the leap year check.

Example Test Cases:
1. is_leap_year(2020) should return 'True'.
2. is_leap_year(1900) should return 'False'.
3. is_leap_year(2000) should return 'True'.
4. is_leap_year(2019) should return 'False'.
"""

def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If it's a century year, check if it's divisible by 400
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

# Example Test Cases
print(is_leap_year(2020)) # True, as 2020 is a leap year
print(is_leap_year(1900)) # False, as 1900 is not a leap year (century years need to be divisible by 400)
print(is_leap_year(2000)) # True, as 2000 is a leap year (it's divisible by 400)
print(is_leap_year(2019)) # False, as 2019 is not a leap year

