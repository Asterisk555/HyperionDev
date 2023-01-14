shopping_1 = input("What's the first item on your shopping list?")
shopping_2 = input("And the second?")
shopping_3 = input("And the third?")

print("\nThank you! Now I'm going to ask how much each item costs in GBP (just type the numbers).\n")

shopping_1_price = float(input("How much does " + shopping_1 + " cost?"))
shopping_2_price = float(input("How much does " + shopping_2 + " cost?"))
shopping_3_price = float(input("How much does " + shopping_3 + " cost?"))

shopping_price_sum = round(shopping_1_price + shopping_2_price + shopping_3_price,2)
shopping_price_avg = round(shopping_price_sum/3,2)

print("\nThe total of " + shopping_1 + ", " + shopping_2 + ", and " + shopping_3 + " is £" + str(shopping_price_sum) + " and the average price of the items is £" + str(shopping_price_avg))