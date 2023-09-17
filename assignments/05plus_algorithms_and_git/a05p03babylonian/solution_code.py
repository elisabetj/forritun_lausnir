# Gather input from the user.
number = int(input())
guess = int(input())
tolerance = float(input())

count = 0  # Count the number of guesses.
previous = 0  # Track the previous calculated value.

assert abs(previous - guess) > tolerance
# The input assurances in the problem description guarantee this,
# but it is nevertheless a good idea to document this assumption to make it explicit.

# Until we are within tolerance, keep inching our way towards the square root.
while abs(previous - guess) > tolerance:
    previous = guess
    assert guess != 0  # Before.
    quotient = number / guess
    guess = (quotient + guess) / 2
    assert guess != 0  # And after.
    count += 1

print(guess)
print(count)
