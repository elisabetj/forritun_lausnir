n = int(input())

if n == 1:
    is_prime = False
else:
    is_prime = True

potential_factor = 2
while potential_factor**2 <= n:
    # If we have not found a proper factor
    # by the time we exceed the square root of n,
    # then we're not going to find one,
    # because any factor needs a complement, which will also be a factor,
    # and only one of them can be greater than the square root of n.
    if n % potential_factor == 0:
        is_prime = False
        break
        # No need to keep looking
        # once we determine that the number is not prime.
    potential_factor += 1

if is_prime:
    print("prime")
else:
    print("not prime")
