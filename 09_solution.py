#Leap Year Checker
#Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

leap_year = 1600

if (leap_year % 400 == 0) or (leap_year % 4 == 0 & leap_year % 100 != 0):
    print('its leap year')
else:
    print("its not")

