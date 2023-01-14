# Inputs a sentence and then displays each word on a new line.

test_string = input("Type a sentence: ")
test_list = test_string.split()

print ("\n".join(test_list))