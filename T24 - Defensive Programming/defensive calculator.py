# Give the user the option to either enter two numbers and an operator,
# display the answer to the equation,
# and return a calculation that is written to a text file, 
# or read all of the equations from the text file and
# print out all of the equations together with the results.
# Use defensive programming to write this program in a manner that is robust and
# handles unexpected events and user inputs.
# Ensure that the program does not crash if a file does not exist,
# and that the user is prompted again to enter the name of the file.

import os

# Class that handles parsing of equations
class EquationParser:
    def __init__(self):
        # Dictionary mapping text operators to functions that handle those operators
        self.operators = {"+":self.add, "-":self.sub, "*":self.mult, "/":self.div}  # Dictionary of operators
    
    # Functions for each operator, names are self explanatory.

    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mult(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a / b

    # Error checking
    # This function returns True if the given character is a supported operator
    def is_operator(self, operator):
        return True if self.operators.get(operator) else False

    # Casting so variables are treated as numbers not strings, and calculations are done properly.
    def parse_number(self, number):
        if "." not in number:
            return int(number)
        else:
            return float(number)

    # Parses a given string equation, handling errors
    def parse(self, equation):
        equation_split = equation.split(" ")

        # Strip whitespace from both sides of every element
        equation_split = [x.strip() for x in equation_split]

        # If we don't have 3 parts, it's not a valid equation.
        if len(equation_split) != 3:
            print("Equations were in the wrong format! Each part of the equation needs to be separated by a space (e.g 4 * 2).")
            return None

        # Extract the 3 values for clarity
        x, op, y = equation_split
    
        # Checks if the equation follows x + y format.
        is_valid = x.isnumeric() and self.is_operator(op) and y.isnumeric()
        
        if not is_valid:
            print("Equations were in the wrong format! Equations needs to be two numbers and an operator (e.g 4 * 2).")
            return False

        x = self.parse_number(x)
        y = self.parse_number(y)

        # Get the operator function defined
        func = self.operators.get(op)

        return func(x, y)


parser = EquationParser()

print("Would you like to read a (f)ile for the equations, or (m)anually input one?")

# Will loop until the user picks either f (file) or m (manual) equation input, handles all erroneous input
while True:
    file_or_input = input("Choose f for file, m for manual: ")
    if "f" in file_or_input.lower() or "m" in file_or_input.lower():
        break
    else:
        print("Please enter a valid choice.")

if file_or_input.lower() == "m":
    # Let user input an equation they want the answer to
    while True:
        user_input = input("Equation: ")
        result = parser.parse(user_input)

        # If there is no result, i.e. None is returned, the equation isn't valid.
        if result:
            print(f"{user_input} = {result}")
            with open("calculation_results.txt", "a") as f:
                f.write(f"{user_input}\n")
            break
        else:
            print("Please enter a valid equation.")
else:
    while True:
        # Let a user input a file with a list of equations that all need answers
        filename = input("Enter filename (with equations): ")
        # If the file doesnt't exist, loop until they input a correct filename, and tell them the folder to add the file
        if not os.path.isfile(filename):
            temp_variable = os.getcwd()
            print(f"Not a valid file. Please check the file is in {temp_variable} and is a txt file. For example, 'equations.txt'")
        else:
            break
    
    with open(filename, "r") as f:
        equations = f.readlines()
    
    equations = [x.strip() for x in equations]
    
    for equation in equations:
        result = parser.parse(equation)
        print(f"{equation} = {result}")