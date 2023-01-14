num_1 = int(input("Pick a number! Any number! As long as it's a whole number:"))
num_2 = int(input("Pick another number, please:"))
num_3 = int(input("Just one more number, but don't choose 0:"))

sum_num = str(num_1 + num_2 + num_3)
print("Sum of all numbers is " + sum_num )

subtract_num = str(num_1 - num_2)
print("First number minus the second is " + subtract_num)

multi_num = str(num_3 * num_1)
print("Third number multiplied by the first is " + multi_num)

sum_divi_num = str((num_1 + num_2 + num_3) / num_3)
print("Sum of numbers divided by the third is " + sum_divi_num )