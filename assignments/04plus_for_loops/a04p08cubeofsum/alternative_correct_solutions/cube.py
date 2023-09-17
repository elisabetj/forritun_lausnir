max_number = int(input())

# Rather few numbers even have an integer cube root,
# so it's quicker to consider only those that do.
root = 0
while root**3 <= max_number:
    number_to_check = root**3
    sum_of_digits = 0

    what_is_left = number_to_check
    while what_is_left > 0:
        last_digit = what_is_left % 10
        sum_of_digits += last_digit
        what_is_left = what_is_left // 10

    if sum_of_digits == root:
        print(number_to_check)

    root += 1
