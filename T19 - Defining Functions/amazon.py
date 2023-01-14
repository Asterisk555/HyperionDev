# For each line in input.txt, compute each line of numbers differently depending on the operation at the start of each line.

contents = ""
temp_list = []
temp_list_operation = []
temp_list_numbers = []
temp_int = 0

import statistics  # Will be used to calculate average of a list of numbers.

with open('input.txt', 'r+', encoding='utf-8-sig') as f:
        for line in f:
            temp_list = line.split(':')  # Split operations from the list of numbers
            temp_list_operation = temp_list[0]
            # Prevent errors due to variations on how operations are capitalised.
            temp_list_operation = temp_list_operation.lower()
            temp_list_numbers = temp_list[1]
            temp_list_numbers = temp_list_numbers.split(',')
            # change list of strings to list of integers so mathematics operations can be applied.
            temp_list_numbers = list(map(int, temp_list_numbers))
            if "min" in temp_list_operation:
                temp_int = min(temp_list_numbers)
                contents = contents + f"The min of {temp_list_numbers} is {temp_int}.\n"
            if "max" in temp_list_operation:
                temp_int = max(temp_list_numbers)
                contents = contents + f"The max of {temp_list_numbers} is {temp_int}.\n"
            if "avg" in temp_list_operation:
                temp_int = round(statistics.mean(temp_list_numbers), 2)
                contents = contents + f"The mean of {temp_list_numbers} is {temp_int}.\n"
        # Backspace twice, to delete the last \n after every line has been processed.
        contents = contents[:-2]

# Write each answer on a new line in output.txt
with open('output.txt', 'w') as ofile:
    ofile.write(contents)