#!/usr/bin/python3

price_of_item = int(input())
amount_paid = int(input())
change = amount_paid - price_of_item

for bill in [20, 10, 5, 2, 1]:
    while change >= bill:
        print(bill)
        change -= bill
