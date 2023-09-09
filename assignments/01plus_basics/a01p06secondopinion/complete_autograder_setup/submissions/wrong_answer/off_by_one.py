total_seconds = int(input())

hours = 0
minutes = 0
while total_seconds > 3600:
    hours += 1
    total_seconds -= 3600

while total_seconds > 60:
    minutes += 1
    total_seconds -= 60


print(f"{hours} : {minutes} : {total_seconds}")
