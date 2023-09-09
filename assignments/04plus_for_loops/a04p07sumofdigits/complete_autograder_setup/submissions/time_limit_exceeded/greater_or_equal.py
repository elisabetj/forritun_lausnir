n = int(input())

total_sum = 0
while n >= 0:
    current_last_digit = n % 10
    total_sum += current_last_digit

    # Now discard the last digit,
    # so the next-to-last digit becomes the new last digit:
    n_with_last_digit_removed = n // 10
    n = n_with_last_digit_removed

print(total_sum)
