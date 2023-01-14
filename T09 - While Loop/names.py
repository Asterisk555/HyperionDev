# Counts the numbers of items entered in a list.

name_input = "0"
print("To stop the input loop type 'stop'")
name_list = []

while name_input != "stop":
    name_input = input("Input name: ")
    name_list.append(name_input)

name_list.remove("stop")

print("Thank you for inputting your student list. Your list contains " + str(len(name_list)) + " names.")