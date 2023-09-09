#!/usr/bin/python3

COMMISSION_RATE = 0.03
DECIMAL_DIGITS = 2

# To make sure these prompts appear on separate lines in the output on Gradescope
# (where the input is not displayed interleaved with the output),
# we can just use '\n' instead of a space at the end.
stock_symbol = input("The stock symbol:\n")
shares = int(input("Number of shares:\n"))
buy_price = float(input("The stock buying price:\n"))
sell_price = float(input("The stock selling price:\n"))
# Gradescope does not distinguish between type of whitespace in this particular problem.
# We just have to make sure there is some whitespace, any kind of whitespace
# (we could have more than one, even combine different kinds,
# like a space and a newline, for example).

total_buy_price = shares * buy_price
total_sell_price = shares * sell_price

buy_commission = total_buy_price * COMMISSION_RATE
sell_commission = total_sell_price * COMMISSION_RATE

profit_loss = total_sell_price - sell_commission - (total_buy_price + buy_commission)

print()
print("Transactions for stock:", stock_symbol)

print("Bought", shares, "shares", "@", buy_price)
print("Paid", round(total_buy_price, DECIMAL_DIGITS))
print("Commission when buying:", round(buy_commission, DECIMAL_DIGITS))

print("Sold", shares, "shares", "@", sell_price)
print("Received", round(total_sell_price, DECIMAL_DIGITS))
print("Commission when selling:", round(sell_commission, DECIMAL_DIGITS))

print("Profit or loss:", round(profit_loss, DECIMAL_DIGITS))
