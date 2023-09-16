temp_now = int(input())
temp_prev = int(input())

RAISE = "raise"
KEEP = "keep"
LOWER = "lower"
SHUTDOWN = "shutdown"
SHUTDOWN_TEMP = 350
OPTIMAL_TEMP = 300

if temp_now == OPTIMAL_TEMP:
    print(KEEP)
elif SHUTDOWN_TEMP <= temp_now:
    print(SHUTDOWN)
elif temp_now < OPTIMAL_TEMP:
    if temp_prev < temp_now:
        print(KEEP)
    else:
        print(RAISE)
else:
    if temp_prev > temp_now:
        print(KEEP)
    else:
        print(LOWER)
