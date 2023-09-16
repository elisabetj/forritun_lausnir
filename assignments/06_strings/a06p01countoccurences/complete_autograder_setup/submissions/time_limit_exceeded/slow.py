a_str = input()
char_to_count = input()

offset = 0

while True:
    index = a_str.find(char_to_count)
    if index == -1:
        break
    print(index + offset)
    offset += index + 1
    a_str = a_str[index + 1 :]
