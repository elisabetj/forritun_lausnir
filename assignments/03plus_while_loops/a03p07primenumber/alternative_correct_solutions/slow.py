n = int(input())

if n == 1:
    is_prime = False
else:
    is_prime = True

potential_factor = 2
while potential_factor < n:
    # Here we keep looking for a factor long after it has become hopeless to find one
    # (if the number turns out to be prime).
    # For example, if n == 1.000.003,
    # then as soon as we reach 1.001 and haven't found a factor,
    # it is unnecessary to continue,
    # so we're just wasting time going through the remaining 999.001 possibilities.
    if n % potential_factor == 0:
        is_prime = False
        break

    potential_factor += 1

if is_prime:
    print("prime")
else:
    print("not prime")
