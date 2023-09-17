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

        # This is a good example of an acceptable use of break.
        # Note how, in the no_break solution,
        # the phrasing becomes more convoluted.
        # It would be confusing to a fresh reader if we just stated
        # while potential_factor**2 <= n and is_prime:
        # in the head of the loop
        # (if we already know it is a prime, then why keep looking?)
        # and confusion is not a friend of readability.

        # And if we want to say something like
        # while potential_factor**2 <= n and no_factorization_found:
        # then that does not really describe the case n == 1 well.
        # We could use separate booleans for those two cases,
        # but that would just be complicating the code.

    potential_factor += 1

if is_prime:
    print("prime")
else:
    print("not prime")
