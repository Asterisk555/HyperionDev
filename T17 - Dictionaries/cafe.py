# Create a list called menu, which contains items in the cafe.
menu = ["sand", "cape", "colt", "brownies"]
# Create a dictionary called stock, which contains the stock value for each item on your menu.
stock = {"sand":2, "cape":4, "colt":10, "brownies":7}
# # Create another dictionary called price, which contains the prices for each item on your menu.
price = {"sand":300.1, "cape":7.2, "colt":11.9, "brownies":12}

total_stock_price = 0  # empty variable to store stock prices

for i in menu:
    # Calculate the total stock worth in the cafe.
    total_stock_price = stock[i] * price[i] + total_stock_price

print(total_stock_price)  # print out the result of the calculation.