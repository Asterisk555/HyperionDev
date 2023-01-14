# Create a function that prints all the days of the week.
# No need to put an argument in the () because we're just printing days, not doing anything with changing arguments, as a result no return either.
def print_days():
    print("Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday")

print_days()  # Running the print_days function here in order to test it does what it's supposed to.

# Create a function that takes in a sentence and replaces every second word with the word “Hello”
def interrupting_hello(sentence):
        # split string into a list, so alternate words can be targeted
        sentence_list = sentence.split(' ')
        sentence_alt = ""
        # loop that will apply different actions depending on the position of the word in the list
        for i in range (len(sentence_list)):
            if i % 2 != 0:
                sentence_alt += "Hello "
            else:
                sentence_alt += sentence_list[i] + ' '
        return print(sentence_alt)

# Running the function here in order to test it does what it's supposed to, and to show you need to use a string as the argument
interrupting_hello("Create a function that takes in a sentence and replaces every second word with the word Hello")