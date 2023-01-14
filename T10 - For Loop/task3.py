# A showcase of different types of loops.

print ("Example of a while loop counting backwards.")

i = 20

while i > 0:
     print (i)
     i = i - 1

print ("Printing even numbers from 1-20.")

i = 20

for i in range (0, i+2):
	if i % 2 == 0:
		print (i)

print ("Asterisk chain loop")

stars = "*****"
for i in range(0 ,5):
    index = i + 1
    print (stars[0:index])

print ("Highest common denominator between two positive integers, where x = 24 and y = 60.")

import math

x = 24
y = 60

print (math.gcd(x, y))