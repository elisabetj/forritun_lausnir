max_number = int(input())

for number in 0, 1, 512, 4913, 5832, 17576, 19683:
    if number <= max_number:
        print(number)

# This is quicker, but it requires some justification,
# so it's kind of cheating ;)
