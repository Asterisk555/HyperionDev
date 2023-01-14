# Ask user to input a number, and return all even numbers between the integer and 0

num = int(input("Please enter a positive whole number: "))
for i in range (0, num + 1):  # num + 1 so the number itself isn't missed
	if i % 2 == 0:
		print(i)