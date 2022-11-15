# Financial calculator program for investments and home loans.
# Requires user input at several points.
# Uses while loops and if statements.

import math

print("This program allows you to accesss our investment calculator, and home loan repayment calculator.\ninvestment - to calculate the amount of interest you'll earn on your investment\nbond - to calculate the amount you'll have to pay on a home loan")

while True:

    calculation_type = input("Enter either 'investment' or 'bond' to proceed: ")
    calculation_type = calculation_type.lower()  # allows input to be valid regardless of case

    if calculation_type == "investment":
        print("You will now be asked to input information required for the investment calculation.")
        deposit = float(input("Amount of money being deposited (GBP): "))
        interest_rate = float(input("Interest rate per year (%): "))
        interest_years = int(input("Duration to invest (years): "))
        interest_type = input("Simple or compound interest: ")
        interest_type = interest_type.lower()
        if interest_type == "simple":
            print("Running simple interest calculations...")
            investment_amount = round(deposit * (1 + interest_rate * interest_years), 2)
        else:
            print("Running compound interest calculations...")
            investment_amount = round(deposit * math.pow((1 + interest_rate), interest_years), 2)
        print("Total interest is £" + str(investment_amount) + ".")
        break
    elif calculation_type == "bond":
        print("You will now be asked to input information required for the home loan repayment calculation.")
        bond_price = float(input("House price (GBP): "))
        interest_rate = float(input("Interest rate per year (%): "))
        interest_months = int(input("How many months do you wish the spread bond repayments over: "))
        bond_total = round(((interest_rate / 12) * bond_price) / (1-(1+interest_rate) ** (-interest_months)), 2)
        print("Amount to pay each month is £" + str(bond_total) + ".")
        break
    else:
        print("Sorry, that input wasn't recognised. Please type a 'investment' or 'bond'.")
        continue



