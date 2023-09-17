largest_number_seen_so_far = 0

number = int(input())
while number >= 0:
    if number > largest_number_seen_so_far:
        largest_number_seen_so_far = number

    number = int(input())

print(largest_number_seen_so_far)
