# Prints the times table for a user entered number.

i = int(input("Type a positive whole number to get the times table: "))

for x in range(1, 13):
    print('{} * {} = {}'.format(x, i, x * i))