"""
Author: Cliff Smith
Date: June 21, 2026
File Name: smith_lemonadeStand.py
Description: This program simulates a lemonade stand by calculating the
cost of making lemonade and the profit earned from selling it.
"""

# Defining a function to calculate the total cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
    total_cost = lemons_cost + sugar_cost  # Add the cost of lemons and sugar
    return total_cost  # Return the total cost


# Defining a function to calculate the profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    total_cost = lemons_cost + sugar_cost  # Calculate the total cost
    profit = selling_price - total_cost  # Subtract cost from selling price
    return profit  # Return the profit


# Creating variables to test the functions
lemons_cost = 5.00
sugar_cost = 3.00
selling_price = 12.00

# Building a string for the cost breakdown using concatenation
cost_breakdown = "$" + str(lemons_cost) + " + $" + str(sugar_cost) + " = $" + str(calculate_cost(lemons_cost, sugar_cost))

# Calling the functions and printing the results to the console
total_cost_output = "Total Cost: " + cost_breakdown
print(total_cost_output)

profit_output = "Profit: $" + str(calculate_profit(lemons_cost, sugar_cost, selling_price))
print(profit_output)
