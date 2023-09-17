# Gather input from the user.
number = int(input())
guess = int(input())
tolerance = float(input())

count = 0  # Count the number of guesses.
previous = 0  # Track the previous calculated value.

# Until we are within tolerance, keep inching our way towards the square root.
while abs(previous - guess) > tolerance:
    previous = guess
    quotient = number / guess
    guess = (quotient + guess) / 2
    count += 1

print(guess)
print(count)
