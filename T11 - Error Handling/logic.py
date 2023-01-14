# Program to show a logical error.

user_num = int(input("Please type a whole number and hit enter: "))

print("Your number is divisible by 2 and 5?")
if (user_num % 2 == 0) and (user_num % 3 == 0):
    print("True")
else:
    print("False")

print("Your number is divisible by 2 or 5?")
if (user_num % 2 == 0) or (user_num % 5 == 0):
    print("True")
else:
    print("False")