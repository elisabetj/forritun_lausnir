max_num = int(input())

root = 0
while root**3 <= max_num:
    number_to_check = root**3
    what_is_left = number_to_check
    sum_of_digits = 0

    while what_is_left > 0:
        last_digit = what_is_left % 10
        sum_of_digits += last_digit
        what_is_left = what_is_left // 10

    if sum_of_digits == root:
        print(number_to_check)
    
    root += 1
