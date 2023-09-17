n = int(input())

candidate = n**2 + 1
while candidate < (n + 1) ** 2:
    if candidate == 1:
        is_prime = False
    else:
        is_prime = True

    potential_factor = 2
    while potential_factor**2 <= candidate:
        if candidate % potential_factor == 0:
            is_prime = False
            break

        potential_factor += 1

    if is_prime:
        print(candidate)

    candidate += 1
