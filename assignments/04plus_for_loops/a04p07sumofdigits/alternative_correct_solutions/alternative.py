n = input()

# It's also possible to loop through the string of digits directly.
# Notice we have not converted n to an int, so it remains a string.
total_sum = 0
for digit in n:
    total_sum += int(digit)  # Now we convert, for the addition to work.

print(total_sum)
