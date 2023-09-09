val_a_int = int(input())
val_b_int = int(input())
val_c_int = int(input())

d = (val_b_int * val_b_int) - (4 * val_a_int * val_c_int)

if d > 0:
    print(2)
elif d == 0:
    print(1)
else:
    print(0)
