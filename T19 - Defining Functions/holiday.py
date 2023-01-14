# This function will take the number of nights a user will be staying at a hotel as an argument, and return a total cost for the hotel stay
def hotel_cost(nights):
    hotel_price = 56
    a = nights * hotel_price
    print(f"Hotel price will be £{a} at £{hotel_price} a night for {nights} nights.")
    return a

# This function will take the city you are flying to as an argument and return a cost for the flight.
def plane_cost(city):
    # Create a dictionary called londonDepartures, where the keys are the name of a city,
    # and the value for each key is the cost of flying there from London.
    londonDepartures = {
        'Barcelona': 127,
        'Stockholm': 134,
        'Ottawa': 209
        }
    b = londonDepartures[city]
    print(f"Return flights will cost £{b} from London to {city}.")
    return b

# This function will take the number of days the car will be hired for as an argument and return the total cost of the car rental.
def car_rental(days):
    car_price = 30
    c = days * car_price
    print(f"Renting a car will be £{c} at £{car_price} a day for {days} days.")
    return c

# This function will return a total cost for your holiday,
# and calculates this using the three previously created functions.
def holiday_cost(nights, city, days):
    d = hotel_cost(nights) + plane_cost(city) + car_rental(days)
    print(f"Total holiday cost is £{d}.")
    return d

# Print out all the details about the holiday in a user friendly way.
holiday_cost(7, 'Ottawa', 8)