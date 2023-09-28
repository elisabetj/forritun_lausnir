from solution_code import is_substring_of


# Now that you have learned about defining your own functions,
# it is a good time to introduce the following common convention.
# You can wrap your program inside a main function.
def main():
    # If you want the output to look exactly like in the problem statement,
    # you want to use this:

    # first = input()
    # second = input()
    # result = is_substring_of(potential_substring, potential_superstring)
    # print(result)

    # But for running the program interactively,
    # you might want to do something like this:

    print(
        "So, you have two strings,",
        "and want to check if the first is contained in the second, eh?",
        "Well, I can help with that.",
    )
    potential_substring = input("Give me the first string: ")
    potential_superstring = input("Now, give me the other string: ")

    result = is_substring_of(potential_substring, potential_superstring)

    if result:
        print(
            f"Yes, the string '{potential_substring}'",
            f"is indeed contained in the string '{potential_superstring}'.",
        )
    else:
        print(
            f"No, the string '{potential_substring}'",
            f"is not contained in the string '{potential_superstring}'.",
        )


# Now that you have defined the main function, you can call it.
main()
