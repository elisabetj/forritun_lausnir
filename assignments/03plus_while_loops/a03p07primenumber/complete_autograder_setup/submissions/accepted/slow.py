n = int(input())

if n == 1:
    is_prime = False
else:
    is_prime = True

potential_factor = 2
while potential_factor < n:
    if n % potential_factor == 0:
        is_prime = False
        break
    potential_factor += 1

if is_prime:
    print("prime")
else:
    print("not prime")
