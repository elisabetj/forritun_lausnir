#!/usr/bin/python3

MIN_LENGTH = 6
MAX_LENGTH = 20
QUIT = "q"

total_count = 0
total_valid = 0
total_invalid = 0

passwd = input()

while True:
    if passwd[0] == QUIT:
        break
    total_count += 1
    length = len(passwd)
    if length < MIN_LENGTH or length > MAX_LENGTH:
        print(f"{passwd}: Invalid length.")
        total_invalid += 1

    else:
        found_lower = False
        found_upper = False
        found_number = False
        for i in range(0, length):
            ch = passwd[i]
            if ch.islower():
                found_lower = True
            if ch.isupper():
                found_upper = True
            if ch.isnumeric():
                found_number = True

        if not found_lower:
            print(f"{passwd}: Missing lower case letter.")
        if not found_upper:
            print(f"{passwd}: Missing upper case letter.")
        if not found_number:
            print(f"{passwd}: Missing numeric letter.")

        if found_lower and found_upper and found_number:
            total_valid += 1
            print(f"{passwd}: Valid password of length {length}.")
        else:
            total_invalid += 1

    passwd = input()

print(
    f"You tried {total_count} passwords, {total_valid} valid, {total_invalid} invalid."
)
