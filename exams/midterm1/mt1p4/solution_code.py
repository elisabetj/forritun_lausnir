#!/usr/bin/python3

price_of_item = int(input())
amount_paid = int(input())
change = amount_paid - price_of_item

while change > 0:
    if change >= 20:
        bill = 20
    elif change >= 10:
        bill = 10
    elif change >= 5:
        bill = 5
    elif change >= 2:
        bill = 2
    elif change >= 1:
        bill = 1

    print(bill)
    change -= bill
