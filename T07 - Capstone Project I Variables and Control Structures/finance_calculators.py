# Financial calculator program for investments and home loans.
# Requires user input at several points.
# Uses while loops and if statements.

import math

print("This program allows you to accesss our investment calculator, and home loan repayment calculator.\ninvestment - to calculate the amount of interest you'll earn on your investment\nbond - to calculate the amount you'll have to pay on a home loan")

while True:

    calculation_type = input("Enter either 'investment' or 'bond' to proceed: ")  # User selects which calculator to use here.
    calculation_type = calculation_type.lower()  # Allows input to be valid regardless of case.

    if calculation_type == "investment":
        print("You will now be asked to input information required for the investment calculation.")

        # Following section asks for all information required for investment calculation.
        deposit = float(input("Amount of money being deposited (GBP): "))  # GBP
        interest_rate = float(input("Interest rate per year (%): "))  # percentage points
        interest_years = int(input("Duration to invest (years): "))  # years
        interest_type = input("Simple or compound interest: ")

        interest_type = interest_type.lower()
        
        if interest_type == "simple":
            print("Running simple interest calculations...")
            investment_amount = round(deposit * (1 + interest_rate * interest_years), 2)  # Simple interest calculation.
        else:
            print("Running compound interest calculations...")
            investment_amount = round(deposit * math.pow((1 + interest_rate), interest_years), 2)  # Compound interest calculation.
        print("Total interest is £" + str(investment_amount) + ".")
        
        break
    
    elif calculation_type == "bond":
        print("You will now be asked to input information required for the home loan repayment calculation.")

        # Following section asks for all information required for bond calculation.
        bond_price = float(input("House price (GBP): "))  # GBP
        interest_rate = float(input("Interest rate per year (%): "))  # percentage points
        interest_months = int(input("How many months do you wish the spread bond repayments over: "))  # months

        bond_total = round(((interest_rate / 12) * bond_price) / (1-(1+interest_rate) ** (-interest_months)), 2)

        print("Amount to pay each month is £" + str(bond_total) + ".")
        
        break

    else:
        print("Sorry, that input wasn't recognised. Please type a 'investment' or 'bond'.")  # If no valid choice was made, loops back to the where user selects a calculator.
        continue