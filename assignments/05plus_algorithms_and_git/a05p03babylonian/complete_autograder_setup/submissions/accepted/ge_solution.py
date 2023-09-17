number = int(input())
guess = int(input())
tolerance = float(input())

count = 0
previous = 0 if abs(guess) >= tolerance else 2 * tolerance
assert abs(previous - guess) >= tolerance

# Check that this works too, with equality allowed,
# to make sure students won't get caught in a floating point error.
while abs(previous - guess) >= tolerance:
    previous = guess
    quotient = number / guess
    guess = (quotient + guess) / 2
    count += 1

print(guess)
print(count)
