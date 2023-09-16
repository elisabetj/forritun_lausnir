string = input()
char = input()

index = string.find(char)
while index != -1:
    print(index)
    index = string.find(char, index + 1)
