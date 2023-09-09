total_seconds: int = int(input())

hours: int = total_seconds // 3600
remainder: int = total_seconds % 3600
minutes: int = remainder // 60
seconds: int = remainder % 60

print(hours, minutes, seconds)
