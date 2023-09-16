a_str = input()

is_palindrome = True
for index in range(len(a_str) // 2):
    if a_str[index] != a_str[-1 - index]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome!")
else:
    print("Nothing special about this string :(")
