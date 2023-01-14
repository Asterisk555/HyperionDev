num1 = 1
num2 = 2
num3 = 3

if num1 - num2 > 0:
    sort_1 = num1
    sort_2 = num2
    print(num1)
else:
    sort_1 = num2
    sort_2 = num1
    print(num2)

if num3 - sort_1 > 0:
    print(str(num3) + ", " + str(sort_1) + ", " + str(sort_2))
elif num3 - sort_2 > 0:
    print(str(sort_1) + ", " + str(num3) + ", " + str(sort_2))
else:
    print(str(sort_1) + ", " + str(sort_2) + ", " + str(num3))