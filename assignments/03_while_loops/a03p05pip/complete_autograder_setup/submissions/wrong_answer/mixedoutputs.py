number = int(input())

no_7_found_yet = True
while number > 0 and no_7_found_yet:  # No need to keep looking if we already found a 7
    last_digit = number % 10
    if last_digit == 7:
        no_7_found_yet = False
    number = number // 10

if no_7_found_yet:
    print("The number contains 7.")
else:
    print("The number does not contain 7.")
