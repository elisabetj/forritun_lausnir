#!/usr/bin/python3

DIGITS = 1
MAX_PRICE = 1000.0

total_price = 0.0
min_price = MAX_PRICE
num_items = 0

# Use the := operator to assign the value to the variable
# and use it in a comparison at the same time.
# The := operator is often called the walrus operator,
# as it looks like a smiley with eyes and the long tusks of a walrus.
# Requires Python 3.8 or higher.
while (price := float(input())) > 0:
    num_items += 1
    total_price += price

    if price < min_price:
        min_price = price

print("Number of items:", num_items)
print("Total price:", round(total_price, DIGITS))
if num_items > 0:
    print("Lowest price:", min_price)
