#!/usr/bin/python3

OO = float("inf")  # Plus infinity.
DIGITS = 1
MAX_PRICE = 1000.0

total_price = 0.0
minimum_price = OO
number_of_items = 0

price = float(input())
while price > 0:
    number_of_items += 1
    total_price += price

    if price < minimum_price:
        minimum_price = price

    price = float(input())

print("Number of items:", number_of_items)
print("Total price:", round(total_price, DIGITS))
if number_of_items > 0:
    print("Lowest price:", minimum_price)
