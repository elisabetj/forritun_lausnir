import math

length_cm = 50

degrees = int(input())
radians = math.radians(degrees)

hypotenuse = length_cm / math.cos(radians)
height_cm = math.sin(radians) * hypotenuse

print(round(height_cm, 2))
