a = bool(int(input()))
b = bool(int(input()))
c = bool(int(input()))

d = int((a and (not b)) or ((not b) and c))

print(d)
