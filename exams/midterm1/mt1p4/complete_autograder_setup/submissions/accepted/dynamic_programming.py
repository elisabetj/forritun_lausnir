#!/usr/bin/python3

cost_of_item = int(input())
amount_paid = int(input())
change = amount_paid - cost_of_item

coin_sizes = [1, 2, 5, 10, 20]

min_coins = [float("inf")] * (change + 1)
min_coins[0] = 0


for i in range(1, change + 1):
    for coin_size in coin_sizes:
        if i >= coin_size:
            min_coins[i] = min((min_coins[i], min_coins[i - coin_size] + 1))

coin_sizes.reverse()
# Trace
while change > 0:
    for coin_size in coin_sizes:
        if (
            change >= coin_size
            and min_coins[change] != float("inf")
            and min_coins[change] == min_coins[change - coin_size] + 1
        ):
            print(coin_size)
            change -= coin_size
            break
    else:
        print("impossible")
        exit()
