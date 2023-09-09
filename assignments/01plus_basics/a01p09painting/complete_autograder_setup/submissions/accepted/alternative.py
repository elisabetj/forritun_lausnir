import math

length_cm = 50

degrees = int(input())
radians = math.radians(degrees)

height_cm = math.tan(radians) * length_cm

print(f"{round(height_cm, 1):.1f}")
