largest_number_seen_so_far = 0

while (number := int(input())) >= 0:
    if number > largest_number_seen_so_far:
        largest_number_seen_so_far = number

print(largest_number_seen_so_far)
