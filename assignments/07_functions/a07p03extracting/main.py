from solution_code import extract_first_number_from_string


# Note that you can not call the function before it is has been defined,
# as would happen if you were to uncomment the following line.

# main()

# This is because at this time in the execution,
# the Python interpreter has not yet encountered the definition of the function.


def main():
    # If you want the output to look exactly like in the problem statement,
    # you want to use this:

    # run_like_hell_ehem_I_mean_run_like_samples()

    # But for running the program interactively,
    # you might want to do something like this:

    run_interactive()

    # Notice how we can define more than one function,
    # and call one function inside another function.
    # We can call functions defined below this line in the code,
    # because we're inside a function that was called
    # after the other functions were defined,
    # so Python has already set them up.

    # This is why we always want to call the main function at the very end of the file.


# If we call main() from here,
# then the other functions below do not exist yet,
# so although we are able to call main() itself,
# it would crash as soon as it tries to call one of the other functions.


# Feel free to rename this function.
# Just make sure to use the updated name also where you call the function.
def run_like_hell_ehem_I_mean_run_like_samples():
    search_string = input()
    first_number = extract_first_number_from_string(search_string)
    print(first_number)


def run_interactive():
    demand = "Numbers! Give me numbers! But hide them inside a string for me to find: "
    search_string = input(demand)

    first_number = extract_first_number_from_string(search_string)

    if first_number == -1:
        print("Hey! There is no number in this string >:(")
    else:
        print(f"Delicious! {first_number}, I see you!")


main()
