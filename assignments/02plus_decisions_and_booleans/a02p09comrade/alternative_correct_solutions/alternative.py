temp_now = int(input())
temp_prev = int(input())

RAISE = "raise"
KEEP = "keep"
LOWER = "lower"
SHUTDOWN = "shutdown"

SHUTDOWN_TEMP = 350
OPTIMAL_TEMP = 300

if temp_now == SHUTDOWN_TEMP:
    print(KEEP)
elif SHUTDOWN_TEMP <= temp_now:
    print(SHUTDOWN)
elif temp_prev < temp_now < OPTIMAL_TEMP:
    print(KEEP)
elif temp_now < OPTIMAL_TEMP and temp_now <= temp_prev:
    print(RAISE)
elif OPTIMAL_TEMP < temp_now < temp_prev:
    print(KEEP)
elif OPTIMAL_TEMP < temp_now and temp_prev <= temp_now: # or simply else
    print(LOWER)
else:
    assert False
