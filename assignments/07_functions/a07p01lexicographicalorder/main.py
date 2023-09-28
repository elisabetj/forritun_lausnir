from solution_code import precedes

# If you want the output to look exactly like in the problem statement,
# you want to use this:

# first = input()
# second = input()
# result = precedes(first, second)
# print(result)

# But for running the program interactively,
# you might want to do something like this:

first = input("Give me a string: ")
second = input("Give me another string: ")

result = precedes(first, second)

print(f"The string '{result}' has alphabetical precedence.")
