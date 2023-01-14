# Asks the user to guess the name 'John' and adds wrong guesses to a list.
# Similar to names.py in T09, but uses several more functions.

print("Guess what my name is!")

# Empty variables for use with name inputs.
name_input = "0"
name_list = []

while name_input != "John":
    name_input = input("Input name: ").capitalize()  # Capitalizes first letter of word to eliminate case sensitivity to input.
    name_list.append(name_input)  # Adds wrong guesses to list.

name_list.remove("John")  # John is not a wrong guess, so needs to be removed from the list of wrong names.

print("You guessed my name!")

if len(name_list) > 0:
    print("But you made a few wrong guesses:" + str(name_list))