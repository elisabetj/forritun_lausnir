temp_now = int(input())
temp_prev = int(input())

RAISE = "raise"
KEEP = "keep"
LOWER = "lower"
SHUTDOWN = "shutdown"

if temp_now == 300:
    print(KEEP)
elif temp_now >= 350:
    print(SHUTDOWN)
elif temp_prev > temp_now:
    print(RAISE)
elif temp_prev < temp_now:
    print(LOWER)
else:
    print(KEEP)
