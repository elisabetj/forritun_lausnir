a = bool(int(input()))
b = bool(int(input()))
c = bool(int(input()))

d = (a and (not b)) or ((not a) and c)

print(int(d))
