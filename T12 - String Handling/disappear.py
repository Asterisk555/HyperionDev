# Asks user to input a string.
# Lets users request which characters they would like to remove.
# Prints the result.

test_string = str(input("Type the sentence you wish to remove characters from: "))
remove_string = str(input("Characters to remove: "))

# Change both strings to lists so they work with character removal methods.
test_list = list(test_string)
remove_list = list(remove_string)

test_list = [i for i in test_list if i not in remove_list]

print(''.join(test_list))  # Join the list so it's more legible when printed.