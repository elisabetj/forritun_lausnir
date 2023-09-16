a_str = input()

is_palindrome = True
while a_str:
    if a_str[0] != a_str[-1]:
        is_palindrome = False
        break
    a_str = a_str[1:-1]

if is_palindrome:
    print("Palindrome!")
else:
    print("Nothing special about this string :(")
