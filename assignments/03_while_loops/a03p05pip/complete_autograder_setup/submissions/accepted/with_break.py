number = int(input())

no_7_found_yet = True
while number > 0:
    last_digit = number % 10

    if last_digit == 7:
        no_7_found_yet = False
        break  # No need to keep looking if we already found a 7
        # This is an acceptable use of break.

        # At least we have one condition in the head of the while loop
        # that immediately gives the reader an idea of
        # how the loop is guaranteed to end eventually.

        # But since we expect this to be our main exit point of the loop,
        # it's probably worth it to mention that in the head of the loop as well,
        # and since we're setting a boolean here anyway,
        # why not just check that in the head?
        # Only costs us one extra division before we get back to the head.

    number = number // 10

if no_7_found_yet:
    print("The number does not contain 7.")
else:
    print("The number contains 7.")
