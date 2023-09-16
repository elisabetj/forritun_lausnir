a_str = input().lower()
char_to_count = input().lower()

index = 0
for char_in_str in a_str:
    if char_in_str == char_to_count:
        print(index)
    index += 1
