a_str = input()
char_to_count = input()

index = 0
for character in a_str:
    if character == char_to_count:
        print(index)
    index += 1
