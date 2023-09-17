number = int(input())
largest_number_seen_so_far = number
while number >= 0:
    if number > largest_number_seen_so_far:
        largest_number_seen_so_far = number

    number = int(input())

print(largest_number_seen_so_far)
