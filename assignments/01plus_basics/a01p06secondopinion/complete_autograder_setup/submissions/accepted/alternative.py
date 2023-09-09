total_seconds: int = int(input())

seconds: int = total_seconds % 60
total_minutes: int = total_seconds // 60
minutes: int = total_minutes % 60
hours: int = total_minutes // 60

print(hours, ":", minutes, ":", seconds)
