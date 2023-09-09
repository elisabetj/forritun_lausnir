max_num = int(input())

for number_to_check in range(0, max_num + 1):
    what_is_left = number_to_check
    sum_of_digits = 0

    while what_is_left > 0:
        last_digit = what_is_left % 10
        sum_of_digits += last_digit
        what_is_left = what_is_left // 10

    if sum_of_digits ** 3 == number_to_check:
        print(number_to_check)
