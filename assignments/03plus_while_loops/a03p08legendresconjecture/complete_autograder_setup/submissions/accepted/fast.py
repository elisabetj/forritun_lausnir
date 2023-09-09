from math import gcd

def miller_rabin(testee, witness):
    n, a = testee, witness
    if n % 2 == 0 or 1 < gcd(a, n) < n:
        return True
    q = n - 1
    k = 0
    while q % 2 == 0:
        q //= 2
        k += 1
    a = pow(a, q, n)
    if a == 1:
        return False
    for i in range(0, k):
        if a == n - 1:
            return False
        a = (a * a) % n
    return True

def is_prime(n):
    if n == 1:
        return False
    witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n in witnesses:
        return True
    # works for n < 3,317,044,064,679,887,385,961,981
    return not any(miller_rabin(n, witness) for witness in witnesses)

n = int(input())
print("Primes in the range", n ** 2, "and", (n + 1) ** 2, "are:")

# No need to check n ** 2 and (n+1) ** 2 themselves,
# since squares will never be primes anyway.
candidate = n ** 2 + 1
while candidate < (n + 1) ** 2:
    if is_prime(candidate):
        print(candidate)
    candidate += 1
