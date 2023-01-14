# import the math module because the task said to.
import math
# import the statistics module, since it has useful functions for this task.
import statistics

tenFloat_input = ""
tenFloat_list = []

# Write a program that starts by asking the user to input 10 floats.
while True:  # While loop will keep running until break, since there's no conditional. Other way to write it without the break would have been while len(tenFloat_list) < 10:
    if len(tenFloat_list) == 10:
        break
    tenFloat_input = float(input("Input a number with decimal points: "))
    tenFloat_list.append(tenFloat_input)

print("Find the total of all the numbers and print the result.")
tenFloat_sum = sum(tenFloat_list)
print(tenFloat_sum)

print("print the index of minimum and maximum values.")
print(tenFloat_list.index(min(tenFloat_list)))
print(tenFloat_list.index(max(tenFloat_list)))

print("Calculate the average of the numbers and round off to 2 decimal places. Print the result.")
print(round(statistics.mean(tenFloat_list), 2))
print("Find the median number and print the result.")
print(statistics.median(tenFloat_list))