# Calculates the average of numbers entered by a user, excluding -1.

usernumber = float(input("Please enter a number:")) 
usernumber_total = 0 
usernumber_attempts=0 
while usernumber != -1: 
  usernumber_total += usernumber 
  usernumber_attempts +=1 
  usernumber = float(input("Please try again:")) 
usernumber_avg = round(usernumber_total / usernumber_attempts,2) 
print("Oh no, negative one, my only weakness...") 
print("Average number input is " + str(usernumber_avg))