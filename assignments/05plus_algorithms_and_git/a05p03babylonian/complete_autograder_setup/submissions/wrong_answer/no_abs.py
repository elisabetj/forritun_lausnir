# Gather input from the user
number = int(input())
guess = int(input())
tolerance = float(input())

count = 0  # count the number of guesses
previous = 0  # track the previous calculated value

# Until we are within tolerance, keep inching our way towards the square root
while previous - guess > tolerance:
    previous = guess
    quotient = number / guess
    guess = (quotient + guess) / 2
    count += 1

print(guess)
print(count)
