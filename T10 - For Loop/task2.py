# Checks which years are leap years within a range.

year = int(input("What is the earliest year you want to check is a leap year? "))
year_range = int(input("How many years forward would you like to check? "))

for year in range (year, year + year_range):
    if year % 4:
        print(str(year) + " isn't a leap year")
    else:
        print(str(year) + " is a leap year")