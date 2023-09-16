a_str = input()
n = len(a_str)

count_same = 0
for i in range(n // 2):
    if a_str[i] == a_str[n - i - 1]:
        count_same += 1

if 2 * count_same == n:
    print("Palindrome!")
else:
    print("Nothing special about this string :(")
