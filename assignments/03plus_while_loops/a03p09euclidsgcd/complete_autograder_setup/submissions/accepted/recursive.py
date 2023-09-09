a = int(input())
b = int(input())

def gcd(a, b):
    return b if a == 0 else gcd(b%a, a)

print(gcd(a, b))
