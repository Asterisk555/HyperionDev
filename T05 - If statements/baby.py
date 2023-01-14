user_birthyear = int(input("Year of birth?\n"))

from datetime import date
current_year = date.today().year

if current_year - user_birthyear >= 18:
    print("You're old enough. Time to party!")
else:
    print("Does your mother know where you are.")