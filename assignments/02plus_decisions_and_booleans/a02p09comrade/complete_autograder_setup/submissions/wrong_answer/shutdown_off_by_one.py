temp_now = int(input())
temp_prev = int(input())

RAISE = "raise"
KEEP = "keep"
LOWER = "lower"
SHUTDOWN = "shutdown"

if temp_now == 300:
    print(KEEP)
elif temp_now > 350:
    print(SHUTDOWN)
elif temp_now < 300:
    if temp_prev < temp_now:
        print(KEEP)
    else:
        print(RAISE)
else:
    if temp_prev > temp_now:
        print(KEEP)
    else:
        print(LOWER)
